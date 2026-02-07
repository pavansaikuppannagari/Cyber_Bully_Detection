# Cyberbullying & Toxic Content Detection on Social Media

## 📌 Project Overview

This project focuses on detecting **cyberbullying and targeted harassment** in social media posts using Natural Language Processing (NLP) and machine learning. The model classifies each text into multiple types of bullying such as race-related, gender/sexual-related, religion-related, or non-bullying.

The goal is to support **content moderation and online safety** systems.

---

## 🧾 Problem Statement

With the growth of social media, toxic and bullying content has become a serious problem. Manual moderation does not scale. The problem is to:

> **Automatically classify a given social media post (tweet) into one of several cyberbullying categories or non-bullying.**

This can assist:
- Social platforms in moderating content
- Safety teams in prioritizing harmful posts
- Researchers in understanding online harassment patterns

---

## 📂 Dataset

- **Source:** Kaggle – Cyberbully Detection Dataset  
- **Link:** https://www.kaggle.com/datasets/momo12341234/cyberbully-detection-dataset  
- **Records:** ~100,000 tweets  
- **Columns:**  
  - `tweet_text` – raw post content  
  - `cyberbullying_type` – label with one of:
    - `not_cyberbullying`
    - `age`
    - `ethnicity`
    - `gender`
    - `religion`
    - (exact labels may vary by version – confirm after loading)

> Download the dataset from Kaggle and place it in the `data/` folder.

---

## 🧪 Approach

### 1. Text Preprocessing

- Lowercasing
- URL, mention, hashtag, and emoji removal or normalization
- Tokenization
- Stopword removal (experimented)
- Lemmatization (where applicable)
- Handling class imbalance (e.g., class weights or oversampling)

### 2. Feature Engineering / Representations

**Classical NLP:**
- Bag-of-Words (BoW) baseline
- TF–IDF n-grams (unigram + bigram)

### 3. Models

**Baseline models:**
- Logistic Regression
- Decision Tree Classifier


### 4. Evaluation

Since this is a multi-class problem, the project reports:
- Accuracy
- Macro / weighted Precision, Recall, F1-score
- Confusion matrix per cyberbullying category
- Classification report for detailed view

---

## 📊 Key Results

> Update with your actual numbers after training.

- Best performing model: `Decision Tree`  
- Overall Accuracy: `99.45%`  
- Macro F1-score: `99.00`  
- Per-class F1:
  - `not_cyberbullying`: `100.00`
  - `ethnicity`: `99.00`
  - `gender`: `100.00`
  - `religion`: `99.00`
 

- 2nd Model that performs best - 'Logistic Regression' 
- Overall Accuracy: `99.22%`  
- Macro F1-score: `99.00`  
- Per-class F1:
  - `not_cyberbullying`: `99.00`
  - `ethnicity`: `99.00`
  - `gender`: `99.00`
  - `religion`: `98.00`

---

