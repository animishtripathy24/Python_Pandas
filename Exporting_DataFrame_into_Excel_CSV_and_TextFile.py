import pandas as pd
import numpy as np
d=pd.read_excel("C:\\Users\\hp\\OneDrive\\Desktop\\marks.xlsx")
df=pd.DataFrame(d)
df['Total_Marks']=df['OS']+df['DBMS']+df['Maths']
df.to_excel("C:\\Users\\hp\\OneDrive\\Desktop\\NewMarks.xlsx",index=False)
df.to_csv("C:\\Users\hp\\OneDrive\\Desktop\\NewmarksCSV.csv",index=False)
# to export it into txt file
df.to_csv("C:\\Users\\hp\\OneDrive\\Desktop\\Newmarks.txt",index=False,sep='\t')


