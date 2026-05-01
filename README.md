# SKILL LAB PRACTICAL HACKATHON
**Final Project README**
> Project Weight: 100% | Team Size: 2 students | Project Duration: 16 hours | Project Type: Playful, interactive, technology-based experience

---

## Before you begin
Repository forked and renamed as: **SKILLLAB_PROR-2026-EdgeDetectors**

---

## 1. Team Identity

### 1.1 Studio / Group Name
**EdgeDetectors**

### 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| Sahil Singh *(Team Lead)* | Hardware Setup & Integration | Project Coordination | Raspberry Pi setup, peripheral configuration, team management |
| Kartik Nagare | Coding | Testing | Algorithm design, Python, OpenCV, frame processing pipeline |
| Shreyash Garud | Computer Vision | Documentation | Panel layout, display assembly, metrics rendering |
| Kunal Sahasrabudhe | Vivado Testing & Debugging | Coding Support | Live testing on FPGA, debugging, adaptive threshold validation |

### 1.3 Project Title
**Neuromorphic DVS Simulation + Edge Detection on Raspberry Pi**

### 1.4 One-Line Pitch
A real-time neuromorphic vision system running on Raspberry Pi that simulates how the brain sees — only processing pixels that actually change, saving compute and mimicking biological vision.

### 1.5 Expanded Project Idea
This project builds two connected computer vision systems on a Raspberry Pi.

The first is a classical edge detection pipeline (`edge_basic.py`) that takes a static image and runs three different edge detectors — Sobel Magnitude, Canny, and Laplacian — simultaneously, displaying all four panels (original + three detectors) in a tiled window. This is the baseline: how conventional computer vision finds edges.

The second and main system (`neuromorphic_dvs.py`) simulates a Dynamic Vision Sensor (DVS) — a type of neuromorphic camera inspired by biological vision. Instead of processing every pixel in every frame (like a normal camera), it only fires on pixels that change brightness beyond a threshold. This is exactly how the human retina works: it sends signals only when something changes, ignoring the static background entirely. The result is a sparse, event-driven system that is far more compute-efficient than conventional frame-by-frame processing — and visually striking. The system runs live on a Raspberry Pi using a test video file, displaying ON events (pixels getting brighter), OFF events (pixels getting darker), confirmed sparse edges, activity metrics, polarity panels, event rate, adaptive threshold, and a rolling activity graph — all in real time.

---

## 2. Inspiration

### 2.1 References

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| Research concept | Neuromorphic computing / Dynamic Vision Sensors (DVS cameras) | The idea that biological vision is event-driven, not frame-driven |
| OpenCV documentation | https://docs.opencv.org | Sobel, Canny, Laplacian implementations and frame differencing |
| Academic concept | Sparse computation in neural systems | Only processing what changes = massive compute savings |

### 2.2 Original Twist
Most edge detection projects run all algorithms on every pixel of every frame — brute force. This project flips that: it first identifies *which* pixels have changed (active pixels), and only runs edge detection on those. This is true neuromorphic-style sparse processing. The visual output — green ON events, red OFF events, white confirmed edges on a black background — directly shows the brain-inspired computation happening in real time.

---

## 3. Project Intent

### 3.1 User Journey
Arjun opens the terminal on the Raspberry Pi and runs `python3 ~/neuromorphic_dvs.py`. A window appears with six panels: the original video on the left, and five panels showing the system's interpretation of motion — active pixels, ON events glowing green, OFF events in red, confirmed edges in white, and a live graph tracking how busy the scene is over time.

He watches the video play. Most of the screen is black — the system is ignoring the static background completely. Only the moving parts of the scene fire events. He presses `+` to raise the threshold — fewer pixels fire, only the strongest motion survives. He presses `A` — adaptive mode kicks in, and the system starts auto-tuning the threshold to keep activity in the ideal range. He presses `S` to save a screenshot. He presses `Q` to quit.

He then runs `python3 ~/edge_basic.py` — a static image opens in a 2×2 grid showing the original alongside Sobel, Canny, and Laplacian edge maps side by side. He can see exactly how each algorithm interprets the same image differently.

---

## 4. Definition of Success

### 4.1 Definition of "Usable"
The project is usable when both scripts run without errors on the Raspberry Pi, produce correct visual output, respond to keyboard controls, and clearly demonstrate the difference between conventional edge detection and neuromorphic event-driven processing.

### 4.2 Minimum Usable Version
- `edge_basic.py` loads an image and shows Sobel, Canny, Laplacian in a tiled window
- `neuromorphic_dvs.py` reads from video, shows ON/OFF events and active mask in real time
- Threshold adjustable with keyboard
- FPS and activity % displayed on screen

### 4.3 Stretch Features
- Polarity separation panels (ON and OFF shown independently) ✅ Done
- Event rate counter (events per second) ✅ Done
- Adaptive threshold (auto-adjusts based on scene activity) ✅ Done
- Real-time rolling activity graph ✅ Done
- Motion bounding boxes around event clusters 🔄 In progress
- Per-region activity heatmap overlay
- Canny threshold live keyboard controls
- Record DVS output to video file

---

## 5. System Overview

### 5.1 Project Type
- ✅ Electronics-based (Raspberry Pi)
- ✅ Sensor-based (camera / video input)
- ✅ Screen/UI-based (OpenCV display window)
- ✅ Game logic based (real-time keyboard controls, adaptive logic)

### 5.2 High-Level System Description
**Input:** A video file (`test.mp4`) is read frame by frame. A static image (`test.jpg`) is used for the edge detection script.

**Processing:** Each frame is converted to grayscale and blurred. Frame differencing computes which pixels changed beyond a threshold — these are the "events". Positive differences are ON events (brighter), negative are OFF events (darker). Canny edge detection runs only on active pixels (sparse processing). Metrics — activity %, event rate, saved compute % — are calculated each frame. An adaptive controller optionally auto-adjusts the threshold.

**Output:** A multi-panel OpenCV window displays the original frame, active mask, event map, ON polarity panel, OFF polarity panel, and a stats panel with a live rolling graph. All rendered at real-time frame rates on the Pi.

**Physical structure:** Raspberry Pi connected to a monitor. No external hardware required — runs entirely in software using a test video file.

### 5.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| test.mp4 (video file) | Input | Source frames for DVS simulation |
| test.jpg (image file) | Input | Source image for static edge detection |
| Frame differencing | Processing | Detects which pixels changed (events) |
| Canny (sparse) | Processing | Finds confirmed edges only on active pixels |
| Adaptive controller | Processing | Auto-adjusts threshold to maintain target activity range |
| OpenCV display window | Output | Shows all panels — events, masks, stats, graph |
| Keyboard (Q / + / - / A / S) | Control | Quit, adjust threshold, toggle adaptive, save screenshot |

---

## 6. System Design and Visual Planning

### 6.1 Concept Architecture

```
VIDEO FILE (test.mp4)
        │
        ▼
   Frame Reader (loops on end)
        │
        ▼
   Grayscale + Gaussian Blur
        │
        ▼
   Frame Differencing (current - previous)
   ┌────┴────┐
   ▼         ▼
ON mask    OFF mask
(diff > T) (diff < -T)
   └────┬────┘
        │ Active Mask (union)
        ▼
   Canny Edge Detection (full frame)
        │
        ▼
   Bitwise AND → Sparse Events (edges only on active pixels)
        │
        ▼
   Metrics: Activity%, Saved%, Event Rate (e/s), Smoothed Activity
        │
        ▼
   Adaptive Threshold Controller (optional, toggle A)
        │
        ▼
   Build 6 display panels → assemble 2×3 grid → imshow
```

### 6.2 Display Layout

```
┌─────────────┬─────────────┬─────────────┐
│  Original   │  Event Map  │ Active Mask │
│  (video)    │ G=ON R=OFF  │ white=      │
│             │ W=edge      │ changed px  │
├─────────────┼─────────────┼─────────────┤
│  ON Events  │ OFF Events  │    Stats    │
│  (green)    │  (blue/red) │  + Graph    │
└─────────────┴─────────────┴─────────────┘
Each panel: 320×240 px  |  Total window: 960×480 px
```

### 6.3 Key Parameters

| Parameter | Value |
|---|---|
| Panel size | 320 × 240 px each |
| Total display | 960 × 480 px (2 rows × 3 cols) |
| Default threshold | 20 |
| Adaptive high limit | 15% activity → raise threshold |
| Adaptive low limit | 4% activity → lower threshold |
| Adaptive cooldown | 10 frames between adjustments |
| Activity history buffer | 60 frames rolling |
| Event rate smoothing | 10 frames |

---

## 7. Electronics Planning

### 7.1 Components Used

| Component | Quantity | Purpose |
|---|---|---|
| Raspberry Pi | 1 | Main compute — runs all Python scripts |
| Monitor | 1 | Display output for OpenCV windows |
| Keyboard | 1 | Live controls (Q, +, -, A, S) |
| MicroSD card | 1 | OS and code storage |
| Power supply | 1 | Power the Pi |

### 7.2 Wiring Plan
No external wiring required. The Raspberry Pi runs entirely in software. The monitor connects via HDMI. The keyboard connects via USB. The video file (`test.mp4`) and image (`test.jpg`) are stored locally on the Pi at `/home/exam/`.

### 7.3 Circuit Diagram
Not applicable — software-only project. No external electronics or wiring beyond standard Raspberry Pi peripherals.

### 7.4 Power Plan

| Question | Response |
|---|---|
| Power source | Standard Raspberry Pi USB-C power supply |
| Voltage required | 5V @ 3A |
| Current concerns | None — no motors or high-draw peripherals |
| Safety concerns | None beyond standard Pi power supply usage |

---

## 8. Software Planning

### 8.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| Python 3 | Main programming language |
| OpenCV (python3-opencv) | Image processing, display, video capture |
| NumPy | Array math — frame differencing, masking, metrics |
| collections.deque | Rolling buffers for activity history and event rate |
| time | FPS calculation and event rate timing |

### 8.2 Software Logic / Algorithm

**Startup:** Video capture opens `test.mp4`. DVSProcessor initialises with threshold=20 and empty history buffers. FPS counter starts.

**Input handling:** `cv2.waitKey(1)` checks keyboard every frame. Q/ESC → quit. `+`/`=` → raise threshold by 5. `-` → lower threshold by 5. `A` → toggle adaptive mode. `S` → save screenshot to `/home/exam/dvs_<timestamp>.png`.

**Frame processing:** Each frame is converted to grayscale and Gaussian blurred (3×3). Frame difference is computed against previous frame. Pixels exceeding threshold in positive direction → ON mask. Negative direction → OFF mask. Union → active mask. Canny runs on full frame; bitwise ANDed with active mask → sparse events (confirmed edges on active pixels only).

**Metrics:** `activity_pct` = active pixels / total pixels × 100. `saved_pct` = 100 - activity_pct. `event_rate` = sparse event pixel count / elapsed time (events/sec). All values smoothed with rolling deques.

**Adaptive threshold:** If adaptive mode ON and cooldown elapsed: if smoothed activity > 15% → raise threshold by 1. If smoothed activity < 4% → lower threshold by 1. Cooldown = 10 frames between adjustments.

**Output:** Six panels built and assembled into a 2×3 grid. Displayed via `cv2.imshow`. Video loops automatically when it ends.

**Reset:** No explicit reset needed — video loops. Threshold and adaptive state persist until manually changed or script restarts.

### 8.3 Code Flowchart

```
START
  │
  ├── Open test.mp4
  ├── Init DVSProcessor (threshold=20)
  └── Init FPS counter
        │
        ▼
  MAIN LOOP ──────────────────────────────────────┐
  │                                               │
  ├── read_frame() → if end of video: loop back   │
  │                                               │
  ├── Calculate FPS (exponential smoothing)       │
  │                                               │
  ├── DVSProcessor.process(frame):                │
  │     ├── Grayscale + GaussianBlur              │
  │     ├── Frame diff → pos_mask, neg_mask       │
  │     ├── active_mask = pos OR neg              │
  │     ├── Canny on full frame                   │
  │     ├── sparse_events = Canny AND active_mask │
  │     ├── Compute activity%, saved%, event_rate │
  │     ├── Update rolling history buffers        │
  │     └── Adaptive threshold adjustment         │
  │                                               │
  ├── Build 6 display panels                      │
  ├── Assemble 2×3 grid                           │
  ├── cv2.imshow()                                │
  │                                               │
  ├── cv2.waitKey(1) — check keyboard:            │
  │     ├── Q / ESC  → BREAK                      │
  │     ├── + / =    → threshold up               │
  │     ├── -        → threshold down             │
  │     ├── A        → toggle adaptive            │
  │     └── S        → save screenshot            │
  │                                               │
  └────────────────────────────────────────────────┘
        │
        ▼
  cap.release()
  cv2.destroyAllWindows()
  END
```

---

## 9. Bill of Materials

### 9.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Spec | Why This Choice? |
|---|---|---|---|---|---|---|
| Raspberry Pi | 1 | Yes | No | ₹0 | Pi 3B+ or 4 | Main compute platform |
| MicroSD Card | 1 | Yes | No | ₹0 | 16GB+ | OS and code storage |
| Monitor + HDMI | 1 | Yes | No | ₹0 | Any | Display output |
| Keyboard | 1 | Yes | No | ₹0 | USB | Live keyboard controls |
| test.mp4 | 1 | No | No | ₹0 | MP4 v2, from w3schools | Test input — no camera needed |
| test.jpg | 1 | No | No | ₹0 | JPEG | Static image for edge_basic.py |

### 9.2 Material Justification
The entire project runs in software — no custom hardware required beyond a standard Raspberry Pi setup. OpenCV was installed via `apt` (`python3-opencv`) to ensure ARM compatibility without needing to compile from source. A test video file was used in place of a physical camera so the system could be developed and tested without camera hardware.

### 9.3 Items Purchased
Not applicable — all components were available in kit or downloaded freely. No purchases required.

### 9.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---|
| Electronics | ₹0 (all in kit) |
| Software | ₹0 (all open source) |
| Test files | ₹0 (downloaded free) |
| **Total** | **₹0** |

### 9.5 Budget Reflection
No budget was spent. The project was deliberately designed to be software-only so it could run on the existing Raspberry Pi kit without any additional procurement.

---

## 10. Planning the Work

### 10.1 Team Working Agreement
Work was divided by feature — one member focused on the core DVS algorithm and frame processing pipeline, the other on display assembly, metrics, and testing. Decisions were made by trying both approaches and keeping what worked. Progress was checked after each feature by running the script live and verifying visual output on the Pi. Documentation was updated after each working milestone.

### 10.2 Task Breakdown

| Task ID | Task | Owner | Est. Hours | Status |
|---|---|---|---|---|
| T1 | edge_basic.py — Sobel, Canny, Laplacian, 2×2 display | Both | 2 | ✅ Done |
| T2 | neuromorphic_dvs.py v1 — basic DVS, 3-panel display | Both | 3 | ✅ Done |
| T3 | Add polarity separation (ON panel + OFF panel) | Both | 1 | ✅ Done |
| T4 | Add event rate counter (events/sec) | Both | 1 | ✅ Done |
| T5 | Add adaptive threshold with cooldown | Both | 2 | ✅ Done |
| T6 | Add rolling activity graph in stats panel | Both | 1 | ✅ Done |
| T7 | Assemble 2×3 grid layout (v2) | Both | 1 | ✅ Done |
| T8 | Motion bounding boxes around event clusters (v3) | Both | 2 | 🔄 In progress |
| T9 | Testing, documentation, GitHub push | Both | 2 | ✅ Done |

### 10.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| DVS algorithm | Both | Both |
| Display / panels | Both | Both |
| Metrics + graph | Both | Both |
| Testing on Pi | Both | Both |
| Documentation | Both | Both |

---

## 11. Hour Milestones

### 11.1 8-Hour Plan

**Bi-Hour 1 — Plan and De-risk**
- ✅ Chose neuromorphic DVS as concept
- ✅ Confirmed OpenCV available on Pi via apt
- ✅ Confirmed test video and image available on Pi
- ✅ edge_basic.py working — Sobel, Canny, Laplacian displaying correctly

**Bi-Hour 2 — Build Core DVS**
- ✅ Frame differencing working
- ✅ ON/OFF event masks generating correctly
- ✅ Sparse Canny events (bitwise AND with active mask) working
- ✅ Basic 3-panel display running on Pi

**Bi-Hour 3 — Add Metrics and Features**
- ✅ Polarity panels (ON + OFF separate)
- ✅ Event rate counter (e/s)
- ✅ Adaptive threshold with cooldown timer
- ✅ Rolling activity graph in stats panel

**Bi-Hour 4 — Integrate and Refine**
- ✅ 2×3 grid layout assembled cleanly
- ✅ All keyboard controls working (Q, +, -, A, S)
- ✅ Tested on Pi — stable FPS, correct visuals
- ✅ Code pushed to GitHub

---

## 12. Update Log

| Day | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Day 1 | Build edge_basic.py and basic DVS | Both done and working on Pi | Added GaussianBlur before differencing — reduces noise significantly | Add polarity panels and event rate |
| Day 2 | Add polarity, event rate, adaptive threshold | All three added and working | Adaptive threshold needed cooldown timer — without it threshold oscillated rapidly | Assemble full 2×3 grid layout |
| Day 3 | Full 2×3 layout, stats panel, activity graph | Done — all 6 panels running cleanly | Activity graph Y-axis capped at 30% — uncapped it was unreadable on noisy scenes | Add bounding boxes around motion clusters |
| Day 4 | Bounding boxes (v3), final testing, documentation | Bounding box plan designed, implementation in progress | — | Complete bounding boxes, final push to GitHub |

---

## 13. Risks and Unknowns

### 13.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| Pi too slow to process 6 panels at real-time FPS | Performance | Medium | High | Resize all panels to 320×240; use NumPy array ops not loops | Both |
| Frame differencing too noisy on compressed video | Algorithm | High | Medium | Apply Gaussian blur before differencing; adjustable threshold via keyboard | Both |
| Adaptive threshold oscillates (hunts up and down) | Algorithm | Medium | Medium | Added cooldown timer (10 frames) between adjustments | Both |
| test.mp4 ends and script crashes | Software | High | Low | Added loop-back: resets to frame 0 on end of file | Both |

### 13.2 Biggest Unknown Right Now
Whether motion bounding boxes (v3) can be drawn accurately on the resized 320×240 panel while contours are detected on the original full-resolution active mask — coordinate scaling between the two must be handled correctly.

---

## 14. Testing

### 14.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| Sobel / Canny / Laplacian output | Run edge_basic.py on test.jpg, visually inspect each panel | All three detectors show correct edge maps, no blank panels |
| Frame differencing — ON/OFF masks | Run DVS on test.mp4, observe green/red events | Moving regions produce events; static background stays black |
| Sparse events | Check white pixels only appear where active mask AND Canny overlap | White edges visible only on moving objects |
| Activity % accuracy | Check displayed % against visual estimate of active area | Roughly matches proportion of screen showing events |
| Event rate counter | Watch e/s as scene changes | e/s rises on busy frames, drops on still frames |
| Adaptive threshold | Press A, watch threshold auto-adjust over 30–60 seconds | Threshold rises if activity > 15%, falls if < 4% |
| Keyboard controls | Press each key during live run | All keys respond correctly with no lag |
| Video loop | Let video run to end | Script loops to frame 0, no crash |
| Screenshot save | Press S | File saved to /home/exam/dvs_<timestamp>.png |

### 14.2 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| During dev | Raw frame diff very noisy — too many false events | Algorithm | Added GaussianBlur (3×3) before differencing | Noise significantly reduced | Keep blur in pipeline |
| During dev | Adaptive threshold oscillating rapidly | Algorithm | Added 10-frame cooldown between adjustments | Threshold now adjusts smoothly | Monitor on different video types |
| During dev | Activity graph Y-axis too large — flat line on normal scenes | Display | Capped Y-axis at 30% activity | Graph now shows meaningful variation | — |
| During dev | Video ending caused read_frame() to return None and crash | Software | Added loop-back: cap.set(CAP_PROP_POS_FRAMES, 0) on end | Video loops cleanly | — |
| During dev | Stats panel text overlapping graph at bottom | Display | Moved graph to bottom 60px, text to top section | No overlap | — |

### 14.3 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| Lab instructor | Watched DVS run, pressed +/- keys | Wasn't sure what the black background meant | Event map visual — found it striking and clear | Added label clarifying black = inactive background |
| Classmate | Tried all keyboard controls | Didn't know A toggled adaptive mode | Liked watching threshold auto-adjust live | Added "Adaptive: ON/OFF" status indicator in stats panel |

---

## 15. Build Documentation

### 15.1 Fabrication Process
Not applicable — this is a software-only project. No physical fabrication was required. The Raspberry Pi, monitor, and keyboard were set up as a standard workstation. The test video and image files were downloaded and placed at `/home/exam/`. Both Python scripts were written and tested directly on the Pi.

---

## 16. Build Screenshots

### MicroBlaze IP Block (Vivado Block Design)
![MicroBlaze IP Block](microblaze_ip_block.jpeg)

### Input — Cars Video Frame
![Input Cars Image](input_cars.jpeg)

### Output — Edge Detection on Cars
![Output Cars Edge Detection](output_cars.jpeg)

### edge_basic.py — 2×2 panel output
![edge_basic output](edge1.jpeg)

### neuromorphic_dvs.py — 6 panel grid
![DVS 6 panel output](edge2.jpeg)

### Additional Output
![Additional output](image1.jpeg)

---

## 17. Final Outcome

### 17.1 Final Description
Two fully working Python scripts running on Raspberry Pi:

**`edge_basic.py`** — loads `test.jpg`, applies Gaussian blur, runs Sobel Magnitude, Canny, and Laplacian edge detection. Displays all four panels in a 2×2 tiled OpenCV window. Press any key to close.

**`neuromorphic_dvs.py` (v2)** — reads `test.mp4` in a loop, simulates a Dynamic Vision Sensor using frame differencing. Displays a 2×3 grid of six panels: Original, Event Map (ON=green, OFF=red, confirmed edge=white), Active Mask, ON Events panel, OFF Events panel, and a Stats panel showing FPS, threshold, activity %, saved compute %, event rate (e/s), adaptive mode status, and a rolling 60-frame activity graph. Keyboard controls: Q to quit, +/- for threshold, A for adaptive, S to screenshot.

### 17.2 What Works Well
- Frame differencing accurately isolates only moving/changing pixels
- Sparse Canny correctly restricts edge detection to active regions — clearly demonstrates the compute saving
- ON/OFF polarity panels give clean independent views of brightening vs darkening
- Adaptive threshold self-tunes stably without oscillation
- Rolling activity graph makes scene busyness immediately readable over time
- All keyboard controls are instant and reliable
- Video loops seamlessly — no crash on end of file
- Runs at stable FPS on Raspberry Pi

### 17.3 What Still Needs Improvement
- Motion bounding boxes (v3) — planned, not yet complete
- Per-region activity heatmap overlay — not yet built
- Currently uses a test video file — would be more powerful with a live camera
- Canny low/high thresholds not yet adjustable by keyboard

### 17.4 What Changed From the Original Plan
The original plan was a simple 3-panel DVS display. Through iterative development it grew into a 6-panel dashboard with polarity separation, event rate counter, adaptive threshold, and a live activity graph. The adaptive threshold originally had no cooldown and oscillated wildly — adding a 10-frame cooldown made it stable. The activity graph Y-axis was originally uncapped and showed as a flat line on normal scenes — capping at 30% made it readable.

---

## 18. Reflection

### 18.1 Team Reflection
**What we did well:** We built iteratively — each feature was working before the next was added. We tested on the actual Pi throughout rather than assuming it would work at the end. Every planned feature got built except bounding boxes which are still in progress.

**What slowed us down:** Getting the adaptive threshold stable took longer than expected. Assembling the 2×3 panel grid required careful coordinate arithmetic — labels had to be offset correctly for each panel position.

**Time and task management:** Good. Working feature by feature with constant live testing kept us on track.

### 18.2 Technical Reflection
**Coding:** NumPy array operations (e.g. `diff > threshold` returning a boolean mask) are far faster than looping pixel by pixel — essential for real-time performance on the Pi.

**Computer Vision:** Frame differencing is simple but powerful. Gaussian blur before differencing is essential — without it, JPEG compression artifacts and sensor noise cause false events everywhere. The bitwise AND between Canny and active_mask is the key insight of the whole project — it's what makes processing sparse.

**Raspberry Pi:** OpenCV installed via apt (`python3-opencv`) worked immediately without compilation. The Pi handles 20–30 FPS comfortably on 320×240 panels.

**Integration:** The hardest part was the stats panel — combining text metrics, adaptive state indicator, and a rendered line graph into one 320×240 panel without elements overlapping.

### 18.3 Design Reflection
**Clarity:** The colour coding (green ON, red OFF, white edges, black background) makes the event map immediately readable without any explanation. First-time viewers understand what they're looking at within seconds.

**Delight:** Watching the black background stay black while only moving objects fire events is genuinely surprising to people who haven't seen neuromorphic vision before. It makes the concept tangible instantly.

**Iteration:** The system went through three significant visual layouts before settling on the 2×3 grid. Earlier versions were harder to read because panels were too small or labels overlapped data.

### 18.4 If We Had One More Hour
Complete the motion bounding boxes feature — drawing coloured rectangles around clusters of events on the Original panel, colour-coded by event density. This would turn the DVS from a visualisation tool into a basic motion detection system, which is the most direct real-world application of neuromorphic vision.

---

## 19. How to Run

```bash
# Basic edge detection (static image)
python3 ~/edge_basic.py

# DVS simulation (video, loops automatically)
python3 ~/neuromorphic_dvs.py

# Keyboard controls during DVS:
#   Q or ESC  — quit
#   + or =    — raise threshold (fewer events)
#   -         — lower threshold (more events)
#   A         — toggle adaptive threshold ON/OFF
#   S         — save screenshot to /home/exam/dvs_<timestamp>.png

# Kill a running script
# Ctrl+Z then:
kill %1
```

---

## 20. System Info

| Item | Value |
|---|---|
| Device | Raspberry Pi |
| Username | exam |
| Home directory | /home/exam |
| OS | Raspberry Pi OS |
| Python | Python 3.x |
| OpenCV | python3-opencv (installed via apt) |
| Test video | /home/exam/test.mp4 (MP4 v2) |
| Test image | /home/exam/test.jpg (JPEG) |
| Display | Connected monitor (not headless) |
| Camera | Not required — using video file |

---

## 21. Final Submission Checklist

- ✅ Team details are complete
- ✅ Project description is complete
- ✅ Inspiration sources are included
- ✅ System architecture / flowchart added
- ✅ Display layout diagram added
- ✅ BOM is complete
- ✅ Budget summary is complete
- ✅ Software planning is documented
- ✅ Code flowchart is added
- ✅ Task breakdown is complete
- ✅ Update logs are complete
- ✅ Risk register is complete
- ✅ Testing plan is complete
- ✅ Testing and debugging log is complete
- ✅ Playtesting notes are included
- ⬜ Screenshots are uploaded *(add images)*
- ✅ Final reflection is written
- ✅ How to run instructions included
