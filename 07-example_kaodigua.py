# coding=gbk
# @file:07-example_kaodigua.py
# @data:2021/7/6 17:17
# Editor:clown
# ��װ��С�� 1.�������ֵ����� ȷ������ ������ʲô ��������
#          2.��������������Ϣ �����ܸ�ʲô ���Ƿ���
#          3.�������ֵ�������Ϣ ȷ��������ô��д
class Potato():
    def __init__(self,stutas,total_time):
        self.stutas=stutas
        self.time=total_time
        if (self.time>=0)and (self.time<3):
            print("�˹�Ϊ����")
        elif  (self.time>=3)and(self.time<6):
            print("�˹�Ϊ����")
        elif (self.time>=6)and(self.time<8):
            print("�˹���͸��")

    def __str__(self):
        if  self.time>6:
            return f"�˹ϵ�״̬Ϊ{self.stutas}"
        else:
            return f"�˹ϴ����ı�{self.stutas}��Ҫ���տ�ʱ��{self.time}"


    def  cook(self,time):
        self.time+=time
        if  self.time<6:
            kao_time=6-self.time
            self.stutas='������'
            self.time=kao_time
            return kao_time
        else:
            print("�˹��Ѿ������")

#���� �ع϶���
potata=Potato('����',7)
cook_time=potata.cook(1)
print(potata)
print("%%%%%%%%%%%%%%%%%%%%%%")
potata1=Potato('����',2)
cook_time=potata1.cook(3)
print('�˹Ͽ�����Ҫ%d'%cook_time+'����')
print(potata1)

