# coding=gbk
# @file:07-example_kaodigua.py
# @data:2021/7/6 17:17
# Editor:clown
# 封装的小套 1.根据文字的描述 确定对象 对象有什么 就是属性
#          2.根据文字描述信息 对象能干什么 就是方法
#          3.根据文字的描述信息 确定方法怎么书写
class Potato():
    def __init__(self,stutas,total_time):
        self.stutas=stutas
        self.time=total_time
        if (self.time>=0)and (self.time<3):
            print("此瓜为生瓜")
        elif  (self.time>=3)and(self.time<6):
            print("此瓜为半熟")
        elif (self.time>=6)and(self.time<8):
            print("此瓜熟透了")

    def __str__(self):
        if  self.time>6:
            return f"此瓜的状态为{self.stutas}"
        else:
            return f"此瓜从生的变{self.stutas}需要的烧烤时间{self.time}"


    def  cook(self,time):
        self.time+=time
        if  self.time<6:
            kao_time=6-self.time
            self.stutas='变熟了'
            self.time=kao_time
            return kao_time
        else:
            print("此瓜已经是熟的")

#创建 地瓜对象
potata=Potato('熟了',7)
cook_time=potata.cook(1)
print(potata)
print("%%%%%%%%%%%%%%%%%%%%%%")
potata1=Potato('生的',2)
cook_time=potata1.cook(3)
print('此瓜烤还需要%d'%cook_time+'分钟')
print(potata1)

