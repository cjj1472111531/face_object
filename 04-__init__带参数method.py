# coding=gbk
# @file:04-__init__带参数method.py
# @data:2021/7/6 13:00
# Editor:clown
#__init__方法  在满足特定条件下 会自动调用，这一类称之为魔法方法
# 1.魔法方法在什么情况下调用
# 2.魔法方法是有什么用
# 3.魔法方法有哪些注意事项  __init__ 构造函数
# 1.调用时机:在创建对象之后，会立即调用
# 2.作用:(1)用来给对象添加属性，给对象属性一个初始值(构造函数)
#        (2)代码业务需求，每创建一个对象，都需要执行的代码写在'__init__'中

class Dog(object):
    #在函数定义时，传入实参即可
    # 入过'__init__'方法中，有除了self之外的形参
    # 那么创建对象的时候，需要给额外的形参传入实参  '类名（实参）'
    def __init__(self,name,age,gender ):
        print("我是__init__方法，我被调用了")
        self.name=name
        self.age=age
        self.gender=gender
        print(f"小狗的名字{self.name},它已经{self.age}岁,性别为{self.gender}")
    def play(self):
        print(f"小狗叫{self.name}")


#创建对象
buf=Dog('TTTTTTT',5,'变态')
buf.play()
# print(buf.name,buf.age,buf.gender)

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
dog1=Dog('RRRRRRRRR',3,'不详')
# print(dog1.name,dog1.age,dog1.gender)
# print(buf)