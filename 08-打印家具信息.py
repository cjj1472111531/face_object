# coding=gbk
# @file:08-��ӡ�Ҿ���Ϣ.py
# @data:2021/7/7 10:35
# Editor:clown
class Furniture(object):
    def __init__(self,name,area):
        self.name=name
        self.area=area

    def __str__(self):
        return f"�üҾ�Ϊ:{self.name},ռ��{self.area}ƽ��"

class House(object):
    def __init__(self,address,all_area):
        self.address=address
        self.h_area=all_area
        self.furniture_list=[]
        self.free_area=all_area  #ʣ�����


    def add_furniture(self,furniture_object):  #�Ҿ������
        if self.free_area>furniture_object.area:
            self.furniture_list.append(furniture_object.name)
            self.free_area-=furniture_object.area  #�޸�ʣ��ռ�
            print(f"�Ҿߣ�{furniture_object.name}��ӳɹ�")
        else:
            print(f"����û�취����{furniture_object}")


    def __str__(self):
        #�Զ���Ҿ��� ������Ķ�����ӵ��б���(������)��ֱ�Ӵ�ӡ����ʾ�Զ�������ַ��Ϣ
        #[�Ҿ߶���]---->[�Ҿ�����]
            # if self.furniture_list:
            #     print(self.furniture_list)
            #     return f"���ӵ�ַΪ{self.address},������ʣ{self.free_area}" \
            #            f",����{','.join(self.furniture_list)}�Ҿ�"
            # else:
            #     return f"���ӵ�ַΪ{self.address},���������ʣ{self.free_area}"
        #�Լ�д��
        # if self.furniture_list:
        #     buf = [obj.name for obj in self.furniture_list]
        #     return f"���ӵ�ַΪ{self.address},ռ�������{self.h_area},������ʣ{self.free_area}" \
        #            f"����{','.join(buf)}�Ҿ�"
        # else:
        #     return f"���ӵ�ַΪ{self.address},ռ�������{self.h_area},���������ʣ{self.free_area}"


            if self.furniture_list:
                return f"���ӵ�ַΪ{self.address},������ʣ{self.free_area}," \
                       f"����{','.join(self.furniture_list)}�Ҿ�"
            else:
                return f"���ӵ�ַΪ{self.address},���������ʣ{self.free_area}"

furniture=Furniture('�յ�',10)
furniture1=Furniture('��ɳ��',10)
# print(furniture)

house=House('������',100)
house.add_furniture(furniture)
house.add_furniture(furniture1)

print(house)