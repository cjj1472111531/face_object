# coding=gbk
# @file:08-����__repr__����.py
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

    def __repr__(self):  #����������
        '''
        1.�Զ���ӡ�б�����  ����ֱ����ʾ��Ϣ  ��������Ķ���
        :return: repr������str�����ǳ����� ���뷵��һ���ַ���
        '''
        return  f"{self.name}---- {self.age}"



my_list1=[Dog(1,2),Dog(3,4),Dog(5,6)]
print(my_list1)   #__repr__����
dog=Dog("С��",18)
print(dog)        #__str__����