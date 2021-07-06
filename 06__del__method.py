# coding=gbk
# @file:06__del__method.py
# @data:2021/7/6 14:31
# Editor:clown
# 1.调用时机:   __del__()
#           对象在内存中被销毁删除时(引用计数为0)会自动调用__del__方法
#           1.程序代码运行结束，在程序运行过程中 创建的所有对象和变量都被删除销毁
#           2.使用'del变量'   将这个对象引用计数变为0 ，会自动调用
# 2.场景:    引用计数 ：是python内存管理的一种机制，是指一块内存，有多少变量在引用
#           1.当一个变量，引用一块内存时 计数为一
#           2.删除一个变量或不再引用这个内存的话 计数减一
#           3.当内存的引用计数变为0的时候  内存被删除 内存数据被删除
# my_list=[1,2]    #1
# my_list1=my_list #2
# del my_list
# del my_list1
class Dog(object):
    # 在函数定义时，传入实参即可
    # 入过'__init__'方法中，有除了self之外的形参
    # 那么创建对象的时候，需要给额外的形参传入实参  '类名（实参）'
    def __init__(self, name, age):
        print("我是__init__方法，我被调用了")
        self.name = name
        self.age = age
        # self.gender=gender
        print(f"小狗的名字{self.name},它已经{self.age}岁")
        # print(f"小狗的名字{self.name},它已经{self.age}岁,性别为{self.gender}")

    def __str__(self):  #一般不加参数
        # print("我是__str__方法，我被调用了") #实际代码中不写这行代码
        return f"clown!!!的名字{self.name}-----啦啦啦啦"

    def __del__(self):
        print(f"我是__del__方法，我被调用了,{self.name}被销毁了")

# dog=Dog('小白',18)
# print("%%%%%%%%%%%%%%%%%%%%")
# # print(dog)
# # print("*"*20)
#
# buf=str(dog)
# print(buf)
# print("@@@@@@@@@@@@@@@@@@@@")
# # del dog
dog=Dog('小花',3) #小花 引用计数1
dog1=dog  #小花 引用计数2
print('第一次删除之前')
del dog   #dog变量不能使用 小花对象引用计数1
print('第一次删除之后')

print('第二次删除之前')
del dog1  #dog1变量不能使用 小花对象引用计数0，会立即调用__del__
print('第二次删除之后')

