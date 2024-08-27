import cv2
import time
import os

################################################################
path = 'C:\\SMA_PRAXIS\\Harrcascade_Modul\\haarcascade_frontalface_alt.xml'  # PATH OF THE CASCADE
cameraNo = 0                       # CAMERA NUMBER
objectName = 'Orang'       # OBJECT NAME TO DISPLAY
frameWidth = 640                     # DISPLAY WIDTH
frameHeight = 480                  # DISPLAY HEIGHT
color = (255, 0, 255)
output_folder = 'C:\\SMA_PRAXIS\\03-02-HarrCascades\\hasilrekaman'  # Folder untuk menyimpan rekaman
slowmo_factor = 3  # Faktor untuk efek slow motion (semakin besar angkanya, semakin lambat)
#################################################################

# Buat folder jika belum ada
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cap = cv2.VideoCapture(cameraNo)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):
    pass

# CREATE TRACKBAR
cv2.namedWindow("Result")
cv2.resizeWindow("Result", frameWidth, frameHeight+100)
cv2.createTrackbar("Scale", "Result", 220, 1000, empty)
cv2.createTrackbar("Neig", "Result", 5, 50, empty)
cv2.createTrackbar("Min Area", "Result", 0, 100000, empty)
cv2.createTrackbar("Brightness", "Result", 195, 255, empty)

# LOAD THE CLASSIFIERS DOWNLOADED
cascade = cv2.CascadeClassifier(path)

# Variables for recording
recording = False
out = None

while True:
    # SET CAMERA BRIGHTNESS FROM TRACKBAR VALUE
    cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
    cap.set(10, cameraBrightness)
    # GET CAMERA IMAGE AND CONVERT TO GRAYSCALE
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # DETECT THE OBJECT USING THE CASCADE
    scaleVal = 1 + (cv2.getTrackbarPos("Scale", "Result") / 1000)
    neig = cv2.getTrackbarPos("Neig", "Result")
    objects = cascade.detectMultiScale(gray, scaleVal, neig)
    
    # Check if any objects are detected
    if len(objects) > 0:
        if not recording:
            # Start recording
            recording = True
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            video_name = os.path.join(output_folder, f"rekaman_{timestamp}.avi")
            out = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), 20, (frameWidth, frameHeight))
            print(f"Started recording: {video_name}")
        
        # Apply slow motion effect
        for _ in range(slowmo_factor):
            out.write(img)
        
        for (x, y, w, h) in objects:
            area = w * h
            minArea = cv2.getTrackbarPos("Min Area", "Result")
            if area > minArea:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                cv2.putText(img, objectName, (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
                roi_color = img[y:y + h, x:x + w]
    else:
        if recording:
            # Stop recording
            recording = False
            out.release()
            print("Stopped recording")
    
    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if job is finished
cap.release()
if recording:
    out.release()
cv2.destroyAllWindows()
