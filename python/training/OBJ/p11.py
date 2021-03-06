#coding=utf-8
'''
多继承
概念

子类 可以拥有 多个父类，并且具有 所有父类 的 属性 和 方法
例如：孩子 会继承自己 父亲 和 母亲 的 特性

语法

class 子类名(父类名1, 父类名2...)
    pass
---------------------------------------------------------------------------

2.1 多继承的使用注意事项
问题的提出
如果 不同的父类 中存在 同名的方法，子类对象 在调用方法时，会调用 哪一个父类中的方法呢？

开发时，应该尽量避免这种容易产生混淆的情况！ 
如果 父类之间 存在 同名的属性或者方法，应该 尽量避免 使用多继承
---------------------------------------------------------------------------

Python 中的 MRO —— 方法搜索顺序（知道）
Python 中针对 类 提供了一个 内置属性 __mro__ 可以查看 方法 搜索顺序
MRO 是 method resolution order，主要用于 在多继承时判断 方法、属性 的调用 路径

print(C.__mro__)
输出结果:
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

1.在搜索方法时，是按照 __mro__ 的输出结果 从左至右 的顺序查找的
2.如果在当前类中 找到方法，就直接执行，不再搜索
3.如果 没有找到，就查找下一个类 中是否有对应的方法，如果找到，就直接执行，不再搜索
4.如果找到最后一个类，还没有找到方法，程序报错
----------------------------------------------------------------------------
新式类与旧式（经典）类
object 是 Python 为所有对象提供的 基类，提供有一些内置的属性和方法，可以使用 dir 函数查看

1.新式类：以 object 为基类的类，推荐使用
2.经典类：不以 object 为基类的类，不推荐使用
3.在 Python 3.x 中定义类时，如果没有指定父类，会默认使用 object 作为该类的 基类 —— Python 3.x 中定义的类都是 新式类
4.在 Python 2.x 中定义类时，如果没有指定父类，则不会以 object 作为 基类
新式类 和 经典类 在多继承时 —— 会影响到方法的搜索顺序

为了保证编写的代码能够同时在 Python 2.x 和 Python 3.x 运行！
今后在定义类时，如果没有父类，建议统一继承自 object
class 类名(object):
    pass
'''

