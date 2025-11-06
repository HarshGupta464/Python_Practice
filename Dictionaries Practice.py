Student = {"Name" : "John", "Class" : "6th", "roll_no":23}
print(Student["Class"],"\n")

# Printing all keys
for x in Student:
    print(x)

print("\nPrinting all values:")
for x in Student:
    print(Student[x])

print("\nUsing value function:")
for x in Student.values():
    print(x)

print("\nUsing item function:")
for x,y in Student.items():
    print(x, "-", y)

print("\n get func:")
x=Student.get("Class")
print(x)

print("\n item func:")
x=Student.items()
print(x)

print("\nkey func:")
b= Student.keys()
print(b)

print("\n value func:")
c=Student.values()
print(c)

print("\n copy func:")
d=Student.copy()
print(d,"\n")

print("Nested Dictionary")

Employees={1: {"Name":"John", "Age":23, "Gender":"Male"},
           2:{"Name":"Lisa", "Age":24,"Gender":"Female"},
           3:{"Name":"Peter", "Age":22,"Gender":"Male"}}
print(Employees[2]["Age"])
print(Employees[1])

print("\nSort a dictionary by values:")

a={"a":12, "b":23, "c":6, "d":91,"e":45}
a=sorted(a.values())
print(a)

print("\nDictionary where values are square of keys:")

a={}
for i in range(1,16):
    a[i] = i**2
print(a)

print("\nMultiply all items in a dictionary:")
a={"a":1, "b":2, "c":3, "d":4, "e":5}
result=1

for i in a:
    result *= a[i]
print(result)

print("\nSort keys:")
a={12:"a", 56:"b", 23:"c", 48:"d", 5:"c"}
a=sorted(a.keys())
print(a)