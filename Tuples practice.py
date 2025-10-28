a= ("Oneplus", "Vivo", "Redmi", "Samsung", "Apple")
print(a)
print(a[1:3])
print(a[:3])
print(a[2:])
print(a[::2])
print(a[1::2])
print(a[::-1])
print(a[2::-1])

for i in a:
    print(i)

print("\n along with range and length in loop\n")

for i in range(len(a)):
    print(a[i])

print("\n next loop\n")

i=0
while i <len(a):
    print(a[i])
    i+=1

# conversion of tuple
b=list(a)
print(type(b))
print(b)

b.append("Nokia")
print(b)
b=tuple(b)
print(type(b))
print(b)

print(a.index("Redmi"))

