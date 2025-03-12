# 🛍️ Virtual Dressing Room – AI-Powered Real-Time Clothing Try-On  

This project is an **AI-powered virtual dressing room** that allows users to try on clothes in real time using a live camera feed. Built using **Django** and **React**, the platform leverages **OpenCV** and **Mediapipe** for real-time garment overlay, giving users an interactive virtual try-on experience.

---

## 🚀 Features
✅ Real-time garment overlay on live video feed  
✅ Accurate garment fitting with shoulder width adjustment  
✅ Hand gesture-based garment selection  
✅ Horizontal gallery for garment selection  
✅ Scalable architecture using Django + React  
✅ Fast communication using WebSockets  

---

## 📸 How It Works
1. **Frontend (React):**  
   - Captures video frames from the user's camera using **Mediapipe**.  
   - Sends frames to the backend via **WebSockets**.  

2. **Backend (Django):**  
   - Processes incoming frames using **OpenCV**.  
   - Overlays the selected garment onto the video frame.  
   - Adjusts garment size based on dynamic `tshirt_shoulder_width` for a perfect fit.  

3. **Garment Selection:**  
   - Left and right windows display garment previews.  
   - Middle window shows the live try-on with the overlay.  
   - Bottom row gallery allows users to scroll and select garments.  
   - Hand gesture detection allows garment selection.  

---

## 🏗️ Tech Stack
| Technology | Purpose |
|------------|---------|
| **Django** | Backend framework |
| **React (Vite)** | Frontend framework |
| **OpenCV** | Computer vision for garment overlay |
| **Mediapipe** | Hand gesture recognition |
| **WebSockets** | Real-time communication |
| **PostgreSQL** | Database for storing garment images (in `bytea` format) |

---

## 🎯 Installation and Setup
### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/virtual-dressing-room.git
cd virtual-dressing-room
