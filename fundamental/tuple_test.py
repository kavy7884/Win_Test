# tuple new
keys = ("NTU", "University", 9999)
print(keys)

# tuple to list
list_keys = list(keys)
print(list_keys)

# tuple to enumerate and print by for loop
for index, key in enumerate(keys):
    print(index, key)

# zip data
names = ("kavy", "peter", "jane")
zip_data = zip(keys, names)
tuple_zip_data = tuple(zip_data)
print(tuple_zip_data)

# unzip
k, n = zip(*tuple_zip_data)
print(k, n)

# generator and list generator
x = (n for n in range(3))
y = [n for n in range(3)]
print(type(x), x)
print(type(y), y)
for n in x:
    print(n)
print(y)