# coding=gbk
# @file:08-example_搬家具.py
# @data:2021/7/7 9:27
# Editor:clown
# 定义家具类 Furniture

class Furniture(object):
    def __init__(self,name,area):
        self.name=name
        self.area=area

    def __str__(self):
        return f"该家具为:{self.name},占地{self.area}平米"

class House(object):
    def __init__(self,address,all_area):
        self.address=address
        self.h_area=all_area
        self.furniture_list=[]


    def add_furniture(self,furniture_name,furniture_area):
        new_area=self.h_area-furniture_area#总的面积减去加入家具的面积
        self.h_area=new_area
        if new_area>0:
            self.furniture_list.append(furniture_name)
        else:
            print(f"房子没办法加入{furniture_name}")
    # def add_furniture(self,furniture_name,furniture_area):
    #     new_area=self.h_area-furniture_area#总的面积减去加入家具的面积
    #     self.h_area=new_area
    #     if new_area>0:
    #         self.furniture_list.append(furniture_name)
    #     else:
    #         print(f"房子没办法加入{furniture_name}")

    def __str__(self):
        if self.furniture_list:
            return f"房子地址为{self.address},房子有剩{self.h_area}," \
                   f"存在{','.join(self.furniture_list)}家具"
        else:
            return f"房子地址为{self.address},这个房子有剩{self.h_area}"

furniture=Furniture('空调',10)
print(furniture)



house=House('人民大道',100)
house.add_furniture('空调',10)
print(house.furniture_list)
print(house)






