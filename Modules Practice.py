import math
import datetime
import random
import demo1 as d

x=datetime.datetime.now()
print(x)

y=datetime.datetime(1996,6,6)
print(y)

print(y.strftime("%A"))
print(y.strftime("%a"))
print(y.strftime("%B"))
print(y.strftime("%p"))

a=random.randint(1,6)
print(a)

coin=["Heads", "Tails"]
c=random.choice(coin)
print(c)

m=max(5,8,3)
print(m)

p=pow(2,4)
print(p)

s=math.sqrt(49)
print(s)

k=math.floor(2.4)
print(k)

l=math.ceil(2.4)
print((l))

val=d.add(7,2)
print(val)

n=d.employee["Name"]
print(n)