import pickle
import cv2
import mediapipe as mp
import numpy as np

# Load trained model
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']
expected_features = model_dict['input_shape']

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Label dictionary (adjust as per your dataset)
labels_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'F', 5: 'G', 6: 'H', 7: 'I', 8: 'J', 9: 'J', 10: 'J', 11: 'K', 12: 'L',
               13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W',
               24: 'X', 25: 'Y', 26: 'Z', 27: '0', 28: '1', 29: '2', 30: '3', 31: '4', 32: '5', 33: '6', 34: '7',
               35: '8', 36: '9', 37: 'Hello', 38: 'Thank You / Thanks', 39: 'Thanks a Lot', 40: 'E', 41: 'I Love You'}

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    H, W, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)

    data_aux = []
    x_ = []
    y_ = []

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

            for landmark in hand_landmarks.landmark:
                x_.append(landmark.x)
                y_.append(landmark.y)

            x_min, y_min = min(x_), min(y_)
            for landmark in hand_landmarks.landmark:
                data_aux.append(landmark.x - x_min)
                data_aux.append(landmark.y - y_min)

            # Ensure feature count matches the model's expected input
            if len(data_aux) != expected_features:
                #print(f"Feature mismatch: Expected {expected_features}, but got {len(data_aux)}")
                continue

            # Predict character
            prediction = model.predict([np.asarray(data_aux)])
            predicted_character = labels_dict[int(prediction[0])]

            # Bounding box
            x1, y1 = int(x_min * W) - 10, int(y_min * H) - 10
            x2, y2 = int(max(x_) * W) + 10, int(max(y_) * H) + 10
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)

            # Display prediction
            cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.imshow('ASL Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
