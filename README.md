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
git clone https://github.com/<your-username>/sign-language-translator.git
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


(Future: Expand vocabulary to full alphabets, words, and phrases)

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


