import cv2
import numpy as np
import time
import collections

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
VIDEO_PATH       = "/home/exam/test.mp4"
PANEL_W, PANEL_H = 320, 240          # size of each panel
ADAPT_HIGH       = 15.0              # if activity > this %, raise threshold
ADAPT_LOW        =  4.0              # if activity < this %, lower threshold
ADAPT_STEP       =  1                # how much to change threshold each step
ADAPT_COOLDOWN   = 10                # frames between auto-adjustments


# ─────────────────────────────────────────────
# VIDEO HELPERS
# ─────────────────────────────────────────────
def open_video():
    cap = cv2.VideoCapture(VIDEO_PATH)
    if cap.isOpened():
        print("[INFO] Using video:", VIDEO_PATH)
        return cap
    print("[ERROR] Could not open video file:", VIDEO_PATH)
    exit(1)

def read_frame(cap):
    ret, frame = cap.read()
    if not ret:                          # loop video when it ends
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = cap.read()
    return frame if ret else None


# ─────────────────────────────────────────────
# DVS PROCESSOR
# ─────────────────────────────────────────────
class DVSProcessor:
    def __init__(self, threshold=20):
        self.threshold   = threshold
        self.adaptive    = False         # toggle with 'A' key
        self._prev_gray  = None

        # rolling buffers
        self._activity_buf  = collections.deque(maxlen=60)   # last 60 frames
        self._event_rate_buf = collections.deque(maxlen=10)  # for smoothing EPS
        self._adapt_timer   = 0                               # cooldown counter
        self._last_time     = time.time()

    # ── main processing ──────────────────────
    def process(self, bgr):
        gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (3, 3), 0)

        if self._prev_gray is None:
            self._prev_gray = gray.copy()
            return None

        # ── frame difference ─────────────────
        diff = gray.astype(np.int16) - self._prev_gray.astype(np.int16)

        pos_mask    = (diff >  self.threshold).astype(np.uint8) * 255   # ON  events
        neg_mask    = (diff < -self.threshold).astype(np.uint8) * 255   # OFF events
        active_mask = ((np.abs(diff)) > self.threshold).astype(np.uint8) * 255

        # ── sparse Canny edges (only on active pixels) ──
        edges_full    = cv2.Canny(gray, 40, 120)
        sparse_events = cv2.bitwise_and(edges_full, active_mask)

        # ── activity % ───────────────────────
        total_px      = active_mask.size
        active_px     = int(np.count_nonzero(active_mask))
        activity_pct  = 100.0 * active_px / total_px
        self._activity_buf.append(activity_pct)

        # ── event rate (events per second) ───
        now       = time.time()
        dt        = max(now - self._last_time, 1e-6)
        eps       = int(np.count_nonzero(sparse_events)) / dt   # events/sec
        self._event_rate_buf.append(eps)
        self._last_time = now

        # ── adaptive threshold ────────────────
        self._adapt_timer += 1
        if self.adaptive and self._adapt_timer >= ADAPT_COOLDOWN:
            self._adapt_timer = 0
            smoothed = np.mean(self._activity_buf)
            if smoothed > ADAPT_HIGH:
                self.threshold = min(self.threshold + ADAPT_STEP, 100)
            elif smoothed < ADAPT_LOW:
                self.threshold = max(self.threshold - ADAPT_STEP, 1)

        self._prev_gray = gray.copy()

        return dict(
            gray          = gray,
            active_mask   = active_mask,
            pos_mask      = pos_mask,
            neg_mask      = neg_mask,
            sparse_events = sparse_events,
            activity_pct  = activity_pct,
            saved_pct     = 100.0 - activity_pct,
            smoothed_act  = float(np.mean(self._activity_buf)),
            event_rate    = float(np.mean(self._event_rate_buf)),
            activity_hist = list(self._activity_buf),   # for graph
        )


# ─────────────────────────────────────────────
# FRAME BUILDERS
# ─────────────────────────────────────────────
def build_event_frame(r):
    """Composite event map: green=ON, red=OFF, white=confirmed edge."""
    H, W = r['gray'].shape
    out = np.zeros((H, W, 3), dtype=np.uint8)
    on_bg  = cv2.bitwise_and(r['pos_mask'], cv2.bitwise_not(r['sparse_events']))
    off_bg = cv2.bitwise_and(r['neg_mask'], cv2.bitwise_not(r['sparse_events']))
    out[on_bg  > 0] = (0,  200, 80)     # green  — ON  background
    out[off_bg > 0] = (60,  60, 220)    # red    — OFF background
    out[r['sparse_events'] > 0] = (255, 255, 255)  # white — confirmed edge
    return out


def build_polarity_panel(mask, label_text, color_on):
    """Coloured single-polarity panel (ON or OFF)."""
    H, W = mask.shape
    out  = np.zeros((H, W, 3), dtype=np.uint8)
    out[mask > 0] = color_on
    put(out, label_text, (8, 22), scale=0.5, color=(255, 255, 255))
    return out


def build_stats_panel(r, fps, dvs, W=PANEL_W, H=PANEL_H):
    """Black panel with metrics + mini activity graph."""
    panel = np.zeros((H, W, 3), dtype=np.uint8)

    # ── text metrics ─────────────────────────
    lines = [
        ("METRICS",                       (8, 26),  0.55, (0, 255, 180)),
        (f"FPS        : {fps:.1f}",       (8, 54),  0.45, (200, 200, 200)),
        (f"Threshold  : {dvs.threshold}", (8, 74),  0.45, (200, 200, 200)),
        (f"Activity   : {r['activity_pct']:.1f}%",  (8, 94),  0.45, (200, 200, 200)),
        (f"Saved work : {r['saved_pct']:.1f}%",     (8, 114), 0.45, (200, 200, 200)),
        (f"Event rate : {r['event_rate']:.0f} e/s",  (8, 134), 0.45, (0, 220, 255)),
        (f"Adaptive   : {'ON' if dvs.adaptive else 'OFF'}",
                                          (8, 154), 0.45,
                                          (0, 255, 100) if dvs.adaptive else (100, 100, 100)),
    ]
    for text, pos, scale, color in lines:
        put(panel, text, pos, scale=scale, color=color)

    # ── mini rolling activity graph ───────────
    hist = r['activity_hist']
    if len(hist) > 1:
        gh, gw = 60, W - 16          # graph height / width
        gx, gy = 8, H - gh - 14     # top-left corner of graph

        # background box
        cv2.rectangle(panel, (gx - 2, gy - 2), (gx + gw + 2, gy + gh + 2),
                      (40, 40, 40), -1)

        # ADAPT_HIGH / ADAPT_LOW reference lines
        for ref_val, ref_col in [(ADAPT_HIGH, (0, 140, 255)), (ADAPT_LOW, (255, 140, 0))]:
            ry = gy + gh - int(ref_val / 30.0 * gh)   # 30% = top of graph
            cv2.line(panel, (gx, ry), (gx + gw, ry), ref_col, 1)

        # plot line
        n     = len(hist)
        xs    = [gx + int(i * gw / (n - 1)) for i in range(n)]
        ys    = [gy + gh - int(min(v, 30) / 30.0 * gh) for v in hist]
        for i in range(1, n):
            cv2.line(panel, (xs[i-1], ys[i-1]), (xs[i], ys[i]),
                     (0, 255, 180), 1, cv2.LINE_AA)

        put(panel, "Activity % (30f)", (gx, gy - 5), scale=0.35, color=(150, 150, 150))

    return panel


# ─────────────────────────────────────────────
# UTILS
# ─────────────────────────────────────────────
def put(img, text, pos, scale=0.55, color=(0, 255, 180)):
    cv2.putText(img, text, pos, cv2.FONT_HERSHEY_SIMPLEX,
                scale, color, 1, cv2.LINE_AA)

def resize(img, w=PANEL_W, h=PANEL_H):
    return cv2.resize(img, (w, h))

def gray_to_bgr(img):
    return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def main():
    cap = open_video()
    dvs = DVSProcessor(threshold=20)
    fps = 0.0
    t_prev = time.time()

    print("Controls:")
    print("  Q / ESC  — quit")
    print("  + / =    — raise threshold")
    print("  -        — lower threshold")
    print("  A        — toggle adaptive threshold")
    print("  S        — save screenshot")

    while True:
        frame = read_frame(cap)
        if frame is None:
            continue

        # ── FPS ──────────────────────────────
        now   = time.time()
        fps   = 0.9 * fps + 0.1 / max(now - t_prev, 1e-6)
        t_prev = now

        result = dvs.process(frame)
        if result is None:
            continue

        # ── build panels (all 320×240) ───────
        p_orig   = resize(frame)
        p_event  = resize(build_event_frame(result))
        p_on     = resize(build_polarity_panel(
                       result['pos_mask'], "ON Events  [brighter]", (0, 220, 80)))
        p_off    = resize(build_polarity_panel(
                       result['neg_mask'], "OFF Events [darker]",   (60, 60, 220)))
        p_mask   = gray_to_bgr(resize(result['active_mask']))
        p_stats  = build_stats_panel(result, fps, dvs)

        # ── label top-row panels ─────────────
        put(p_orig,  "Original",   (8, 20), scale=0.5, color=(255, 255, 255))
        put(p_event, "Event Map",  (8, 20), scale=0.5, color=(255, 255, 255))
        put(p_mask,  "Active Mask",(8, 20), scale=0.5, color=(255, 255, 255))

        # ── assemble 2×3 grid ────────────────
        row1 = np.hstack([p_orig,  p_event, p_mask ])
        row2 = np.hstack([p_on,    p_off,   p_stats])
        display = np.vstack([row1, row2])

        cv2.imshow("Neuromorphic DVS v2", display)

        # ── keyboard ─────────────────────────
        key = cv2.waitKey(1) & 0xFF
        if key in (ord('q'), 27):
            break
        elif key in (ord('+'), ord('=')):
            dvs.threshold = min(dvs.threshold + 5, 100)
            print(f"[Manual] Threshold → {dvs.threshold}")
        elif key == ord('-'):
            dvs.threshold = max(dvs.threshold - 5, 1)
            print(f"[Manual] Threshold → {dvs.threshold}")
        elif key == ord('a'):
            dvs.adaptive = not dvs.adaptive
            print(f"[Adaptive] {'ON' if dvs.adaptive else 'OFF'}")
        elif key == ord('s'):
            fname = f"/home/exam/dvs_{int(time.time())}.png"
            cv2.imwrite(fname, display)
            print(f"[Saved] {fname}")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
