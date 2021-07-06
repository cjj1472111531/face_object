# coding=gbk
# @file:05-__str__method.py
# @data:2021/7/6 13:37
# Editor:clown
# 1.调用时机:
#           1.'print('对象')'，会自动调用'__str__'方法
#           打印输出的结果是'__str__'方法的返回值
#           2.'str(对象)' 类型转换，将自定义转换为字符串的时候，会自动调用
# 2.作用:(1) 打印对象的时候，输出一些属性信息
#        (2)将对象转换成字符串类型的时候
#   方法必须放回一个字符串  智能有self参数

class Dog(object):
    # 在函数定义时，传入实参即可
    # 入过'__init__'方法中，有除了self之外的形参
    # 那么创建对象的时候，需要给额外的形参传入实参  '类名（实参）'
    def __init__(self, name, age):
        print("我是__init__方法，我被调用了")
        self.name = name
        self.age = age
        # self.gender=gender
        print(f"小狗的名字{self.name},它已经{self.age}岁")
        # print(f"小狗的名字{self.name},它已经{self.age}岁,性别为{self.gender}")

    def __str__(self):  #一般不加参数
        # print("我是__str__方法，我被调用了") #实际代码中不写这行代码
        return f"clown!!!的名字{self.name}-----啦啦啦啦"


    def play(self):
        print(f"小狗叫{self.name}")


# 创建对象
dog = Dog('大黄', 18)  #
print("@@@@@@@@@@@@@@@@@@@@")

print(dog)  # 没有定义__str__方法 类型转换 赋值的也是引用地址  默认

print("@@@@@@@@@@@@@@@@@@@@")
str_dog = str(dog)  # 没有定义__str__方法 类型转换 赋值的也是引用地址
                    #   用str_dog进行接收 所以 后面打印才会有效
print("**************************")
print(str_dog)

# dog.play()