# 🐛 Worm Head Trajectory Annotator

A manual annotation tool for tracking worm head positions frame-by-frame in a video, with trajectory visualization and CSV export.

---

## Overview

This script lets you click on a worm's head in each video frame to record its position. Once all frames are annotated, it saves the coordinates to a CSV file and plots the full trajectory with directional arrows.

---

## Requirements

Install the dependencies with:

```bash
pip install opencv-python matplotlib pandas
```

| Package | Purpose |
|---|---|
| `opencv-python` | Video reading and frame display |
| `matplotlib` | Trajectory plotting |
| `pandas` | CSV export |

---

## Usage

1. **Place your video** in the same directory as the script and name it `worm_video.mp4` (or update the `video_path` variable).

2. **Run the script:**

```bash
python worm_annotator.py
```

3. **Annotate each frame:**
   - A window titled **"Annotate Worm Head"** will open showing the first frame.
   - **Left-click** on the worm's head to record its position.
   - Press **any key** to advance to the next frame.
   - Press **ESC** to stop early and save progress.

4. After annotation, the script will:
   - Save positions to `worm_head_positions.csv`
   - Display a trajectory plot

---

## Output

### `worm_head_positions.csv`

| Column | Description |
|---|---|
| `Frame` | Frame index (0-based) |
| `X` | Horizontal pixel coordinate of the click |
| `Y` | Vertical pixel coordinate of the click |

### Trajectory Plot

- 🔴 **Red dots & lines** — full trajectory path
- 🟢 **Green dot** — start position (first click)
- 🔵 **Blue dot** — end position (last click)
- **Arrows** — direction of movement between frames
- **Numbers** — click order label at each point

---

## Controls

| Input | Action |
|---|---|
| Left Click | Record worm head position |
| Any Key | Advance to next frame |
| ESC | Stop annotation and save |

---

## Notes

- Each frame waits indefinitely (`cv2.waitKey(0)`) until a key is pressed — you don't need to click and press a key simultaneously; just click first, then press any key.
- If you press a key **without clicking**, that frame will have no recorded position.
- The Y-axis is inverted in the plot to match image coordinate conventions (origin at top-left).
- Designed for single-worm videos; for multi-worm tracking, consider extending with multi-point annotation.
