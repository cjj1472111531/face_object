# coding=gbk
# @file:04-__init__������method.py
# @data:2021/7/6 13:00
# Editor:clown
#__init__����  �������ض������� ���Զ����ã���һ���֮Ϊħ������
# 1.ħ��������ʲô����µ���
# 2.ħ����������ʲô��
# 3.ħ����������Щע������  __init__ ���캯��
# 1.����ʱ��:�ڴ�������֮�󣬻���������
# 2.����:(1)����������������ԣ�����������һ����ʼֵ(���캯��)
#        (2)����ҵ������ÿ����һ�����󣬶���Ҫִ�еĴ���д��'__init__'��

class Dog(object):
    #�ں�������ʱ������ʵ�μ���
    # ���'__init__'�����У��г���self֮����β�
    # ��ô���������ʱ����Ҫ��������βδ���ʵ��  '������ʵ�Σ�'
    def __init__(self,name,age,gender ):
        print("����__init__�������ұ�������")
        self.name=name
        self.age=age
        self.gender=gender
        print(f"С��������{self.name},���Ѿ�{self.age}��,�Ա�Ϊ{self.gender}")
    def play(self):
        print(f"С����{self.name}")


#��������
buf=Dog('TTTTTTT',5,'��̬')
buf.play()
# print(buf.name,buf.age,buf.gender)

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
dog1=Dog('RRRRRRRRR',3,'����')
# print(dog1.name,dog1.age,dog1.gender)
# print(buf)