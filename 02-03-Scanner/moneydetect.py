import cv2
import numpy as np
from collections import Counter
import argparse
import imutils

# Definisikan batas warna untuk setiap denominasi uang rupiah
boundaries = {
    '100.000': ([0, 100, 100], [10, 255, 255]),  # Merah
    '50.000': ([90, 100, 100], [130, 255, 255]),  # Biru
    '20.000': ([35, 100, 100], [85, 255, 255]),  # Hijau
    '10.000': ([125, 50, 50], [160, 255, 255])  # Ungu
}

def get_dominant_color(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    color_count = Counter()
    
    for key, (lower, upper) in boundaries.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        
        mask = cv2.inRange(hsv_image, lower, upper)
        
        if cv2.countNonZero(mask) > 0:
            color_count[key] = cv2.countNonZero(mask)
    
    if color_count:
        dominant_color = color_count.most_common(1)[0][0]
    else:
        dominant_color = None
    
    return dominant_color

def detect_objects(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 75, 200)

    contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    detected_objects = []
    hierarchy = hierarchy[0]

    for i, contour in enumerate(contours):
        if cv2.contourArea(contour) > 100:
            if hierarchy[i][3] == -1:  # Hanya kontur luar yang tidak berada di dalam kontur lain
                x, y, w, h = cv2.boundingRect(contour)
                crop_img = image[y:y+h, x:x+w]
                detected_objects.append((x, y, w, h, crop_img))
    
    return detected_objects

def display_image_with_counts(image, contours_list):
    uang_count = Counter()
    
    for (x, y, w, h, crop_img) in contours_list:
        dominant_color = get_dominant_color(crop_img)
        if dominant_color:
            uang_type = dominant_color
            color = (0, 255, 0)  # Hijau untuk kotak pembatas
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            cv2.putText(image, uang_type, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
            uang_count[uang_type] += 1

    # Menghitung total jumlah uang
    total_amount = sum([int(uang.replace('.', '').replace('000', '')) * count for uang, count in uang_count.items()])
    total_amount_text = f"Total uang: Rp {total_amount:,}.000"
    
    # Menampilkan jumlah uang per denominasi
    total_count_text = ", ".join([f"{uang}: {count}" for uang, count in uang_count.items()])
    
    y0, dy = 20, 20
    for i, line in enumerate(total_count_text.split(", ")):
        y = y0 + i * dy
        cv2.putText(image, line, (10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    
    # Menambahkan teks total jumlah uang
    y = y0 + len(total_count_text.split(", ")) * dy
    cv2.putText(image, total_amount_text, (10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow("Uang Rupiah Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Argumen dari command line
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image f ile")
args = vars(ap.parse_args())

# Proses gambar dari argumen yang diberikan
image_path = args["image"]
image = cv2.imread(image_path)

if image is not None:
    contours_list = detect_objects(image)
    display_image_with_counts(image, contours_list)
else:
    print(f"Could not read image at {image_path}")
