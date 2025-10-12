print("To check if a number is Positive")
num = int(input("Enter a number: "))
if num>0:
    print(num,"is positive")
elif num==0:
    print(num,"is zero")
else:
    print(num,"is negative")

print("To check if a number is odd or even")
num = int(input("Enter a number: "))
if num%2==0:
    print("Number is even")
else:
    print("Number is odd")

print("To check vowel")
l = str(input("Enter a letter: "))
if l in "aeiou" or l in "AEIOU":
    print("It is a vowel")
else:
    print("not a vowel")