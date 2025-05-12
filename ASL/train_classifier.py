import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset from 'data.pickle'
with open('data.pickle', 'rb') as file:
    data_dict = pickle.load(file)

# Extract data and labels
data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.2, shuffle=True, stratify=labels, random_state=42
)

# Initialize and train the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

# Evaluate the model
y_predict = model.predict(x_test)
accuracy = accuracy_score(y_test, y_predict)

print(f"{accuracy * 100:.2f}% of samples were classified correctly!")

# Save the trained model to 'model.p'
with open('model.p', 'wb') as f:
    pickle.dump({'model': model, 'input_shape': data.shape[1]}, f)
