import pandas as pd

# 1.creating a dataframe using excel file
d=pd.read_excel("C:\\Users\\hp\\OneDrive\\Desktop\\marks.xlsx")
df=pd.DataFrame(d)
print(f"The excel file is :")
print(df)
print(f"The first three rows of the table is : \n {df.head(3)}")

# 2.creating a dataframe from a 1-d dictionary
d1= {'name':['verma','sharma','mishra'],'total':[89,92,78]}
df1=pd.DataFrame(d1)
print(f"The dataframe created from the dictionary is : \n{df1}")

# 3.creating dataframe from the list of dictionaries
secA={'roll':3,'Name':'raja','Marks':90}
secB={'roll':4,'Name':'Mohan','Marks':100}
secC={'roll':5,'Name':'Sohan','Marks':80}
l1=[secA,secB,secC]
df=pd.DataFrame(l1,index=['a','b','c'])
print("The dataFrame created from the dictionary is :")
print(df)

#4.creating a dataframe object from a 2-D dictionary with values as series object
s1=pd.Series(['Raja','Verma','Mohan'])
s2=pd.Series([89,98,78])
d={'name':s1,'Marks':s2}
df1=pd.DataFrame(d)
print(f"The data frame created is :\n{df}")

#5.creating dataframe object from another dataframe object
df1=pd.DataFrame(df)
print(df1)


