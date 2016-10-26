# coding=utf-8
__createAt_ = '5/15/2016'

# 单引号中可以使用双引号
a = 'zsx'
print(a)

b = 'my name is "zsx"'
print(b)

# 双引号中也可以交叉使用单引号，单不保留换行
c = "ghm"
print(c)

d = "her name's 'ghm'"
print(d)

# 三个引号，不管是三个单引号还是三个双引号，都表示一个字符串，只不过换行符会保留
e = '''
this
is
three
'''
print(e)

f = """
this
is
three
two
"""
print(f)

'''
这里是注释
'''

# 转义符，通过和特定字符组合表示新的意义 \' == "'"
print("it's a dog")
print('it\'s a dog')

# 自然字符串，保留转义符原来样式：在字符串前加 r
print 'it\'s not nature string'
print r'it\'s nature string'

# 字符串重复：字符串后 *n
print "hi girl \n" * 10

# 获取子字符串
str = "this is parent string"
# 根据索引获取一个字符
child1 = str[2]
print(child1)
# 根据起始、结束索引获取一段字符,注意不是逗号是冒号 :
child2 = str[0:4]
print(child2)
child3 = str[:4]  # 冒号左边为空表示从0开始
print(child3)
child4 = str[5:]  # 冒号右边为空表示到str末尾
print(child4)

