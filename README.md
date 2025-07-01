# 🐦 Twitter Sentiment Analysis & Visualization – Task 4 (PRODIGY_DS)

This repository contains **Task 4 of 5** from my Data Science Internship at **Prodigy InfoTech**.

---

## 🎯 Task Objective

**Task 4:** Analyze sentiment patterns in social media (Twitter) data to understand public opinion and attitudes towards specific topics.

The project uses labeled Twitter data to visualize the distribution and proportions of sentiments across various discussion topics.

---

## 🧪 Dataset Used

- `twitter_training.csv`  
- `twitter_validation.csv`  
(Sourced from Twitter data annotated for sentiment analysis)

Each entry includes:
- `ID`: Tweet ID  
- `Topic`: Main subject (e.g., "Apple", "COVID", "Microsoft")  
- `Sentiment`: Labeled as `Positive`, `Negative`, `Neutral`, or `Irrelevant`  
- `Tweet`: The tweet text

---

## 📊 Visualizations Created

- ✅ **Sentiment Distribution** – Bar plot showing overall sentiment breakdown in the dataset  
- ✅ **Stacked Bar Chart by Topic** – Sentiment proportions across topics for a comparative view

---

## 🛠️ Technologies Used

- Python  
- Pandas  
- Seaborn  
- Matplotlib

---

## 🧹 Data Preprocessing Steps

- Loaded and combined training and validation datasets  
- Assigned meaningful column names  
- Removed duplicate tweets  
- Grouped and normalized sentiment data for visualization

---

## 🚀 How to Run

1. Clone the repository  
2. Place `twitter_training.csv` and `twitter_validation.csv` in the project root  
3. Run the script:

```bash
python main.py
