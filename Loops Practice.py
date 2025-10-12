for i in range (1,6):
    for j in range (1, i+1):
        print("*", end = " ")
    print()

print("Sum of even numbers between 1 to 50:")
sum=0
for i in range(0,51,2):
    sum += i
print("Sum = ", sum)

print("Squares of first 20 numbers:")
for i in range(1,21):
    print(i," , ", i*i)

print("Sum of first 10 odd numbers:")
sum=0
i=1
while i<=20:
    if i%2!=0:
        sum += i
    i +=1
print("Sum of odd nums: ", sum)

for i in range(1,6):
    for j in range(1,i+1):
        print(i, end=" ")
    print()

print("Next pattern:\n")

for i in range (1,6):
    for j in range (6,i,-1):
        print(i, end = " ")
    print()

for i in range(1,6):
    for j in range(5,i, -1):
        print(" ", end = " ")
    for k in range(1, i+1):
        print("*", end= " ")
    print()

print("\nNow next pattern:\n")

for i in range (1,6):
    for j in range (i,0,-1):
        print(j,end=" ")
    print()

print("\nNow next pattern:\n")

for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()
for k in range(4,0,-1):
    for l in range(k,0,-1):
        print("*", end=" ")
    print()

print("\nNow next pattern:\n")

for i in range(1,9):
    for j in range (1,i+1):
        print(i*j, end=" ")
    print()

