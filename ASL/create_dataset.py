import os
import pickle
import mediapipe as mp
import cv2

# Suppress TensorFlow Lite logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Directory containing the dataset
DATA_DIR = './data'

# Check if the dataset directory exists
if not os.path.exists(DATA_DIR):
    raise FileNotFoundError(f"Data directory '{DATA_DIR}' does not exist.")

# Initialize data and labels
data = []
labels = []

# Process each subdirectory in the data folder
for dir_ in os.listdir(DATA_DIR):
    dir_path = os.path.join(DATA_DIR, dir_)
    if not os.path.isdir(dir_path):
        continue  # Skip non-directory files

    print(f"Processing folder: {dir_}")

    # Process each image in the subdirectory
    for img_path in os.listdir(dir_path):
        img_file = os.path.join(dir_path, img_path)
        if not img_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(f"Skipping non-image file: {img_file}")
            continue

        # Read the image and convert it to RGB
        img = cv2.imread(img_file)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Detect hand landmarks
        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                data_aux = []
                x_ = []
                y_ = []

                # Extract coordinates
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    x_.append(x)
                    y_.append(y)

                # Normalize coordinates
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

                # Append data and label
                data.append(data_aux)
                labels.append(dir_)
        else:
            print(f"No hand landmarks detected in {img_file}. Skipping...")

# Save processed data to a pickle file
with open('data.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)

print("Dataset processing completed. Data saved to 'data.pickle'.")
