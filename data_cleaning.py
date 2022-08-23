import pandas as pd
import csv

df = pd.read_csv("C:\\Users\\HP\\Documents\\Python Projects\\C_130_PRO\\total_stars.csv")

print(df.columns)

del df["Luminosity"]
del df["Unnamed: 0"]
del df["Unnamed: 5"]
del df["Star_name"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]

print(df.columns)

df.to_csv('total.csv')