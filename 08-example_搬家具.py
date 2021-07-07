# coding=gbk
# @file:08-example_��Ҿ�.py
# @data:2021/7/7 9:27
# Editor:clown
# ����Ҿ��� Furniture

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


    def add_furniture(self,furniture_name,furniture_area):
        new_area=self.h_area-furniture_area#�ܵ������ȥ����Ҿߵ����
        self.h_area=new_area
        if new_area>0:
            self.furniture_list.append(furniture_name)
        else:
            print(f"����û�취����{furniture_name}")
    # def add_furniture(self,furniture_name,furniture_area):
    #     new_area=self.h_area-furniture_area#�ܵ������ȥ����Ҿߵ����
    #     self.h_area=new_area
    #     if new_area>0:
    #         self.furniture_list.append(furniture_name)
    #     else:
    #         print(f"����û�취����{furniture_name}")

    def __str__(self):
        if self.furniture_list:
            return f"���ӵ�ַΪ{self.address},������ʣ{self.h_area}," \
                   f"����{','.join(self.furniture_list)}�Ҿ�"
        else:
            return f"���ӵ�ַΪ{self.address},���������ʣ{self.h_area}"

furniture=Furniture('�յ�',10)
print(furniture)



house=House('������',100)
house.add_furniture('�յ�',10)
print(house.furniture_list)
print(house)






