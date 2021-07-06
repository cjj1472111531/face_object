# coding=gbk
# @file:07-teacher_version.py
# @data:2021/7/6 17:42
# Editor:clown
class Potato(object):
    def __init__(self):
        self.status='生瓜'
        self.total_time=0

    def cook(self,time):
       # 计算烧烤总时间
        self.total_time+=time
       # 修改地瓜状态
        if (self.total_time>= 0) and (self.total_time< 3):
            self.status='生瓜'
            # print("生瓜")

        elif (self.total_time >= 3) and (self.total_time < 6):
            # print("半熟")
            self.status='半熟'

        elif (self.total_time >= 6) and (self.total_time < 8):
            # print("熟透了")
            self.status='熟'
        else:
            self.status='烤糊了'

        if self.status=='生瓜'or self.status=='半熟':
            cook_time=6-self.total_time
            return cook_time
        else:
            print("此瓜已经熟了")

    def __str__(self):
            return f"此瓜从生的变{self.status},总烧烤时间{self.total_time}"

po=Potato()
print(po)
print("&&&&&&&&&&&&&&&&&")
z=po.cook(4)
print(z)
print(po)
print("^^^^^^^^^^^^^^^^^^^^^^^^")
po.cook(5)
print(po)
