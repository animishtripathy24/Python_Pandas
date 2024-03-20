import pandas as pd
import numpy as np
d=pd.read_excel("C:\\Users\\hp\\OneDrive\\Desktop\\Pandas Python\\Duplicate.xlsx")
df=pd.DataFrame(d)
print(f"The DataFrame containing duplicates is \n {df}")

#duplicated() function whether the data contains duplicates or not
print(df.duplicated())

#<dataframe object>.drop_duplicates creates a new dataframe with all the removed duplicates
print(df.drop_duplicates())
#if we want to reflect in the original dataframe then we have to use inplace argument
df.drop_duplicates(inplace=True)
print(f"The DataFrame with the removed duplicates is : \n {df}")

