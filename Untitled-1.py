import pandas as pd
a=[7,9,4,5,6,3]
ds = pd.Series(a)
print(ds)

print("Now next example:\n")

b=[2,9,4,6,4]
y=pd.Series(b,index=["No.1","No.2","No.3","No.4", "No.5"])
print(y)

x = pd.read_csv("2018.csv")
print(x.head(5))