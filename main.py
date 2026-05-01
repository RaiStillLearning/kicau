import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import pygame
import os
import sys
import time
import numpy as np

# Dapatkan direktori tempat script ini berada
base_path = os.path.dirname(os.path.abspath(__file__))

# Setup Audio
pygame.mixer.init()
mp3_path = os.path.join(base_path, "assets", "kicau_mania.mp3")
if os.path.exists(mp3_path):
    pygame.mixer.music.load(mp3_path)
else:
    print(f"Peringatan: File {mp3_path} tidak ditemukan!")

# Setup MediaPipe Tasks
model_path = os.path.join(base_path, "assets", "hand_landmarker.task")
if not os.path.exists(model_path):
    print(f"❌ ERROR: File model {model_path} tidak ditemukan!")
    print("💡 Script ini membutuhkan model MediaPipe Tasks. Pastikan folder assets/ lengkap.")
    sys.exit(1)

base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)

print("⏳ Mencari kamera yang aktif...")
cap = None
for i in range(3):
    print(f"🔍 Mencoba membuka Kamera Index {i}...")
    temp_cap = cv2.VideoCapture(i, cv2.CAP_AVFOUNDATION)
    if not temp_cap.isOpened():
        temp_cap = cv2.VideoCapture(i) 

    if temp_cap.isOpened():
        valid_camera = False
        for f in range(10):
            success, img = temp_cap.read()
            if success and np.mean(img) > 5.0:
                valid_camera = True
                break
        if valid_camera:
            cap = temp_cap
            print(f"🎯 Kamera {i} terpilih sebagai input utama.")
            break
        temp_cap.release()

if cap is None:
    print("❌ ERROR: Tidak ada kamera yang bisa memberikan gambar!")
    sys.exit(1)

video_path = os.path.join(base_path, "assets", "cat_dance.mp4")
cat_video = cv2.VideoCapture(video_path)
cat_fps = cat_video.get(cv2.CAP_PROP_FPS) or 30.0

show_second_window = False
is_playing = False
history_x = []
last_swipe_time = 0
WIN_W, WIN_H = 600, 450
start_play_time = 0
frames_read = 0
last_cat_frame = None

print("--- MODE KICAU MANIA AKTIF ---")
print("✋ Ayunkan tangan ke KIRI untuk memulai!")

while True:
    success, img = cap.read()
    if not success: break

    img = cv2.flip(img, 1)
    img = cv2.resize(img, (WIN_W, WIN_H))
    
    # MediaPipe Tasks butuh format Image
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    detection_result = detector.detect(mp_image)

    if detection_result.hand_landmarks:
        # Kita ambil tangan pertama yang terdeteksi
        hand_landmarks = detection_result.hand_landmarks[0]
        
        # Landmark 9 adalah tengah telapak tangan
        x_pos = hand_landmarks[9].x
        history_x.append(x_pos)
        if len(history_x) > 10: history_x.pop(0)
        
        current_time = time.time()
        if current_time - last_swipe_time > 1.0:
            if len(history_x) >= 5:
                min_x, max_x = min(history_x), max(history_x)
                if (max_x - min_x) > 0.15 and not show_second_window:
                    if history_x[-1] < history_x[0]: # Swipe Kiri
                        show_second_window = True
                        pygame.mixer.music.play(0)
                        is_playing = True
                        cat_video.release()
                        cat_video = cv2.VideoCapture(video_path)
                        start_play_time = time.time()
                        frames_read = 0
                        last_cat_frame = None
                        last_swipe_time = current_time
                        history_x.clear()
        
        # Gambar titik tangan (Opsional: Kita gambar manual karena drawing_utils juga bagian dari solutions)
        for lm in hand_landmarks:
            px, py = int(lm.x * WIN_W), int(lm.y * WIN_H)
            cv2.circle(img, (px, py), 3, (0, 255, 0), -1)
    else:
        history_x.clear()

    cv2.imshow("Face Cam", img)
    cv2.moveWindow("Face Cam", 50, 150)

    if show_second_window:
        elapsed_time = time.time() - start_play_time
        desired_frames = int(elapsed_time * cat_fps)
        frames_to_read = desired_frames - frames_read
        
        video_finished = False
        for _ in range(max(0, frames_to_read)):
            ret_cat, cat_frame = cat_video.read()
            if not ret_cat:
                video_finished = True
                break
            last_cat_frame = cat_frame
            frames_read += 1
            
        if video_finished:
            show_second_window = False
            pygame.mixer.music.stop()
            is_playing = False
            try: cv2.destroyWindow("Kucing Joget")
            except: pass
        elif last_cat_frame is not None:
            display_frame = cv2.resize(last_cat_frame, (WIN_W, WIN_H))
            cv2.imshow("Kucing Joget", display_frame)
            cv2.moveWindow("Kucing Joget", 50 + WIN_W + 10, 150)
    else:
        try:
            if cv2.getWindowProperty("Kucing Joget", cv2.WND_PROP_VISIBLE) >= 1:
                cv2.destroyWindow("Kucing Joget")
        except: pass

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cat_video.release()
cv2.destroyAllWindows()
pygame.mixer.music.stop()
