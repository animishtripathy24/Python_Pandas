import pandas as pd
import numpy as np

d=pd.read_excel("C:\\Users\\hp\\OneDrive\\Desktop\\Pandas Python\\NewMarks.xlsx")
df=pd.DataFrame(d)
print(df)
print()
print("The details of the student that got less than 60 in OS")
print(df.loc[df['OS']<60])
print()
print("The details of the student who got less than 60marks in DBMS as well as OS are")
print(df.loc[(df["OS"]<60) & (df["DBMS"]<60)])
print()
#we can also use or(pipe | symbol)
print(df.loc[(df["OS"]<60) | (df["DBMS"]<60)])
print()
#if we want to access the name of those students whose name contains an anywhere
print(df.loc[df["Name"].str.startswith("A")])

