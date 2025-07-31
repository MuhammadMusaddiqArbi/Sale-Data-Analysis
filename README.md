# E-commerce Sales Analysis

### An end-to-end data analysis project to uncover sales trends and insights from a real-world e-commerce dataset.

![Top 10 Products Chart](top_10_products.png)

---

## 📋 Project Overview

This project performs a comprehensive exploratory data analysis (EDA) on the "Online Retail II" dataset. The goal is to clean and process the raw transactional data to make it suitable for analysis, and then to extract actionable insights regarding sales performance, top products, and customer geography. This project serves as a practical demonstration of data cleaning, feature engineering, and visualization techniques using Python.

---

## 💾 Dataset

The data used is the **Online Retail II UCI** dataset, which contains transactional data for a UK-based online retail company from 01/12/2009 to 09/12/2011.

*   **Source:** [Kaggle - Online Retail II UCI](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci)
*   **Size:** Contains over 500,000 records.

---

## 🛠️ Tools and Libraries

*   **Python:** The core programming language for the analysis.
*   **Pandas:** Used for data manipulation, cleaning, and aggregation.
*   **Matplotlib & Seaborn:** Used for data visualization to create charts and graphs.
*   **Jupyter Notebook:** Used as the interactive environment for coding and analysis.

---

## ⚙️ Analysis Workflow

The project followed a structured approach to ensure data quality and derive meaningful insights.

#### 1. Data Cleaning and Preprocessing
*   **Handled Missing Values:** Removed rows with missing `Customer ID` as they are crucial for customer-level analysis.
*   **Corrected Data Types:** Converted `InvoiceDate` to `datetime` objects and `Customer ID` to `string` to ensure proper handling.
*   **Removed Canceled Orders:** Filtered out transactions with invoice numbers starting with 'C'.
*   **Filtered Invalid Data:** Removed records with negative quantities or zero prices, which represent returns or data errors.
*   **Feature Engineering:** Created a `TotalRevenue` column (`Quantity` * `Price`) to facilitate monetary analysis.

#### 2. Exploratory Data Analysis (EDA)
*   **Top-Selling Products:** Identified the most popular products by summing the total quantity sold for each item.
*   **Sales Trends Over Time:** Analyzed monthly sales revenue to identify seasonality and growth patterns.
*   **Geographic Analysis:** Determined the top contributing countries by total sales revenue.

---

## 📊 Key Findings & Insights

The analysis uncovered several key insights into the business's performance:

*   **Top Products:** A small number of products, such as "WORLD WAR 2 GLIDERS ASSTD DESIGNS", account for a significant portion of the total sales volume, highlighting key items for inventory management.
*   **Seasonal Sales Peak:** There is a clear and significant increase in sales revenue in the month of **November**, indicating a strong holiday shopping season that the business can capitalize on with targeted marketing.
*   **Primary Market:** The **United Kingdom** is by far the largest market, generating the vast majority of the total revenue. This underscores the importance of the domestic market while also pointing to potential for international expansion.

---

## 🚀 How to Run

To replicate this analysis, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/E-commerce-Sales-Analysis.git
    cd E-commerce-Sales-Analysis
    ```

2.  **Install the required libraries:**
    ```bash
    pip install pandas matplotlib seaborn jupyterlab
    ```

3.  **Download the dataset:**
    *   Download the `online_retail_II.xlsx` or `.csv` file from the [Kaggle link](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci) and place it in the project directory.

4.  **Run the Jupyter Notebook:**
    *   Launch Jupyter Lab and open the `.ipynb` file to see the full analysis.
    ```bash
    jupyter lab
    ```

---

## 🔮 Future Work

This foundational analysis opens the door for more advanced projects, including:

*   **Customer Segmentation:** Perform RFM (Recency, Frequency, Monetary) analysis to segment customers for targeted marketing.
*   **Market Basket Analysis:** Identify which products are frequently bought together to optimize product recommendations and bundles.
*   **Predictive Forecasting:** Build a time-series model to forecast
