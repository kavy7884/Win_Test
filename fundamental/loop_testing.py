# Python for
some_list = ["A", "B", "C", "D"]
for item in some_list :
    print(item)

# For with condition
file_list = ["aaa.py", "bbb.exe", "ccc.py", "ddd.txt"]
py_file = list()
for file in file_list :
    if file.endswith(".py") :
        py_file.append(file)
print(py_file)

# Range for
for x in range(3) :
    print(x)

for x in range(1, 10, 2) :
    print(x)

for x in range(3, -3, -2) :
    print(x)

# rnage sum
print(sum(range(5)))

# rnage to list
x_list = list(range(5))
print(x_list)

# list generator
x2_list = [x**2 for x in range(5)]
print(x2_list)

results_x2_list = [[x, x2] for x in x_list for x2 in x2_list]
print(results_x2_list)

# list generator with condition
tri = [[a, b, c] for a in range(1, 20) for b in range(a, 20) for c in range(b, 20) \
                    if a**2 + b**2 == c**2 \
      ]
print(tri)

# for ... else
for x2 in x2_list :
    if x2 < 0 :
        break
else :
    print("x2 not negative value")

# while with iterated object
while x_list :
    print(x_list.pop())

# enumerate
drinks = ["coffee", "tea", "wine"]
for data in enumerate(drinks) :
    print(data)

for data in enumerate(drinks, 10) :
    print(data)

scores = [21,29, 18, 33, 66, 20]

for count, score in enumerate(scores, 1) :
    if score >= 20 :
        print("場次 %d : 得分")