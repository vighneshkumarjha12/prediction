import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Simulated data, replace this with your actual data loading and preprocessing
# Assume you have 'X_images' as the image data and 'X_symptoms' as the symptoms data
# 'y' contains the labels (1 for lung cancer, 0 for no lung cancer)

# Simulated image data (replace with your actual image data loading and preprocessing)
X_images = np.random.rand(100, 64, 64, 3)  # Replace with your image dimensions

# Simulated symptoms data (replace with your actual symptoms data loading and preprocessing)
X_symptoms = np.random.rand(100, 5)  # Replace with the number of symptoms

# Simulated labels (replace with your actual labels)
y = np.random.randint(2, size=100)

# Split the data into training, validation, and test sets
X_images_train, X_images_temp, X_symptoms_train, X_symptoms_temp, y_train, y_temp = train_test_split(
    X_images, X_symptoms, y, test_size=0.3, random_state=42)

X_images_val, X_images_test, X_symptoms_val, X_symptoms_test, y_val, y_test = train_test_split(
    X_images_temp, X_symptoms_temp, y_temp, test_size=0.5, random_state=42)

# Standardize the symptoms data
scaler = StandardScaler()
X_symptoms_train = scaler.fit_transform(X_symptoms_train)
X_symptoms_val = scaler.transform(X_symptoms_val)
X_symptoms_test = scaler.transform(X_symptoms_test)

# Define the image branch of the model
image_input = tf.keras.layers.Input(shape=(64, 64, 3))
conv1 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu')(image_input)
flatten1 = tf.keras.layers.Flatten()(conv1)

# Define the symptoms branch of the model
symptoms_input = tf.keras.layers.Input(shape=(X_symptoms_train.shape[1],))
dense1 = tf.keras.layers.Dense(64, activation='relu')(symptoms_input)

# Concatenate the outputs from both branches
concatenated = tf.keras.layers.concatenate([flatten1, dense1])

# Add fully connected layers for combined features
dense2 = tf.keras.layers.Dense(128, activation='relu')(concatenated)
output = tf.keras.layers.Dense(1, activation='sigmoid')(dense2)

# Create the model
model = tf.keras.models.Model(inputs=[image_input, symptoms_input], outputs=output)

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit([X_images_train, X_symptoms_train], y_train, epochs=10, validation_data=([X_images_val, X_symptoms_val], y_val))

# Evaluate the model on the test set
loss, accuracy = model.evaluate([X_images_test, X_symptoms_test], y_test)
print(f'Test Accuracy: {accuracy * 100:.2f}%')

# Make predictions on a new data point
normal = np.random.rand(1, 64, 64, 3)  # Replace with actual image data
new_symptoms = np.random.rand(1, 5)  # Replace with actual symptoms data
new_symptoms = scaler.transform(new_symptoms)  # Standardize symptoms data

prediction = model.predict([normal, new_symptoms])

# Classify based on the threshold of 0.5
classification = 'Positive' if prediction[0, 0] >= 0.5 else 'Negative'
print(f'Prediction: {prediction[0, 0]:.4f}, Classification: {classification}')
