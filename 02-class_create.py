# coding=gbk
# @file:02-class_create.py
# @data:2021/7/5 23:01
# Editor:clown
#定义类
class Dog(object):  # 推荐用法
    #在类中定义的函数，称为方法 函数的知识都可以使用
    def play(self):
        print("小狗快乐的拆家中......")
    pass
# 创建对象 变量=类名()
dog=Dog()  #创建一个对象
print(id(dog))


dog1=Dog()  #再创建一个对象
print(id(dog1))

#可以使用对象调用类的方法  对象.方法名()
dog.play()
dog1.play()

my_list=list()

