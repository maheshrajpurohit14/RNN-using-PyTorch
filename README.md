# 📧 Spam RNN Classifier

This project is a simple text classification tool that detects whether a message is spam or not using a Recurrent Neural Network (RNN).  
It is built with TensorFlow, Keras, and Streamlit, and trained on a custom `spam.csv` dataset.

---

## 🧰 **Project Structure**
<img width="624" height="235" alt="Screenshot 2025-08-02 103754" src="https://github.com/user-attachments/assets/685bf1d9-3add-4cf8-a1f2-b7848fa6e7f6" />


---

## 🚀 **How to Run**

### ✅ Step 1: Create virtual environment
(Recommended: Python 3.11)

```bash
python -m venv venv
venv\Scripts\activate
```

## Step 2: Install dependencies
```bash

pip install -r requirements.txt
```
✅ Step 3: Train the model
```bash
python main.py
```
✅ Step 4: Predict spam or ham
```bash
python prediction.py
```
* It will ask you to enter sample text in the console.

## Streamlit App
To run the web interface (if implemented):

```bash
streamlit run main.py
```
## Dependencies
tensorflow==2.15.0

* pandas

* numpy

* scikit-learn

* tensorboard

* matplotlib

* streamlit

* scikeras

(All listed in requirements.txt)

## Dataset
The dataset used is spam.csv, containing SMS text messages labeled as:

1 → Spam

0 → Ham (not spam)

✏️ About
This project was created by SHARAN MJ as part of an RNN classifier demo, following faculty project guidelines.

## Result

<img width="1920" height="1080" alt="Screenshot 2025-08-01 144622" src="https://github.com/user-attachments/assets/8920a51f-f402-419d-8c78-c42a2af065d4" />
<img width="1920" height="1080" alt="Screenshot 2025-08-01 144651" src="https://github.com/user-attachments/assets/25f90b14-46f0-43d2-85e7-e50b4b2d8547" />
<img width="1920" height="1080" alt="Screenshot 2025-08-01 144708" src="https://github.com/user-attachments/assets/7bd9fe16-b725-4d38-8123-a963a39b4c14" />


---

### ✅ **Next step:**
* Save this as `README.md` inside your project folder.  
* Then:
```bash
git add README.md
git commit -m "Add README.md"
git push
```
