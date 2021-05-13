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

# modify list
t = [1,1,1]
print(t)
t.append(2)
print(t)
t.insert(1, 2)
print(t)
t.pop()
print(t)
t.pop(0)
print(t)
t.append(555)
print(t)
t.remove(555)
print(t)
t.reverse()
print(t)
t.sort()
print(t)
t.sort(reverse=True)
print(t)
t.insert(0, 555)
print(t)
print(sorted(t))
print(t)
print(t.index(555))
t.sort()
print(t.index(555))
print(t.count(555))
t.append(y)
print(t)
print(t.pop())
print(t)
t.extend(x)
print(t)