# coding=gbk
# @file:03-类外部添加和获取对象属性.py
# @data:2021/7/6 10:50
# Editor:clown
class Dog(object):  # 推荐用法
    #在类中定义的函数，称为方法 函数的知识都可以使用
    def play(self):
        print("小狗快乐的拆家中......")
    pass
# 创建对象 变量=类名()
dog=Dog()  #创建一个对象
# print(id(dog))


#调用类中方法
dog.play()

#给对象添加属性 对象.属性名=属性值   添加 name age gengder
dog.name='clown'
dog.age=18
dog.gender='公'

#获取对象的属性  对象.属性名即可
print(dog.name)


#修改属性值 添加一样，存在就是修改  不存在就是添加
dog.age=3
print(dog.age)


#新创建一个对象
dog1=Dog()  #再创建一个对象
# print(id(dog1))

#给对象添加属性 对象.属性名=属性值   添加 name age gengder
dog1.name='fuck'
dog1.age=15
dog1.gender='母'

#获取对象的属性  对象.属性名即可
print(dog1.name)


#修改属性值 添加一样，存在就是修改  不存在就是添加
dog1.age=3
print(dog1.age)

