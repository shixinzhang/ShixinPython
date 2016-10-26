# coding=utf-8

# 引入其他文件，通过文件名调用类,比较麻烦，下面的方法可以直接调用
# import oop
#
# h = oop.Hello("导包")
# h.sayHello()

# 从某文件中导入某类，可以直接调用
from oop import Hello
h = Hello("直接使用")
h.sayHello()