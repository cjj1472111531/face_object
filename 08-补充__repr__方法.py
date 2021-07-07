# coding=gbk
# @file:08-补充__repr__方法.py
# @data:2021/7/7 11:08
# Editor:clown
my_list=['hell0',"clown","python"]
print(my_list)


class  Dog(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f'{self.name},{self.age}'

    def __repr__(self):  #放在容器里
        '''
        1.自动打印列表内容  更加直接显示信息  容器里面的东西
        :return: repr方法和str方法非常类似 必须返回一个字符串
        '''
        return  f"{self.name}---- {self.age}"



my_list1=[Dog(1,2),Dog(3,4),Dog(5,6)]
print(my_list1)   #__repr__方法
dog=Dog("小黄",18)
print(dog)        #__str__方法