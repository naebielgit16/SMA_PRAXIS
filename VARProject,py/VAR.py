from collections import deque
from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time
import os

# Konfigurasi video dan buffer
buffer_size = 32
output_folder = "C:\\SMA_PRAXIS\\03-00-cobadulu\\RekamanGoal"

# Batasan warna "red" dalam ruang warna HSV
redLower1 = (0, 120, 70)
redUpper1 = (10, 255, 255)
redLower2 = (170, 120, 70)
redUpper2 = (180, 255, 255)

# Inisialisasi variabel
pts = deque(maxlen=buffer_size)
counter = 0
(dX, dY) = (0, 0)
direction = ""
score = 0
goal_counted = False
slowmo_factor = 3
recording = False
out = None
record_count = 1
goal_time = None
start_time = time.time()  # Waktu mulai dari 0

# Mulai video stream dari webcam
vs = VideoStream(src=0).start()
time.sleep(2.0)

# Buat folder output jika belum ada
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop utama
while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask1 = cv2.inRange(hsv, redLower1, redUpper1)
    mask2 = cv2.inRange(hsv, redLower2, redUpper2)
    mask = cv2.add(mask1, mask2)

    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    height, width = frame.shape[:2]
    mid_x = width // 5
    line_y = height - 50  # Garis horizontal sebagai indikator posisi bola

    # Gambar garis horizontal untuk menandai posisi bola
    cv2.line(frame, (0, line_y), (width, line_y), (0, 255, 160), 2)
    
    # Menampilkan waktu real-time di window
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    current_time_text = f"Time: {minutes:02}:{seconds:02}"
    cv2.putText(frame, current_time_text, (10, height - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            pts.appendleft(center)

            # Memulai rekaman jika bola melewati garis
            if int(x + radius) < mid_x and not goal_counted:
                if not recording:
                    video_name = os.path.join(output_folder, f"rekaman_{record_count}.avi")
                    out = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), 20, (width, height))
                    print(f"Started recording: {video_name}")
                    recording = True
                    record_count += 1

            if int(x + radius) >= mid_x and recording:
                # Mencatat waktu goal
                goal_time = elapsed_time
                cv2.putText(frame, f"Goal: {goal_time:.2f} sec", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 3)
                cv2.putText(frame, f"Menit: {int(goal_time // 60)}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 3)
                cv2.putText(frame, f"Detik: {int(goal_time % 60)}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 3)
                score += 1
                goal_counted = True
                print(f"Goal at {goal_time:.2f} sec")

            elif int(x + radius) >= mid_x:
                goal_counted = False

            # Tuliskan frame ke video dengan efek slow motion
            if recording:
                for _ in range(slowmo_factor):
                    out.write(frame)

    else:
        if recording:
            recording = False
            out.release()
            print("Stopped recording")

    # Menampilkan skor dan waktu goal terakhir
    cv2.putText(frame, f"Score: {score}", (width - 150, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
    if goal_time is not None:
        cv2.putText(frame, f"Goal Time: {goal_time:.2f} sec", (width - 250, height - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    counter += 1

    # Jika 'q' ditekan, berhenti
    if key == ord("q"):
        break

    # Jeda 5 detik setelah 'goal'
    if goal_counted:
        time.sleep(5)
        goal_counted = False  # Reset flag setelah jeda

# Memberhentikan stream dan menutup semua jendela
vs.stop()
if out is not None:
    out.release()
cv2.destroyAllWindows()
