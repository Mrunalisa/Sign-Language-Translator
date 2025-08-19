# Sign Language Translator

A real-time **Sign Language Translator** built using **Python**, **MediaPipe Holistic**, **OpenCV**, and **Random Forest Classifier**.
This project captures hand gestures via a webcam, processes them into hand landmarks, and translates recognized signs into **text**—bridging communication gaps for people with hearing or speech impairments.

---

## ✨ Features

* 📸 **Real-time hand tracking** using Google’s **MediaPipe Holistic**
* 🧠 **Random Forest Classifier** for robust gesture recognition
* 🔤 Supports **American Sign Language (ASL)**
* ⚡ **Fast & lightweight** – runs on a normal laptop webcam
* 💾 Easy dataset creation using image collection scripts
* 🖥️ Text output for recognized signs (future extension: speech output)

---

## 📁 Project Structure

```
.
├── .gitattributes
├── README.md
└── ASL/
    ├── data/                        # Collected gesture images
    ├── collect_imgs.py              # Capture gesture images
    ├── collect_imgs_for-e-ilu.py    # Collect specific signs (e,ilu)
    ├── create_dataset.py            # Build dataset (pickle format)
    ├── data.pickle                  # Serialized dataset (features + labels)
    ├── train_classifier.py          # Train Random Forest Classifier
    ├── model.p                      # Trained model file
    ├── inference_classifier.py      # Real-time gesture recognition
    └── requirements.txt             # Dependencies
```

---

## 🛠️ Tech Stack

* **Python 3.8+**
* **OpenCV** → Image capture & preprocessing
* **MediaPipe Holistic** → Extract 21 hand landmarks
* **Scikit-learn** → Random Forest Classifier
* **NumPy / Pickle** → Data handling & model persistence

---

## 🚀 How It Works

1. **Data Collection**
   Capture gesture images using `collect_imgs.py`. Images are stored in `data/` by label.

2. **Dataset Preparation**
   Run `create_dataset.py` to extract MediaPipe hand landmarks → store in `data.pickle`.

3. **Model Training**
   Train a Random Forest Classifier with `train_classifier.py`. The model is saved as `model.p`.

4. **Real-time Inference**
   Run `inference_classifier.py` to open webcam → system detects hand landmarks → predicts the corresponding sign → displays it as **text**.

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/Mrunalisa/Sign-Language-Translator.git
cd sign-language-translator/ASL

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

### 1. Collect Gesture Images

```bash
python collect_imgs.py
```

### 2. Create Dataset

```bash
python create_dataset.py
```

### 3. Train the Model

```bash
python train_classifier.py
```

### 4. Run Real-time Translator

```bash
python inference_classifier.py
```

---

## 📊 Example Results

* **Gesture: Hello (ASL)** → Output: `Hello`
* **Gesture: L (ASL)** → Output: `L`
  
![WhatsApp Image 2025-08-19 at 11 01 44 AM (1)](https://github.com/user-attachments/assets/0e8a0e10-c00f-41c4-a781-67819a37120e)
![WhatsApp Image 2025-08-19 at 11 01 45 AM (1)](https://github.com/user-attachments/assets/5fb3784c-8ffe-4f36-8e7c-a25db43aa4cc)
![WhatsApp Image 2025-08-19 at 11 01 41 AM](https://github.com/user-attachments/assets/8e41dd6e-067c-4e0d-90fd-e4822e28a007)
![WhatsApp Image 2025-08-19 at 11 01 41 AM (1)](https://github.com/user-attachments/assets/b0bb7bc1-589d-4a71-998d-c54e569465ab)
![WhatsApp Image 2025-08-19 at 11 01 46 AM](https://github.com/user-attachments/assets/fc0b9312-4e5a-410d-bbb7-c1ebdded7e55)
![WhatsApp Image 2025-08-19 at 11 01 43 AM (1)](https://github.com/user-attachments/assets/5b2bf5ae-58b3-4531-bf84-7b5aaa2ab49d)
![WhatsApp Image 2025-08-19 at 11 01 45 AM](https://github.com/user-attachments/assets/ad38bd82-ad82-4530-9e10-066ec3167cbf)
![WhatsApp Image 2025-08-19 at 11 01 43 AM](https://github.com/user-attachments/assets/61a50dd5-9f4c-4a78-8bd1-b2991320b8fe)
![WhatsApp Image 2025-08-19 at 11 01 42 AM](https://github.com/user-attachments/assets/e0bcb710-3d11-4924-b0c1-c0c543db89e2)
![WhatsApp Image 2025-08-19 at 11 01 42 AM (1)](https://github.com/user-attachments/assets/63d4c129-35ed-4fc8-ac24-c8a51beb55df)
![WhatsApp Image 2025-08-19 at 11 01 45 AM (2)](https://github.com/user-attachments/assets/9845e3f6-dec4-4537-b44a-3ef4d334aa4b)
![WhatsApp Image 2025-08-19 at 11 01 44 AM](https://github.com/user-attachments/assets/bbfa997c-f7d6-43ba-9462-a88ce0c2a373)

---


## 🔮 Future Scope

* Currently, the system supports **ASL gestures**; in the future, **Indian Sign Language (ISL)** can also be implemented for broader applicability.
* Expand dataset with more gestures (alphabets, words, sentences).
* Add **speech output** along with text for better accessibility.
* Support **two-hand detection** required for ISL gestures.
* Improve robustness under varied lighting & backgrounds.
* Explore **deep learning (CNN/LSTM)** for recognizing continuous/dynamic signs.


---

## 🙏 Acknowledgements

* [Google MediaPipe](https://github.com/google/mediapipe)
* [OpenCV](https://opencv.org/)
* [Scikit-learn](https://scikit-learn.org/)

---

## 📜 License

This project is licensed under the MIT License


