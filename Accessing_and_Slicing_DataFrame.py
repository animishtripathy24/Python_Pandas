import pandas as pd
import numpy as np
secA={'roll':3,'Name':'raja','Marks':900}
secB={'roll':4,'Name':'Mohan','Marks':100}
secC={'roll':5,'Name':'Sohan','Marks':860}
secD={'roll':6,'Name':'Sohan','Marks':360}
secE={'roll':7,'Name':'Sohan','Marks':570}
secF={'roll':8,'Name':'Sohan','Marks':np.NaN}
secG={'roll':9,'Name':'Sohan','Marks':640}
secH={'roll':10,'Name':'Sohan','Marks':830}
secI={'roll':11,'Name':'Sohan','Marks':700}
secJ={'roll':12,'Name':'Sohan','Marks':np.NaN}
secK={'roll':13,'Name':'Sohan','Marks':85}
l1=[secA,secB,secC,secD,secE,secF,secG,secH,secI,secJ,secK]
df=pd.DataFrame(l1)
print("The dataFrame created from the dictionary is :")
print(df)

#describe() function will return all the basic stuff like count.min etc
print(df.describe())

#if we have to access multiple rows
print(df[['roll','Name']].head(5))

#returns the rowindex and series object 
for index,row in df.iterrows():
    print(index,row)

#if we want to access the marks of particular student
print()
#returns the columnindex and series object
for index,column in df.iteritems():
    print(index,column)
# len() fiunctions counts the number of rows in the dataframe
print(f"The number of rows in the dataframe is: {len(df)}")

#in the count() we can provide the axis as well
# axis=0 is for the columns
#axis=1 is for the rows
print(f"The count of columns is :{df.count(axis=0)}")
print(f"The count of rows is : {df.count(axis=1)}")

#accessing individual values
print(df.Marks[1])

#sorting dataFrame values
print("The sorted value of names are displayed here")
print(df.sort_values("Name")) # this will sort in ascending order
print("IN descending order")
print(df.sort_values(["Name","Marks"]))



