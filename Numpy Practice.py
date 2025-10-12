import numpy as np
a= np.array ([7,9,9,2])
print(a)
print("===========================")

b=np.array([(7,9,9,2),(16,11,9,6)])
print(b)
print("===============================")

print("Generating Arrays:\n")

c=np.arange(10)
d=np.linspace(1,5,10)
print(c)
print(d)
print("===================================")

x=np.array([(5,6,7,6,4,3),(45,15,5,5,16,38),(63,687,91,68,98,39),(21,29,79,62,65,14)])

print("Array properties:\n")
print("Dimension of array:")
print(a.ndim)
print(b.ndim)
print(x.ndim)
print("Bytesize of each element")
print(a.itemsize)
print(b.itemsize)
print(x.itemsize)

print("Datatype of array:")
print(a.dtype)
print(x.dtype)

print("No. of elements:")
print(a.size)
print(b.size)
print(x.size)

print("Memory occupied:")
print(a.size*a.itemsize)
print(b.size*b.itemsize)
print(x.size*x.itemsize)

print("Shape of array:")
print(a.shape)
print(b.shape)
print(x.shape)

print("Array Reshape:")
y=b.reshape(4,2)
x=x.reshape(6,4)
print(y)
print(x)
print("==============================")

print("Array slicing:\n")
print(b[0,2])
print(x[3,2])
print(b[0:,2])       #displays values from 0th row till last row in 2nd column
print(x[3:,2])       #displays value from 3rd row till last row in 2nd column
print("==================================")

print("Array Value Operation")
e=np.array([7,9,9,2,16,11,96])
print(e.min())
print(e.max())
print(e.sum())
print(x.min())
print(x.sum())
print("==================================")

print("Array arithmatic operations")
c=np.array([1,9,9,6])
print(a+c)
print(a-c)
print(a*c)
print(a/c)
print("====================================")

print("a=", a)
print("b=", b)
print("x=", x)

print("Operations:")
print(b.sum(axis=0))      #sums vertically down
print(x.sum(axis=1))      #sums across horizontally
print(np.sqrt(a))
print(np.std(a))
print(np.exp(a))
print(np.log(a))
print(np.log10(a))
print("============================")

print("Stacking and flattening:")
f=np.array([(1,2,3,4),(5,6,7,8)])
print(np.vstack((b,f)))
print("---------------")
print(np.hstack((b,f)))
print("-----------------")
print(b.ravel())
print("============================")
print("End of numpy")