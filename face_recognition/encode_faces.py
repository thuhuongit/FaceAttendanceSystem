import face_recognition
import os
import pickle
import cv2

dataset_path = "face_data"
encoding_file = "face_recognition/encodings.pkl"

known_encodings = []
known_names = []

print("[INFO] Đang mã hóa khuôn mặt...")

for person_name in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person_name)
    if not os.path.isdir(person_folder):
        continue

    for img_name in os.listdir(person_folder):
        img_path = os.path.join(person_folder, img_name)
        image = cv2.imread(img_path)

        if image is None:
            print(f"[WARNING] Không đọc được ảnh: {img_path}")
            continue

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(person_name)

data = {"encodings": known_encodings, "names": known_names}

with open(encoding_file, "wb") as f:
    pickle.dump(data, f)

print(f"[DONE] Đã lưu mã hóa vào: {encoding_file}")
