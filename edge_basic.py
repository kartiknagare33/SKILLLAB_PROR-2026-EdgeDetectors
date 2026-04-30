import cv2
import numpy as np

def sobel_magnitude(gray):
    sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    mag = np.sqrt(sx**2 + sy**2)
    return np.clip(mag / mag.max() * 255, 0, 255).astype(np.uint8) if mag.max() > 0 else mag.astype(np.uint8)

def canny_edges(gray, low=50, high=150):
    return cv2.Canny(gray, low, high)

def laplacian_edges(gray):
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    lap_abs = np.abs(lap)
    return np.clip(lap_abs / lap_abs.max() * 255, 0, 255).astype(np.uint8) if lap_abs.max() > 0 else lap_abs.astype(np.uint8)

def label(img, text):
    out = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) if len(img.shape) == 2 else img.copy()
    cv2.putText(out, text, (8, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 180), 2, cv2.LINE_AA)
    return out

def tile_2x2(tl, tr, bl, br):
    top = np.hstack([tl, tr])
    bot = np.hstack([bl, br])
    return np.vstack([top, bot])

def main():
    frame = cv2.imread("/home/exam/test.jpg")
    if frame is None:
        print("Image not found")
        return

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    t1 = label(frame, "Original")
    t2 = label(sobel_magnitude(gray), "Sobel Magnitude")
    t3 = label(canny_edges(gray), "Canny")
    t4 = label(laplacian_edges(gray), "Laplacian")

    display = tile_2x2(t1, t2, t3, t4)
    cv2.imshow("Basic Edge Detection", display)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
