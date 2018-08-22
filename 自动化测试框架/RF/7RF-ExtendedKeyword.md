python扩展关键字
    
    1、python模块作为测试库
        *模块文件名作为测试库的名字
        *比如python的模块叫MyLibrary，对应的python文件是MyLibrary.py.那么测试库的名字就是MyLibrary
        *定义在python模块文件中的函数，名称前有下划线"_"前缀的不会作为关键字
            def _returnlist()
                return[1,3]
                
    2、python类作为测试库
        比如python文件是tlib2.py
        class SubLibrary:
            def returnint(self):
                return 3
                
            def _returnint(self):
                return 4
               
        声明
        *** Settings ***
        Library   tlib2.SubLibrary
        
        *该类中的成员方法，名称前有下划线"_"的不会作为关键字
        *导入时的参数，对应类的初始化方法
        *如果类和模块文件同名，声明的时候就可以省略后面的类名
        
    python扩展库的搜索库的规则
        完全是按照python的模块的搜索规则来的
        (1)如果在包内 pylib/lib/rightpass.py
            *** Settings ***
            Library   pylib.lib.rightpass
            -----------------------------------
            Library   pylib/lib/rightpass.py
            
        (2)在settings中声明资源文件和变量文件
            路径、目录之间的分隔符，不用点，而是用斜杠 /
            
        (3)在settings中声明测试库：
            路径、目录之间的分隔符，可以用点，也可以用斜杠 /
            路径分隔符用点后面不加.py，  用斜杠后面加.py