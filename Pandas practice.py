import pandas as pd
print("Practice for pandas day 1")

var=[7,9,4,5,6,3]
ds = pd.Series(var)
print(ds)

print("Now next example:\n")

var2=[2,9,4,6,4]
ds2=pd.Series(var2,index=["No.1","No.2","No.3","No.4", "No.5"])
print(ds2)

print("For dataset files:")

y=pd.read_excel("Data1.xlsx")
print(y.head(5))
z=pd.read_csv("Data2.txt")
print(z.head(5))

# Dataset details

print("# Dataset details")
print(y.shape)
print(y.describe())

for index, row in y.iterrows():
    print(index, row["Name"])

print("Next Command")

print(y["Name"][0:6])

print("Next Command")
print(y.iloc[0])

print("next command")
print(y.iloc[1:5])

print("Next Command:\n")

print(y.iloc[9,4])

print("Next Command:\n")

# Data slicing with filter
print("Data slicing with filter:\n")

print(y.loc[y["Speed"]>90])


a=y.sort_values(["Speed"], ascending = True)
print(a.head(15))


# Editing data

print("# Editing data")

y["Power"] = y["HP"] + y["Attack"]
# print(y.head(20))

y["Char"] = y["Attack"] + y["Defense"]
print(y.head(20))

y=y.drop(columns=["Char"])
print(y.head(20))

# Save data in new file
print("# Save data in new file")

y.to_csv("Newdata.csv")

# Check null values
print("# Check null values")


print(y.isna().any())

y=y[y["Type 2"].notna()]
print(y.head(20))

# Fillig NaN with mean of that specific column
print("# Fillig NaN with mean of that specific column")

meanval=y["Speed"].fillna(y["Speed"].mean())
print(meanval)

print(y.head(20))

# Mapping certain data to another value
print("# Mapping certain data to another value")

# print(y.head(20))
Generation = set(y["Generation"])
y["Generation"] = y["Generation"].map({1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six"})

print(y.head(180))

print("The end of Pandas")