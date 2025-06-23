# World Bank Data Cleaning Project 🧹

**Internship Task – Elevate Labs**

Cleaned and preprocessed World Bank data using Python and Pandas.

---# 🌍 World Bank Dataset Cleaning Project

This repository contains the cleaned version of a World Bank dataset along with the Jupyter Notebook used to process and clean the data. This project was completed as part of the **Elevate Labs Internship Task 1** by **Parampreet Singh Ahluwalia**.

---

## 📂 Files Included

| File Name | Description |
|-----------|-------------|
| `cleaned_world_bank_data.csv` | Cleaned dataset file after preprocessing and handling missing values |
| `world_Bank_cleaned.ipynb` | Jupyter Notebook with all cleaning steps performed on the raw dataset |
| `README.md` | This file, providing an overview of the project |
| `python.py`-Python script containing the full cleaning logic.|

---

## 🧠 Objective

To clean the raw World Bank dataset by:

- Identifying and handling missing values
- Standardizing column names
- Removing irrelevant or duplicated data
- Ensuring consistency in data formats (e.g., years, country names, etc.)
- Preparing the dataset for further data analysis or machine learning tasks

---

## 🛠️ Tools Used

- Python 🐍
- Pandas 🐼
- Jupyter Notebook 📓

---

## 🔍 Data Cleaning Performed

✅ Null Values Handled  
✅ Removed irrelevant or non-informative columns  
✅ Standardized column headers  
✅ Converted data types where necessary  
✅ Checked for duplicates  
✅ Exported clean dataset to CSV

---

## 📷 Preview

*You can include a screenshot of your Jupyter Notebook here:*



## 📁 Repository Contents

- `Cleaned_WorldBank_Data.csv` – Final cleaned dataset ready for analysis.  
- `WorldBank_Cleaned.ipynb` – Jupyter notebook outlining all cleaning steps with code and commentary.  
- `README.md` – Overview, steps, and how to reproduce the cleaning.
- `python.py`-Python script containing the full cleaning logic.

---

## 🧑‍💻 Cleaning Process

This S3-step (and how it’s implemented) in the notebook:

1. **Load Data**
    ```python
    import pandas as pd
    df = pd.read_csv("Cleaned_WorldBank_Data.csv")
    ```

2. **Inspect & Clean**
    ```python
    df.isnull().sum()         # Check missing values
    df = df.dropna()          # Remove rows with any missing value
    df = df.drop_duplicates() # Remove duplicate rows
    df.columns = df.columns \
        .str.strip() \
        .str.replace(" ", "_") \
        .str.lower()
    ```

3. **Save Cleaned Data**
    ```python
    df.to_csv("Cleaned_WorldBank_Data.csv", index=False)
    ```

---

## 🚀 How to Run It Locally

1. Clone the repo:
    ```bash
    git clone https://github.com/Param170906/world-bank-cleaning.git
    ```
2. Navigate into the folder:
    ```bash
    cd world-bank-cleaning
    ```
3. (Optional) Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows
    ```
4. Install dependencies:
    ```bash
    pip install pandas notebook
    ```
5. Launch Jupyter and follow the notebook:
    ```bash
    jupyter notebook WorldBank_Cleaned.ipynb
    ```

---

## 📊 Visual Overview

| Step                   | Description                                       |
|------------------------|---------------------------------------------------|
| Load dataset           | Used Pandas `read_csv` to import data            |
| Preview                | Used `df.head()` and `df.info()`                 |
| Clean                  | Removed NaNs and duplicates, standardized names |
| Save final dataset     | Re-exported clean CSV for GitHub and sharing     |

---

## 🤝 Author

**Parampreet Singh Ahluwalia**  
Elevate Labs Internship – Data Task  
[LinkedIn Profile](https://www.linkedin.com/in/parampreet-singh-ahluwalia-0704582b1/)
