# coding=gbk
# @file:08-打印家具信息.py
# @data:2021/7/7 10:35
# Editor:clown
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
        self.free_area=all_area  #剩余面积


    def add_furniture(self,furniture_object):  #家具类对象
        if self.free_area>furniture_object.area:
            self.furniture_list.append(furniture_object.name)
            self.free_area-=furniture_object.area  #修改剩余空间
            print(f"家具：{furniture_object.name}添加成功")
        else:
            print(f"房子没办法加入{furniture_object}")


    def __str__(self):
        #自定义家具类 将该类的对象添加到列表中(容器内)，直接打印则显示自定义对象地址信息
        #[家具对象]---->[家具类型]
            # if self.furniture_list:
            #     print(self.furniture_list)
            #     return f"房子地址为{self.address},房子有剩{self.free_area}" \
            #            f",存在{','.join(self.furniture_list)}家具"
            # else:
            #     return f"房子地址为{self.address},这个房子有剩{self.free_area}"
        #自己写的
        # if self.furniture_list:
        #     buf = [obj.name for obj in self.furniture_list]
        #     return f"房子地址为{self.address},占地面积：{self.h_area},房子有剩{self.free_area}" \
        #            f"存在{','.join(buf)}家具"
        # else:
        #     return f"房子地址为{self.address},占地面积：{self.h_area},这个房子有剩{self.free_area}"


            if self.furniture_list:
                return f"房子地址为{self.address},房子有剩{self.free_area}," \
                       f"存在{','.join(self.furniture_list)}家具"
            else:
                return f"房子地址为{self.address},这个房子有剩{self.free_area}"

furniture=Furniture('空调',10)
furniture1=Furniture('大沙发',10)
# print(furniture)

house=House('人民大道',100)
house.add_furniture(furniture)
house.add_furniture(furniture1)

print(house)