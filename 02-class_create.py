# coding=gbk
# @file:02-class_create.py
# @data:2021/7/5 23:01
# Editor:clown
#������
class Dog(object):  # �Ƽ��÷�
    #�����ж���ĺ�������Ϊ���� ������֪ʶ������ʹ��
    def play(self):
        print("С�����ֵĲ����......")
    pass
# �������� ����=����()
dog=Dog()  #����һ������
print(id(dog))


dog1=Dog()  #�ٴ���һ������
print(id(dog1))

#����ʹ�ö��������ķ���  ����.������()
dog.play()
dog1.play()

my_list=list()

