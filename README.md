🏠🎥 Smart Motion Tracker for Home/Office (YOLO + Tracking)

A real-time motion tracking system that detects people, assigns unique IDs, and draws their movement paths using YOLOv8 + Object Tracking.
This project is useful for home/office monitoring, visitor movement analysis, and basic security surveillance.

🚀 Features

✔ Real-time person detection using YOLO
✔ Unique ID tracking for each individual
✔ Motion path drawing (tracks movement over time)
✔ Works on webcam, CCTV IP cameras, or video files
✔ Lightweight and easy to customize

📌 Tech Used
Technology	Purpose
Python	Main programming language
OpenCV	Video handling and drawing
YOLOv8	Object detection
NumPy	Data management
Deque	Storing motion paths
📸 How It Works

Detects a person using YOLO.

Assigns an ID to each detected person.

Saves their movement points.

Draws a colored path showing where they move.

🛠 Installation
📍 1. Clone the repository
git clone https://github.com/farwa-shaikh/smart-motion-tracker.git
cd smart-motion-tracker

📍 2. Install dependencies
pip install ultralytics opencv-python numpy

📍 3. Download YOLOv8 Model

It downloads automatically on first run.
Or download manually from Ultralytics.

▶️ Run the Project
Run motion tracker:
python main.py

Ensure tracker file is present:
tracker.py

📂 Project Structure
Smart-Motion-Tracker/
│── main.py          # Main camera + detection code
│── tracker.py       # Motion tracking class
│── requirements.txt # Libraries
│── README.md        # Project description

🧠 Future Improvements

🔐 Add entry–exit counting
📍 Create heatmaps of motion
🔊 Sound alarm on unknown person
📱 Send alerts to a mobile app

👩‍💻 Developer

👤 Farwa Shaikh
📎 Electronics Engineer | AI & Computer Vision Enthusiast
🤖 Passionate about Edge AI, Robotics & Smart Security Systems.

⭐ Contribute / Support

Feel free to fork, improve, and star ⭐ this repository if you like it!
