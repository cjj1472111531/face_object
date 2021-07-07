# coding=gbk
# @file:07-引用对象.py
# @data:2021/7/7 8:51
# Editor:clown
import  sys

class Dog(object):
    pass


dog=Dog()   #调用引用一次 1
print(sys.getrefcount(dog))#计算引用一次
dog1=dog   #调用引用一次 2
print(sys.getrefcount(dog))#计算引用一次  计算引用完就没有 所以会自动减一
# dog2=dog   #调用引用一次   1
# print(sys.getrefcount(dog))#计算引用一次多一次
del dog
# print(sys.getrefcount(dog))
print(sys.getrefcount(dog1))