import cv2
import matplotlib.pyplot as plt
import pandas as pd

video_path = "worm_video.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    raise IOError("Error: Cannot open video file!")

positions = []  # store (frame_index, x, y)
frame_index = 0

# Mouse callback
def click_event(event, x, y, flags, param):
    global frame_index
    if event == cv2.EVENT_LBUTTONDOWN:
        positions.append((frame_index, x, y))
        print(f"✅ Frame {frame_index}: Clicked at ({x}, {y})")

cv2.namedWindow("Annotate Worm Head")
cv2.setMouseCallback("Annotate Worm Head", click_event)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Annotate Worm Head", frame)
    key = cv2.waitKey(0) & 0xFF  # waits for key press

    if key == 27:  # ESC to quit early
        break

    frame_index += 1

cap.release()
cv2.destroyAllWindows()

# --- Save clicks to CSV ---
if positions:
    df = pd.DataFrame(positions, columns=["Frame", "X", "Y"])
    df.to_csv("worm_head_positions.csv", index=False)
    print("✅ Saved head positions to worm_head_positions.csv")

    # --- Plot trajectory ---
    xs, ys = zip(*[(x, y) for _, x, y in positions])
    plt.figure(figsize=(6,6))

    # Plot full trajectory
    plt.plot(xs, ys, 'ro-', markersize=3, label="Trajectory")

    # Mark start point (first click)
    plt.scatter(xs[0], ys[0], color="green", s=100, marker="o", label="Start")

    # Mark end point (last click)
    plt.scatter(xs[-1], ys[-1], color="blue", s=100, marker="o", label="End")

    plt.gca().invert_yaxis()
    plt.title("🐛 Worm Head Trajectory (Manual Annotation)")
    plt.xlabel("X (pixels)")
    plt.ylabel("Y (pixels)")
    plt.legend()
    plt.show()
