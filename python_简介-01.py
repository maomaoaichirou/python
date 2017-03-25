#python 第一步 ^_^
第一步：
安装IPython、python

[fairy@bogon ~]$ ipython
Python 2.7.13 (default, Jan 12 2017, 17:59:37) 
Type "copyright", "credits" or "license" for more information.

IPython 3.2.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

Python 标识符:
    在python里，标识符有字母、数字、下划线组成。
    在python中，所有标识符可以包括英文、数字以及下划线（_），但不能以数字开头。
    python中的标识符是区分大小写的。
    以下划线开头的标识符是有特殊意义的。以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用"from xxx import *"而导入；
    以双下划线开头的（__foo）代表类的私有成员；以双下划线开头和结尾的（__foo__）代表python里特殊方法专用的标识，如__init__（）代表类的构造函数。

Python保留字符
   下面的列表显示了在Python中的保留字。这些保留字不能用作常数或变数，或任何其他标识符名称。
  
    所有Python的关键字只包含小写字母:
    and         exec        not
    assert      finally     pass
    等等...
    

行和缩进：
    学习Python与其他语言最大的区别就是，Python的代码块不使用大括号（{}）来控制类，函数以及其他逻辑判断。python最具特色的就是用缩进来写模块。
    缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。如下所示：


缩进错误：
    $ python test.py  
        File "test.py", line 5
        if True:
        ^
        IndentationError: unexpected indent


Python 代码缩进：
    python中缩进层次要求非常严格使用TAB 或者 空格  或者四个空格  对代码进行缩进,制表符不能混用. 














