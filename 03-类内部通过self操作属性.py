# coding=gbk
# @file:03-���ڲ�ͨ��self��������.py
# @data:2021/7/6 11:00
# Editor:clown
class Dog(object):  # �Ƽ��÷�
    #�����ж���ĺ�������Ϊ���� ������֪ʶ������ʹ��
    #self ����Ϊ���з����ĵ�һ���βΣ���ͨ��������÷�����ʱ�򣬲���Ҫ�ֶ�����ʵ��ֵ
    #python������ �Զ����ø÷����Ķ����self������self����βδ���Ķ���
    #self  ���β���   ����д��������   һ�㲻�޸��������� Ĭ��self
    def play(self):
        print(f'self:{id(self)}')
        print(f"dog:{self.name, self.age, self.gender}")
        print(f"С�� ��{self.name}���ֵĲ����......")

# �������� ����=����()
dog=Dog()  #����һ������
print("$$$$$$$$$$$$$$$$")
dog.name='clown'
dog.age=18
dog.gender='��'
dog.play()
# print(f"dog:{dog.name,dog.age,dog.gender}")
print("$$$$$$$$$$$$$$$$")
dog1=Dog()  #����һ������
# print(f"dog1:{id(dog1)}")
dog1.name='fuck'
dog1.age=3
dog1.gender='ĸ'
dog1.play()