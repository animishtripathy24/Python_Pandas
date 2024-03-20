import pandas as pd
import numpy as np
l=[10,20,30,40,50]
i=np.arange(1,10,2,dtype=np.int64)
s=pd.Series(data=l,index=i)
print(f"The Basic Series is \n{s}")

#different ways of creating series in python
# 1.creating a empty series
s1=pd.Series(dtype=np.int64)
print(f"The empty series is : {s1}")

# 2.creating a series using array
arr=np.linspace(3,9,10)
n=np.arange(1,20,2)
print("The Series created using array is:")
s2=pd.Series(data=arr,index=n)
print(s2)

# 3. creating a dataframe using list
l=[10,20,30,40]
s3=pd.Series(l)
print("The series created using list is:")
print(s3)

# 4.creating a series using a dictionary
#here the keys of the dictionary acts as the index
#and the respective values acts as a data for the series
d={'A':10,'B':20,'C':30,'D':40}
s4=pd.Series(d)
print("The series created using dictionary is:")
print(s4)

#various attributes that gives information about the series in pandas
print(f"The index values of series s4 is \n: {s4.index}")
print(f"The array of values is: \n{s4.array}")
print(f"The values of the array are :\n {s4.values}")
print(f"The name of the series is: \n{s4.name}");
print(f"The shape of the array is:\n{s4.name}")
print(f"The dimension of the series is:\n {s4.ndim}")
print(f"The size of the series is : \n{s4.size}")
print(f"The memory occupied by the values are : \n{s4.nbytes}")
print(f"The memory occupied as a whole is:\n{s4.memory_usage()}")
print(f"kya hamara series khali hai....{s4.empty}")
print(f"The data types of the values of the values is: {s4.dtype}")
#the hasnans attribute checks for NaN values in the
print(f"NaN values hai??? {s4.hasnans}")




  
