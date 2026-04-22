import cv2
import mediapipe as mp
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as mp_draw
import pygame

pygame.mixer.init()
try:
    pygame.mixer.music.load("kicau_mania.mp3")
except:
    print("Peringatan: File kicau_mania.mp3 tidak ditemukan!")

hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)
cat_video = cv2.VideoCapture("cat_dance.mp4")

show_second_window = False
is_playing = False

WIN_W, WIN_H = 600, 450

print("--- MODE KICAU MANIA + MUSIK AKTIF ---")

while True:
    success, img = cap.read()
    if not success: break
    img = cv2.flip(img, 1)
    img = cv2.resize(img, (WIN_W, WIN_H))

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
            x_pos = handLms.landmark[8].x 
            
            if x_pos < 0.3 and not show_second_window: 
                show_second_window = True
                if not is_playing:
                    pygame.mixer.music.play(-1)
                    is_playing = True
                    
            if x_pos > 0.7 and show_second_window: 
                show_second_window = False
                pygame.mixer.music.stop()
                is_playing = False

    cv2.imshow("Face Cam", img)
    cv2.moveWindow("Face Cam", 50, 150)

    if show_second_window:
        ret_cat, cat_frame = cat_video.read()
        if not ret_cat:
            cat_video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret_cat, cat_frame = cat_video.read()
        
        cat_frame = cv2.resize(cat_frame, (WIN_W, WIN_H))
        cv2.imshow("Kucing Joget", cat_frame)
        cv2.moveWindow("Kucing Joget", 50 + WIN_W + 10, 150)
    else:
        try:
            if cv2.getWindowProperty("Kucing Joget", cv2.WND_PROP_VISIBLE) >= 1:
                cv2.destroyWindow("Kucing Joget")
        except:
            pass

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cat_video.release()
cv2.destroyAllWindows()
pygame.mixer.music.stop()
