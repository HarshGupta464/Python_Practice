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