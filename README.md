# World Bank Data Cleaning Project 🧹

**Internship Task – Elevate Labs**

Cleaned and preprocessed World Bank data using Python and Pandas.

---

## 📁 Repository Contents

- `Cleaned_WorldBank_Data.csv` – Final cleaned dataset ready for analysis.  
- `WorldBank_Cleaned.ipynb` – Jupyter notebook outlining all cleaning steps with code and commentary.  
- `README.md` – Overview, steps, and how to reproduce the cleaning.

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
[LinkedIn Profile](https://www.linkedin.com/in/parampreetsinghahluwalia)  
