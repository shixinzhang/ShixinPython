# coding=utf-8
# 一个类
class Hello:
    # 构造方法，self 类似Java 的 this
    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print("Hello class by {0}".format(self.name))


# 继承
class Hi(Hello):
    ''' Python的继承 跟我想的不太一样
    def __init__(self, name):
        self.name = name
        Hello.sayHello(self.name)
    '''

    def sayHi(self):
        print("Hi class by {0}".format(self.name))


'''
h = Hello("zsx222")
h.sayHello()
'''

hi = Hi("张拭心")
hi.sayHi()