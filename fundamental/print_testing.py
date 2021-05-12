# print with separator and anding
num1 = 222
num2 = 333
print(num1, num2, num1+num2, sep = ", ", end = " !\n")

# simple print
score = 90
name = "Kavy"
count = 1
str = "%s 你的第 %d 次物理考試成績是 %d"
print(str % (name, count, score))

# advanced print format
x = 100
y = 10.5
s = "Deep"
print("x = /%6d/" % x)
print("y = /%6.2f/" % y)
print("s = /%6s/" % s)

print("x = /%-6d/" % x)
print("y = /%-6.2f/" % y)
print("s = /%-6s/" % s)

print("x = /%+6d/" % x)
print("y = /%+6.2f/" % y)

# scientific print
x = 12345678
print("x = /%10.1e/" % x)
print("x = /%10.2e/" % x)
print("x = /%-10.2E/" % x)
print("x = /%+10.2E/" % x)

# cut string print
str = "abcdefg"
print("str = /%10.3s/" % str)

# simple format print
score = 90
name = "Kavy"
count = 1
print("{0} 你的第 {1} 次物理考試成績是 {2}".format(name, count, score))

# alignment print
r = 5
PI = 3.14159
area = PI * r ** 2
print("半徑{0:3d}圓面積是{1:10.2f}/".format(r, area))
print("半徑{0:>3d}圓面積是{1:>10.2f}/".format(r, area))
print("半徑{0:<3d}圓面積是{1:<10.2f}/".format(r, area))
print("半徑{0:^3d}圓面積是{1:^10.2f}/".format(r, area))

# padding print
title = " Python講座 "
print("/{0:*^20s}/".format(title))

