# coding=gbk
# @file:07-���ö���.py
# @data:2021/7/7 8:51
# Editor:clown
import  sys

class Dog(object):
    pass


dog=Dog()   #��������һ�� 1
print(sys.getrefcount(dog))#��������һ��
dog1=dog   #��������һ�� 2
print(sys.getrefcount(dog))#��������һ��  �����������û�� ���Ի��Զ���һ
# dog2=dog   #��������һ��   1
# print(sys.getrefcount(dog))#��������һ�ζ�һ��
del dog
# print(sys.getrefcount(dog))
print(sys.getrefcount(dog1))