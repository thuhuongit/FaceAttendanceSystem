import os
import django

# ==== [1] Khởi tạo Django sớm ====
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FaceAttendanceSystem.settings")
django.setup()

# ==== [2] Import tiếp các thư viện sau ====
import face_recognition
import cv2
import pickle
from datetime import datetime

# Import model Django (phải làm sau khi setup Django)
from attendance.models import AttendanceRecord
from employees.models import Employee

ENCODINGS_PATH = "face_recognition/encodings.pkl"

# Load dữ liệu khuôn mặt đã mã hóa
with open(ENCODINGS_PATH, "rb") as f:
    data = pickle.load(f)

# Khởi động webcam (nếu không có webcam thì dùng ảnh/video)
video = cv2.VideoCapture(0)
recognized_names = set()

print("[INFO] Đang bật webcam để nhận diện...")

while True:
    ret, frame = video.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, boxes)

    for encoding, box in zip(encodings, boxes):
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "Unknown"

        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1

            name = max(counts, key=counts.get)

            if name not in recognized_names:
                recognized_names.add(name)
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[+] {name} điểm danh lúc {now}")

                # ==== GHI ĐIỂM DANH VÀO DATABASE ====
                try:
                    employee = Employee.objects.get(name=name)
                    AttendanceRecord.objects.create(employee=employee)
                    print(f"[✓] Đã ghi điểm danh DB cho {name}")
                except Employee.DoesNotExist:
                    print(f"[!] Không tìm thấy nhân viên trong DB: {name}")

        # Vẽ khung
        top, right, bottom, left = box
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
