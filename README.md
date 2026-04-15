🐛 Worm Tracker – Manual Annotation Tool

Because sometimes… the best AI is still your own eyes + clicks 👀✨

Track the movement of a worm’s head frame-by-frame and visualize its journey like a boss 📈

🎯 What This Does

This script lets you:

🎥 Load a video (worm_video.mp4)
🖱️ Click on the worm’s head in each frame
📍 Record coordinates (X, Y) for every frame
💾 Save data into a CSV file
📊 Generate a beautiful trajectory plot with:
Direction arrows ➡️
Step numbers 🔢
Start 🟢 and End 🔵 markers

⚙️ How It Works
The video opens frame by frame
You click on the worm’s head
Press any key to move to the next frame
Repeat until done (or press ESC to exit early)
Boom 💥 — data + visualization generated

🧠 Output Files
📄 worm_head_positions.csv
Frame	X	Y
0	123	456
1	130	460
📊 Trajectory Plot
Red line → movement path
Arrows → direction
Numbers → click order
Green dot → start
Blue dot → end

🚀 How to Run
pip install opencv-python matplotlib pandas
python your_script_name.py

🎮 Controls
Action	Key
Click worm head	Left Mouse Click 🖱️
Next frame	Any key ⌨️
Exit early	ESC ❌

😎 Why This is Cool
No complex ML model needed 🤖❌
Full control over tracking ✔️
Perfect for:
Biology experiments 🧬
Motion analysis 🏃
Data visualization practice 📊
💡 Future Upgrades (if you feel like leveling up)
🔁 Auto-tracking using OpenCV
🎯 Heatmaps of movement
⏱️ Speed & acceleration analysis
🧠 Train a model using your manual data

⚠️ Pro Tip

Be consistent with your clicks — accuracy = better trajectory 📈

🐛 Final Thought

“Even a worm leaves a path… you just made it visible.”
