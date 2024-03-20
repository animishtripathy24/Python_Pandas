import pandas as pd
s1=[28,29,24,25,28,30,32]
week1=pd.Series(s1)
print(week1)
s2=[23,25,27,29,18,19,29]
week2=pd.Series(s2)
print(week2)
s3=[28,29,24,25,28,30,32]
week3=pd.Series(s3)
print(week3)
s4=[23,25,27,29,25,27,29]
week4=pd.Series(s4)
print(week4)
d={'w1':s1,'w2':s2,'w3':s3,'w4':s4}
i=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
df=pd.DataFrame(data=d,index=i)
print(df)
print('average temperature of each day of the week')
print(df.mean(axis=1))
print('average temperature of w1,w2,w3')
print(df.mean(axis=0))
print('average temperature of the whole month')
print(df.mean())

