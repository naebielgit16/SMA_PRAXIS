import cv2
import face_recognition
import numpy as np
import datetime
import json

# Fungsi untuk memulai jam
def start_clock():
    return datetime.datetime.now()

# Fungsi untuk memulai video stream
def start_video_stream():
    return cv2.VideoCapture(0)

# Fungsi untuk mendeteksi wajah
def detect_face(frame):
    face_locations = face_recognition.face_locations(frame)
    if len(face_locations) > 0:
        return True, face_locations[0]
    return False, None

# Fungsi untuk mengenkode wajah dan menentukan kecocokan terbaik
def encode_face_and_find_match(frame, face_location, known_face_encodings, known_face_names):
    face_encoding = face_recognition.face_encodings(frame, [face_location])[0]
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        return known_face_names[best_match_index]
    return None

# Fungsi untuk menyimpan data kehadiran
def save_attendance(name, role, face_expression, time, is_first_time):
    attendance_data = {
        "name": name,
        "role": role,
        "face_expression": face_expression,
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "type": "attendance" if is_first_time else "go_home"
    }
    with open("attendance.json", "a") as f:
        json.dump(attendance_data, f)
        f.write("\n")

# Fungsi untuk menampilkan jendela registrasi
def show_registration_window():
    # Implementasi GUI untuk registrasi akan ditambahkan di sini
    name = input("Enter name: ")
    role = input("Enter role: ")
    return name, role

# Fungsi utama
def main():
    known_face_encodings = []
    known_face_names = []
    
    video_capture = start_video_stream()
    
    while True:
        current_time = start_clock()
        
        ret, frame = video_capture.read()
        
        face_detected, face_location = detect_face(frame)
        
        if face_detected:
            name = encode_face_and_find_match(frame, face_location, known_face_encodings, known_face_names)
            
            if name:
                # Implementasi deteksi ekspresi wajah akan ditambahkan di sini
                face_expression = "neutral"
                
                # Cek apakah ini kunjungan pertama hari ini
                is_first_time = True  # Logika untuk mengecek kunjungan pertama akan ditambahkan
                
                save_attendance(name, "Unknown", face_expression, current_time, is_first_time)
            else:
                name, role = show_registration_window()
                face_encoding = face_recognition.face_encodings(frame, [face_location])[0]
                known_face_encodings.append(face_encoding)
                known_face_names.append(name)
                save_attendance(name, role, "neutral", current_time, True)
        
        # Tampilkan frame dengan informasi
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()