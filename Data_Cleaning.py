# -*- coding: utf-8 -*-
"""Data_Cleaning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Pmzj9z15NBjugd1kS6OI56ezIOd15zTP
"""

import pandas as pd



df = pd.read_csv("online_retail_II.csv")

df.isna().sum()
df[df.Description.isna()]
df.dropna(inplace=True)
df.head()

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df.head()

df["Customer ID"] = df["Customer ID"].astype(str)
df.head()
df.dtypes

df.head()
df["Invoice"].str.startswith("C", na=False)
df.info()

df_filtered = df[df['Quantity'] > 0].copy()
df["Quantity"].head()

df_filtered["Total Revenue"] = df_filtered["Quantity"]*df_filtered["Price"]
df_filtered.head()

df_filtered.to_csv("online_retail_II_cleaned.csv")
df_filtered.head()