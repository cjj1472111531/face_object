# coding=gbk
# @file:04-__init__method.py
# @data:2021/7/6 12:45
# Editor:clown
#__init__����  �������ض������� ���Զ����ã���һ���֮Ϊħ������
# 1.ħ��������ʲô����µ���
# 2.ħ����������ʲô��
# 3.ħ����������Щע������  __init__ ���캯��
# 1.����ʱ��:�ڴ�������֮�󣬻���������
# 2.����:(1)����������������ԣ�����������һ����ʼֵ(���캯��)
#        (2)����ҵ������ÿ����һ�����󣬶���Ҫִ�еĴ���д��'__init__'��

class Dog(object):
    def __init__(self):
        print("����__init__�������ұ�������")
        self.name='clown'
        self.age=18
        self.gender='��'
        print(f"С��������{self.name},�������{self.age},�Ա�Ϊ{self.gender}")

#��������
buf=Dog()
print("%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(buf.name,buf.age,buf.gender)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(buf)








