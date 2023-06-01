 

#   MULTITHREADING

#-----fuction based multithreading:

# multithreading crete by functions

from threading import *

items = [10,20,30,40,50]

def callsquare(nums):
    print("===squares====")
    for i in nums:
        print(i*i)


def callcube(nums):
    print("===cube====")
    for i in nums:
        print(i*i*i)

t1 = Thread(target = callsquare, args = (items,))
t2 = Thread(target = callcube, args = (items,))

t1.start()
t2.start()

t1.join()
t2.join()

print("--------------------------------------------------------")


def date1():
    for i in range(5):
        print("Hello World--")


def date2():
    for i in range(5):
        print("Hy Everone---")

t1 = Thread(target = date1)
t2 = Thread(target = date2)

t1.start()
t2.start()

t1.join()
t2.join()

print("-----------------------------------------------------------")

# multithreading crete by class :


class Helloworld(Thread):
    def run(self):
        for i in range(5):
            print("Hello World--")

class Hyeverone(Thread):
    def run(self):
        for i in range(5):
            print("HY EverOne--")

a = Helloworld()
b = Hyeverone()

a.start()
b.start()

a.join()
b.join()

print("---------------------------------------------------------------------")

class hello(Thread):
    def run(self):
        for i in range(10):
            print("welcome to the city of lake---")

class world(Thread):
    def run (self):
        for i in range(10):
            print("Hello World this is the Bhopal---")

class really(Thread):
    def run(self):
        for i in range(10):
            print("You are really nice person---")

a = hello()
b = world()
c = really()

a.start()
b.start()
c.start()

a.join()
b.join()
c.join()


print("--------------------------------------------------------")

items = [10,20,30,40,50,60,70,80,90,100]

def callmultiply(nums):
    print("---Multiply---")
    for i in nums:
          print(i*i)

def calldivide(nums):
    print("----Divide------")
    for i in nums:
        print(i/i)

def calladdition(nums):
    print("----Addtion-----")
    for i in nums:
        print(i+i)
        
t1 = Thread(target = callmultiply , args = (items,))
t2 = Thread(target = calldivide , args = (items,))
t3 = Thread(target = calladdition , args = (items,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()









