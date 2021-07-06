# coding=gbk
# @file:07-Tteacher_new.py
# @data:2021/7/6 18:26
# Editor:clown
class Potato(object):
    def __init__(self):
        self.status='生瓜'
        self.total_time=0
        self.namelist=[]  #调料方法

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
        # buf_list=str(self.namelist)
        # buf_list=buf_list.replace('[','')
        # buf_list=buf_list.replace(']','')  #将字符串进行替换
        #字符串.join(列表)，可以将字符串添加到列表每一个元素之间组成信字符串
        if self.namelist:
            return f"此瓜从生的变{self.status},总烧烤时间{self.total_time}," \
                   f"此地瓜的调料为{self.namelist}"
        else:
            return f"此瓜从生的变{self.status},总烧烤时间{self.namelist},"


            #调料包
    #属性：name_list=[]
    #方法：添加调料 add()
    def tiaoliao(self,name):
        self.namelist.append(name)


po=Potato()
po.tiaoliao('油')
print(po)
print("&&&&&&&&&&&&&&&&&")
po.cook(4)
po.tiaoliao('辣椒面')
print(po)
print("^^^^^^^^^^^^^^^^^^^^^^^^")
po.cook(5)
po.tiaoliao('孜然')
print(po)
