__author__ = 'zhangshixin-pc'
# 函数

def sayHello():
    print("Hello Python zsx")


def getMax(a, b):
    if a > b:
        return a
    else:
        return b


def saySomething(a):
    print(a)


sayHello()
saySomething("haha")
print("max is {0}".format(getMax(31, 6)))