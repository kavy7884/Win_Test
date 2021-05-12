# list slice
x = [0,1,2,3,4,5,6,7,8,9]
print(x[:3])
print(x[:-3])
print(x[3:])
print(x[-3:])
print(x[-1])
# list operation
y = [10,11,12,13,14]
print(x + y)
print(y * 3)
# list delete
print(x)
del x[0:len(x):2]
print(x)
# list package
a, b, *c = x
print(a, b, c)
a, *b, c = y
print(a, b, c)