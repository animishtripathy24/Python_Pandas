import pandas as pd
import numpy as np
d=pd.read_excel("C:\\Users\\hp\\OneDrive\\Desktop\\marks.xlsx")
df=pd.DataFrame(d)
print(f"The dataframe is : \n {df}")
#loc(startrow:endrow,startcolumn:endcolumn) is completely label based operation
print(df.loc[0:2,'Name':'DBMS'])
# if we want to display only OOPS and DBMS marks from the index 0 to 2
#then we can give the arguments in the form of list
print(df.loc[0:2,['Name','DBMS']])
#iloc(startrowindex:endrowindex,startcolumnindex:endcolumnindex) is completely index based operation
print(df.iloc[0:3,2:4])
