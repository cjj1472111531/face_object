# coding=gbk
# @file:07-teacher_version.py
# @data:2021/7/6 17:42
# Editor:clown
class Potato(object):
    def __init__(self):
        self.status='����'
        self.total_time=0

    def cook(self,time):
       # �����տ���ʱ��
        self.total_time+=time
       # �޸ĵع�״̬
        if (self.total_time>= 0) and (self.total_time< 3):
            self.status='����'
            # print("����")

        elif (self.total_time >= 3) and (self.total_time < 6):
            # print("����")
            self.status='����'

        elif (self.total_time >= 6) and (self.total_time < 8):
            # print("��͸��")
            self.status='��'
        else:
            self.status='������'

        if self.status=='����'or self.status=='����':
            cook_time=6-self.total_time
            return cook_time
        else:
            print("�˹��Ѿ�����")

    def __str__(self):
            return f"�˹ϴ����ı�{self.status},���տ�ʱ��{self.total_time}"

po=Potato()
print(po)
print("&&&&&&&&&&&&&&&&&")
z=po.cook(4)
print(z)
print(po)
print("^^^^^^^^^^^^^^^^^^^^^^^^")
po.cook(5)
print(po)
