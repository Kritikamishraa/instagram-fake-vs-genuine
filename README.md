

# Content for the Instagram Fake vs Genuine Account Analysis README

# 📱 Instagram Fake vs Genuine Account Analysis

This project analyzes Instagram account-level data to distinguish between fake and genuine profiles using Exploratory Data Analysis (EDA) techniques in Python.

---

## 🎯 Objective

- Understand patterns that differentiate fake accounts from genuine ones  
- Perform visual comparisons using boxplots and correlation matrices  
- Prepare data for future use in classification models

---

## 🧾 Dataset Overview

The dataset `instagram_accounts.csv` includes the following columns:

| Column Name     | Description                                      |
|------------------|--------------------------------------------------|
| Username         | Instagram handle                                 |
| Followers        | Number of followers                              |
| Following        | Number of accounts followed                      |
| Posts            | Number of posts made                             |
| Bio              | Text description in the bio section              |
| Profile_Pic      | 1 if the profile has a picture, 0 otherwise      |
| Private          | 1 if the account is private, 0 otherwise         |
| Verified         | 1 if the account is verified                     |
| Fake_Account     | 1 = Fake account, 0 = Genuine account            |

---

## 🧰 Tools Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Jupyter Notebook

---

## 📊 EDA Steps

### 1. Data Loading & Cleaning
- Load data using Pandas  
- Convert binary columns to integers  
- Check for missing values and clean  

### 2. Visual Analysis
- Distribution plot of fake vs genuine accounts  
- Boxplots for:  
  - Followers  
  - Following  
  - Posts  
- Correlation heatmap to analyze feature relationships

### 3. Export Cleaned Data
- Save cleaned data to `cleaned_instagram_data.csv` for future modeling

---

## 📈 Sample Insights

- Fake accounts often have **low followers but high following**  
- Many fake accounts **don’t have profile pictures**  
- **Verified accounts are mostly genuine**  
- **Post count tends to be lower** in fake profiles  

---

## 🧑‍💻 How to Run

1. Clone the repository  
2. Install dependencies:
```bash
pip install pandas numpy matplotlib seaborn
