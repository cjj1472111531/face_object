# coding=gbk
# @file:03-类内部通过self操作属性.py
# @data:2021/7/6 11:00
# Editor:clown
class Dog(object):  # 推荐用法
    #在类中定义的函数，称为方法 函数的知识都可以使用
    #self 在作为类中方法的第一个形参，在通过对象调用方法的时候，不需要手动传递实参值
    #python解释器 自动调用该方法的对象给self，所以self这个形参代表的对象
    #self  是形参名   可以写其他名字   一般不修改其他名字 默认self
    def play(self):
        print(f'self:{id(self)}')
        print(f"dog:{self.name, self.age, self.gender}")
        print(f"小狗 ：{self.name}快乐的拆家中......")

# 创建对象 变量=类名()
dog=Dog()  #创建一个对象
print("$$$$$$$$$$$$$$$$")
dog.name='clown'
dog.age=18
dog.gender='公'
dog.play()
# print(f"dog:{dog.name,dog.age,dog.gender}")
print("$$$$$$$$$$$$$$$$")
dog1=Dog()  #创建一个对象
# print(f"dog1:{id(dog1)}")
dog1.name='fuck'
dog1.age=3
dog1.gender='母'
dog1.play()