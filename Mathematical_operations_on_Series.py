import pandas as pd
import numpy as np

# addition of two series for this we use .add() function
l1=[8,7,4,5]
l2=[8,7,6,4]
i1=[0,1,2,3]
i2=[0,1,'a','b']
s1=pd.Series(data=l1,index=i1)
s2=pd.Series(data=l2,index=i2)
print(f"The addition of two series is:\n {s1+s2}")
#for all the matching values it adds and returns NAN for non matching
print(f"The subtraction of the two series is")
print(s1-s2)
print(s2-s1)
print(f"The multiplication of the two series is")
print(s1*s2)
print(f"The division of the two series is")
print(s1.divide(s2))
print(f"The power of the two series is")
print(s1.pow(s2))
print(s1<s2) #this will not work for above example as it works for only identical labelled series
print(s1>s2)#this will not work for above example as it works for only identical labelled series
print(s1==s2)#this will not work for above example as it works for only identical labelled series



 
