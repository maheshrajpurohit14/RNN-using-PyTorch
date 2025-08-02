"""
simplernn.py
------------
Builds and trains a simple neural network classifier for spam detection.
Saves the trained model as spam_model.h5.
"""

import tensorflow as tf
from sklearn.metrics import classification_report
from embedding import X_train, X_test, y_train, y_test

# Define the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),   # Input layer
    tf.keras.layers.Dense(64, activation='relu'),       # Hidden layer
    tf.keras.layers.Dropout(0.3),                       # Dropout for regularization
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')      # Output layer
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# TensorBoard callback for visualization (optional)
tensorboard_cb = tf.keras.callbacks.TensorBoard(log_dir='logs')

# Train the model
history = model.fit(
    X_train, y_train,
    epochs=5,
    batch_size=32,
    validation_split=0.1,
    callbacks=[tensorboard_cb]
)

# Evaluate model on test data
y_pred = (model.predict(X_test) > 0.5).astype(int)
print(classification_report(y_test, y_pred, target_names=['Ham', 'Spam']))

# Save the trained model
model.save('spam_model.h5')
print("✅ Model saved as spam_model.h5")
