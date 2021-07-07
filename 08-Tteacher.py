# coding=gbk
# @file:08-Tteacher.py
# @data:2021/7/7 10:15
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
        if self.furniture_list:
            return f"���ӵ�ַΪ{self.address},������ʣ{self.free_area},����{self.furniture_list}�Ҿ�"
        else:
            return f"���ӵ�ַΪ{self.address},���������ʣ{self.free_area}"

furniture=Furniture('�յ�',10)
# print(furniture)

house=House('������',100)
house.add_furniture(furniture)

print(house)