a=["Thor", "Hulk", "Ironman", "Antman"]
print(a)
print(len(a))

#add to the list
a.append("Spiderman")
print(a)
a.append("Hulk")
print(a)

#occurense of an element
print(a.count("Hulk"))

#to add to a specific location
a.insert(2, "Vision")
print(a)

#remove fom a list
a.remove("Hulk")
print(a)

#remove from a location
print(a.pop(1))
print(a)

print("Next part:\n")
b=a.copy()
print(b)

print(a.index("Antman"))

c=["Superman", "Batman"]
a.extend(c)
print(a)

a.reverse()
print(a)

a.sort()
print(a)

a.clear()
print(a)

#comprehension

l1=[10,60,40,90,50]

l2=[]
for i in l1:
    if i>45:
        l2.append(i)

print(l2)

l3=[i for i in l1 if i>45]
print('l3:', l3)

# Practice questions
print("Practice questions:\n")
A=["Ross", "Rachel", "Monica", "Joey"]
# To swap 1st and 4th element
A[0],A[3]=A[3],A[0]
print(A)

# add a value to 2nd position
A.insert(1,"Phoebe")
print(A)

#delete from 3rd position
A.pop(2)
print(A)

B=[13,7,12,10]

#multiply all nos in list

res=1
for i in B:
    res = res*i
print(res)

# print largest number
B.sort()
print(B[-1])

