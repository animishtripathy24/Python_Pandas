import pandas as pd
import numpy as np
df=pd.read_excel("C:\\Users\\hp\\OneDrive\\Desktop\\marks.xlsx")
res=pd.DataFrame(df)
print(f"The dataframe obtained is : \n{res}")

#this is the way to add column
df["Total_Marks"]=df['OS']+df['DBMS']+df['OOPS']+df['Maths']
print(df)

#to remove the column we can use drop function
#generally drop function is used to drop any row
df=df.drop(1);
#if we want to delete multiple multiple rows
#then we can pass the row number in the form of list
df=df.drop([2,3])
print(f"The dataframe after deleting row is : \n {df}")

#now if we want to delete the column we have to explicitely specify the axis=1
df=df.drop(['OS','Maths'],axis=1)
print(f"The dataframe after deleting columns is :\n {df}")

#to remove any column we can use del df["<column name>"]
del df['Total_Marks']
print(df)
