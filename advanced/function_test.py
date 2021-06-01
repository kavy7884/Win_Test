import math
from functools import reduce
# basic function
def print_list(list_data, pre = "[ ", sep = ", ", post = " ]\n"):
    """ print list by user define format """
    print(pre, end = "")
    for idx, item in enumerate(list_data):
        if(idx < len(list_data) - 1):
            print(item, end = sep)
        else:
            print(item, end = post)

data = [1, 2, 3]
print_list(data)
print_list(data, pre = "{ ", post = " }\n")

# modified data function
def add_list(original_list,  append_list):
    """ append data into list """
    original_list.extend(append_list)

app_data = [4, 5, 6]
add_list(data, app_data)
print(data)
add_list(data[:], app_data) # pass by copy
print(data)

# pass any argument as list
def my_sum(*args):
    return sum(args)
print(my_sum(1, 2, 3, 4, 5))

def show_dict(**dict_args):
    for key, value in dict_args.items():
        print(key, ", ", value)

show_dict(kavy= 7777, aaa= 8888)

# closure
def linear(a, b):
    def first_order(x):
        return a * x + b
    return first_order

f = linear(3, 4)
print(f(1))
print(f(2))
print(f(3))

# lambda
exact_func = lambda x, y: math.sin(x) + math.sin(y)
print(exact_func(2, 5))

# filter w lambda
def oddfun(x):
    return x if (x % 2 == 1) else None

filter_odd = list(filter(oddfun, data))
print(filter_odd)

# map w lambda
map_square = list(map(lambda x:x ** 2, data))
print(map_square)

# reduce
reduce_result = reduce(lambda x, y: x * y, data)
print(reduce_result)

# user define generator
def my_range(start, stop, step = 1):
    n = start
    while n < stop:
        yield n
        n += step

for x in my_range(0, 5):
    print(x)

s = [x for x in my_range(0, 10)]
print(s)

# decorator
def upper_fun(fun):
    def new_func(args):
        old_result = fun(args)
        new_result = old_result.upper()
        return new_result
    return new_func

@upper_fun
def echo_string(str):
    return str

print(echo_string("hello world"))

def error_check(func):
    def new_func(*args):
        if args[1] != 0:
            result = func(*args)
        else:
            result = "除數不能為0!"
        return result
    return new_func

@error_check
def my_div(x, y):
    return x/y

print(my_div(5, 3))
print(my_div(5, 0))


