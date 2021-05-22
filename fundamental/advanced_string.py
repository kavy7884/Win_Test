# index of string
str = "Python"
print(" str[0] = ", str[0],
      "\n str[1] = ", str[1],
      "\n str[2] = ", str[2],
      "\n str[3] = ", str[3],
      "\n str[4] = ", str[4],
      "\n str[5] = ", str[5])

print(" str[-1] = ", str[-1],
      "\n str[-2] = ", str[-2],
      "\n str[-3] = ", str[-3],
      "\n str[-4] = ", str[-4],
      "\n str[-5] = ", str[-5],
      "\n str[-6] = ", str[-6])

# slice of string
str = "Deep Learning"
print(str)
print("列印str第0-2元素         = ", str[0:3])
print("列印str第1-3元素         = ", str[1:4])
print("列印str第1,3,5元素       = ", str[1:6:2])
print("列印str第1到最後元素     = ", str[1:])
print("列印str前3元素           = ", str[0:3])
print("列印str後3元素           = ", str[-3:])

# length, max and min of string
strlen = len(str)
maxstr = max(str)
minstr = min(str)
print("字串長度", strlen)
print("字串最大的unicode碼值和字元", ord(maxstr), maxstr)
print("字串最小的unicode碼值和字元", ord(minstr), minstr)

# sting to list
x = list(str)
print(x)
x[5:] = "Happy"
print(x)

# string split
str_1 = "National Taiwan University"
str_2 = "C:\\happy\\fuck"
s_str_1 = str_1.split()
s_str_2 = str_2.split("\\")
print(s_str_1)
print(s_str_2)

# string join
j_str_1 = " "
print(j_str_1.join(s_str_1))
j_str_2 = "*"
print(j_str_2.join(s_str_2))

# check start, end contents and replace
print(str_1.startswith("National"))
print(str_2.endswith("happy"))
print(str_2.replace("C", "D"))




