"""
prediction.py
-------------
Loads the trained model and provides a function to predict new messages.
"""

import tensorflow as tf
from embedding import vectorizer

# Load trained model
model = tf.keras.models.load_model('spam_model.h5')

def predict_spam(message: str) -> str:
    """
    Predicts whether the input message is spam or ham.

    Args:
        message (str): Input text message.
    Returns:
        str: 'Spam' or 'Ham'
    """
    vec = vectorizer.transform([message]).toarray()
    pred_prob = model.predict(vec)[0][0]
    return 'Spam' if pred_prob > 0.5 else 'Ham'
