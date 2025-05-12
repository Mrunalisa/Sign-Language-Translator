import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Create the missing folders
missing_classes = [40, 41]
dataset_size = 100

cap = cv2.VideoCapture(0)

for class_name in missing_classes:
    class_path = os.path.join(DATA_DIR, class_name)
    if not os.path.exists(class_path):
        os.makedirs(class_path)

    print(f'Collecting data for class {class_name}')

    # Initial ready screen
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" to start! :)', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Collect data for the class
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame. Exiting...")
            break

        cv2.imshow('frame', frame)
        cv2.imwrite(os.path.join(class_path, f'{counter}.jpg'), frame)

        counter += 1
        if cv2.waitKey(25) & 0xFF == ord('q'):  # Press Q to stop early
            print(f"Stopped early at {counter} images.")
            break

cap.release()
cv2.destroyAllWindows()

print("Data collection completed for missing folders.")
