import pandas as pd
import numpy as np
d=pd.read_excel("C:\\Users\\hp\\OneDrive\\Desktop\\NewMarks.xlsx")
df=pd.DataFrame(d)
print(f"The data frame is \n {df}")

#dropna() function removes all the rows containing NaN value(even a single value)
print(df.dropna())

# if we write in the argument how='all' then it will delete only those rows containing all the values as NaN
print(df.dropna(how='all'))

#if we have to delete columns then we have to specify the axis=1 in the argument of dropna() function
print(df.dropna(axis=1))

# the dropna function will create a new dataframe but the original dataframe will not be affected
# if we want to reflect in the original dataframe we have to specify the argument inplace=True in the dropna() function and by default it is false
df.dropna(inplace=True)
print(df)

print(df['OOPS'].dropna());

f=pd.read_excel("C:\\Users\\hp\\OneDrive\\Desktop\\NewMarks.xlsx")
df1=pd.DataFrame(f)
print(f"The dataFrame with the missing values is \n {df1}")
print(df1.fillna('missing')) #it will fill all the NaN values with missing

#use dictionary is fill NaN values for the columns separately
d1={'Name':'**','OOPS':"$$",'DBMS':"%%"}
print(df1.fillna(d1))

#if we have to fill the default marks 40 for all the missing value for OS
#print(df1['OS'].fillna(40))

print(df1['OS'].fillna(df['OS'].mean()))








