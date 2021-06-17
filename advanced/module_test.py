# random module
import random
# time module
import time
# system module
import sys
# keyword module
import keyword
# calender module
import calendar
# defaultdict in collections module
from collections import defaultdict
# counter in collections module
from collections import Counter
# deque in collections module
from collections import deque
# pprint in pprint module
from pprint import pprint
# itertools module
import itertools

# random in integel range
print("1-100: ", random.randint(1, 100))
print("500-1000: ", random.randint(500, 1000))
print("2000-3000: ", random.randint(2000, 3000))

# pick up randomly 
names = ["kavy", "anna", "peter", "jane"]
print(random.choice(names))

# shuffle porker
porker = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"];
random.shuffle(porker)
print(porker)

# get problem sample 
print(random.sample(porker, 3))

# get uniform distribution number
print("uniform distribution number(50-100): ")
for i in range(5):
    print(random.uniform(50, 100))

# get pseudo-random number
print("pseudo-random number(0-1): ")
for i in range(5):
    print(random.random())

# calculate run time and sleep
start_time = time.time()
time.sleep(0.1)
end_time = time.time()
print("Run time: ", end_time - start_time)

# print current system time
print(time.asctime())

# get local time data
xtime = time.localtime()
print(xtime)
print("年 ", xtime[0])
print("月 ", xtime[1])
print("日 ", xtime[2])
print("時 ", xtime[3])
print("分 ", xtime[4])
print("秒 ", xtime[5])
print("星期幾 ", xtime[6])
print("第幾天 ", xtime[7])
print("夏令時間 ", xtime[8])

# print version
print("python version:", sys.version)
print("python version:", sys.version_info)

# std input
print("請輸入字串, 輸入完成請按Enter: ")
# msg = sys.stdin.readline()
# print(msg)

# std output
sys.stdout.write("YOYOYOYO\n")

# get run platform
print(sys.platform)

# get PATH
for dir_path in sys.path:
    print(dir_path)

# get python executable modules
print(sys.executable)

# get file arguments
print("file arguments: ", sys.argv)

# list all python keywords
print("list all python keywords:")
print(keyword.kwlist)

# check python keywords
print("check python keywords:")
print(keyword.iskeyword("as"))
print(keyword.iskeyword("break"))
print(keyword.iskeyword("python"))

# check leap year
print("2020 is leap year? ", calendar.isleap(2020))
print("2021 is leap year? ", calendar.isleap(2021))

# print month calender
print(calendar.month(2021, 6))

# print year calender
print(calendar.calendar(2021))

# using defaultdict
fruits = defaultdict(int)
fruits["apple"] = 20
fruits["orange"]
print(fruits)

# using defaultdict (with lambda default)
fruits = defaultdict(lambda:10)
fruits["apple"] = 20
fruits["orange"]
print(fruits)

# get counter diction
fruits = ["apple", "orange", "apple", "banana"]
fruits_num_dict = Counter(fruits)
print(fruits_num_dict)

# get most common
my_fruit = fruits_num_dict.most_common()
print(my_fruit)
my_fruit_0 = fruits_num_dict.most_common(0)
print(my_fruit_0)
my_fruit_1 = fruits_num_dict.most_common(1)
print(my_fruit_1)
my_fruit_2 = fruits_num_dict.most_common(2)
print(my_fruit_2)

# counter plus/minus
fruits_2 = ["apple", "apple", "grape", "orange", "apple"]
fruits_2_num_dict = Counter(fruits_2)
print(fruits_num_dict + fruits_2_num_dict)
print(fruits_num_dict - fruits_2_num_dict)

# counter intersection/union
print(fruits_num_dict & fruits_2_num_dict)
print(fruits_num_dict | fruits_2_num_dict)

# deque
de = deque("kavy")
print(de)
print(de.pop())
print(de.popleft())
print(de)

# pprint
pprint(sys.path)

# chain
for i in itertools.chain([1, 2, 3], ("a", "b"), ["kavy", "katelyn"]):
    print(i)

# accumulate
for i in itertools.accumulate([1, 2, 3, 4, 5, 6]):
    print(i)

for i in itertools.accumulate([1, 2, 3, 4, 5, 6], lambda x, y: x * y):
    print(i)




