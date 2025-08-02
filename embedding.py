"""
embedding.py
-------------
Loads the spam dataset, cleans it, vectorizes text using TF-IDF,
and splits into train/test sets.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
df = pd.read_csv('spam.csv', encoding='latin-1')

# Clean dataframe
df = df.rename(columns={'v1': 'label', 'v2': 'text'})
df = df[['label', 'text']]  # Keep only required columns
df['label'] = df['label'].map({'ham': 0, 'spam': 1})  # Encode labels

# Initialize TF-IDF vectorizer
vectorizer = TfidfVectorizer(max_features=5000)

# Fit & transform text
X = vectorizer.fit_transform(df['text']).toarray()
y = df['label'].values

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Optional: print shapes to verify
print(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")
