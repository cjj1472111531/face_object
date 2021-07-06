# coding=gbk
# @file:04-__init__method.py
# @data:2021/7/6 12:45
# Editor:clown
#__init__方法  在满足特定条件下 会自动调用，这一类称之为魔法方法
# 1.魔法方法在什么情况下调用
# 2.魔法方法是有什么用
# 3.魔法方法有哪些注意事项  __init__ 构造函数
# 1.调用时机:在创建对象之后，会立即调用
# 2.作用:(1)用来给对象添加属性，给对象属性一个初始值(构造函数)
#        (2)代码业务需求，每创建一个对象，都需要执行的代码写在'__init__'中

class Dog(object):
    def __init__(self):
        print("我是__init__方法，我被调用了")
        self.name='clown'
        self.age=18
        self.gender='男'
        print(f"小狗的名字{self.name},它多大了{self.age},性别为{self.gender}")

#创建对象
buf=Dog()
print("%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(buf.name,buf.age,buf.gender)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(buf)








