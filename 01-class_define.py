# coding=gbk
# @file:01-class_define.py
# @data:2021/7/5 22:52
# Editor:clown
# 类的组成
# 类名    关键字class
# 属性：特性：变量
# 类中属性有很多，只需要?使用的属性
'''
#object 是所有的类基类，最初是的类
#类名:遵循大驼峰的命名规范  大驼峰就是名字第一个大写
class 类名(object)
    类中代码
'''
# PEP8定义规范


class Dog(object):  # 推荐用法
    pass


class Dog1():  # 括号内容可以不写
    pass


class Dog2:  # 括号也能不行
    pass
'''
新式类：直接或间接继承object的类 
在python3当中，所有的类默认继承object类 python3中都是新式类
旧式类(经典类)：已经过时 不推荐使用
'''