# coding=gbk
# @file:03-���ⲿ��Ӻͻ�ȡ��������.py
# @data:2021/7/6 10:50
# Editor:clown
class Dog(object):  # �Ƽ��÷�
    #�����ж���ĺ�������Ϊ���� ������֪ʶ������ʹ��
    def play(self):
        print("С�����ֵĲ����......")
    pass
# �������� ����=����()
dog=Dog()  #����һ������
# print(id(dog))


#�������з���
dog.play()

#������������� ����.������=����ֵ   ��� name age gengder
dog.name='clown'
dog.age=18
dog.gender='��'

#��ȡ���������  ����.����������
print(dog.name)


#�޸�����ֵ ���һ�������ھ����޸�  �����ھ������
dog.age=3
print(dog.age)


#�´���һ������
dog1=Dog()  #�ٴ���һ������
# print(id(dog1))

#������������� ����.������=����ֵ   ��� name age gengder
dog1.name='fuck'
dog1.age=15
dog1.gender='ĸ'

#��ȡ���������  ����.����������
print(dog1.name)


#�޸�����ֵ ���һ�������ھ����޸�  �����ھ������
dog1.age=3
print(dog1.age)

