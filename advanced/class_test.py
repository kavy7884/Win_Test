# class demo
class Bank():
    ''' The bank class '''
    counter = 0

    def __init__(self, name) -> None:
        Bank.counter += 1
        self.__name = name
        self.__balance = 0
        self.__bankname = "Taipei Bank"


    def saveMoney(self, money):
        self.__balance += money
        print("存款 ", money, " 完成！")

    def withdrawMondy(self, money):
        self.__balance -= money
        print("提款 ", money, " 完成！")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance;

    def printInfo(self):
        print(self.__name.title(), " 目前餘額： ", self.__balance)

    @classmethod
    def resetCounter(cls):
        cls.counter = 0

    @staticmethod
    def demo():
        print("I'm demo!")

    def __str__(self) -> str:
        return "Bank User: " + self.__name

    __repr__ = __str__

my_bank = Bank("kavy")
my_bank.saveMoney(1000)
print("Balance: ", my_bank.balance)
my_bank.withdrawMondy(200)
my_bank.printInfo()

my_bank_1 = Bank("kavy_1")
print(Bank.counter)
Bank.resetCounter()
print(Bank.counter)

Bank.demo()

# test inheritance
class Grandfather():
    ''' level - 0 class '''
    money_grandfather = 0
    def __init__(self) -> None:
        self.money_grandfather = 10000
    def printGrandfatherInfo(self):
        print("Grandfater!")

class Father(Grandfather):
    ''' level - 1 class '''
    money_father = 0
    def __init__(self) -> None:
        super().__init__()
        self.money_father = 500
    def printFatherInfo(self):
        print("Fater!")

class Son(Father):
    ''' level - 3 class '''
    money_son = 0
    def __init__(self) -> None:
        super().__init__()
        self.money_son = 100
    def printSonInfo(self):
        print("Son!")
    def printMoney(self):
        print("Son: ", self.money_son)
        print("Father: ", self.money_father)
        print("Grandfather: ", self.money_grandfather)

son = Son()
son.printSonInfo()
son.printFatherInfo()
son.printGrandfatherInfo()
son.printMoney()

class SonNew(Father):
    ''' level - 3 class '''
    money_son_new = 0
    def __init__(self) -> None:
        super().__init__()
        self.money_son_new = 10
    def printSonNewInfo(self):
        print("Son New!")
    def printMoney(self):
        print("Son New: ", self.money_son_new)
        Son().printMoney() #get brother class

son_new = SonNew()
son_new.printSonNewInfo()
son_new.printMoney()

#  multi-inheritance
class A():
    def __init__(self) -> None:
        super().__init__()
        print("class A")

class B():
    def __init__(self) -> None:
        super().__init__()
        print("class B")

class C(B, A):
    def __init__(self) -> None:
        super().__init__()
        print("class C")

x = C()

# type for class and member function
print(type(son))
print(type(son.printFatherInfo))

# instance of class
print(isinstance(son, Son))
print(isinstance(son, Father))
print(isinstance(son, Grandfather))
print(isinstance(son_new, Son))

# get class documents
print(son.__doc__)
print(my_bank.__doc__)

# get current name
print(__name__)

# print object test
print(my_bank)

# Implement to class iterator (run Frobenius series)
class Fib():
    def __init__(self, max) -> None:
        self.__max = max
    
    def __iter__(self):
        self.__a = 0
        self.__b = 1
        return self
    
    def __next__(self):
        fib = self.__a
        if fib > self.__max:
            raise StopIteration
        self.__a, self.__b = self.__b, self.__a + self.__b
        return fib

for i in Fib(100):
    print(i)

