# coding=gbk
# @file:07-Tteacher_new.py
# @data:2021/7/6 18:26
# Editor:clown
class Potato(object):
    def __init__(self):
        self.status='����'
        self.total_time=0
        self.namelist=[]  #���Ϸ���

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
        # buf_list=str(self.namelist)
        # buf_list=buf_list.replace('[','')
        # buf_list=buf_list.replace(']','')  #���ַ��������滻
        #�ַ���.join(�б�)�����Խ��ַ�����ӵ��б�ÿһ��Ԫ��֮��������ַ���
        if self.namelist:
            return f"�˹ϴ����ı�{self.status},���տ�ʱ��{self.total_time}," \
                   f"�˵عϵĵ���Ϊ{self.namelist}"
        else:
            return f"�˹ϴ����ı�{self.status},���տ�ʱ��{self.namelist},"


            #���ϰ�
    #���ԣ�name_list=[]
    #��������ӵ��� add()
    def tiaoliao(self,name):
        self.namelist.append(name)


po=Potato()
po.tiaoliao('��')
print(po)
print("&&&&&&&&&&&&&&&&&")
po.cook(4)
po.tiaoliao('������')
print(po)
print("^^^^^^^^^^^^^^^^^^^^^^^^")
po.cook(5)
po.tiaoliao('��Ȼ')
print(po)
