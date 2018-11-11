1、导入库
    
    ---.robot文件和.py文件在同一目录中，需要将.py文件导入到.robot用例中
    比如导入mylib.py文件的导入方式: Library  mylib
    
    ---如果需要导入多个库时，不可同时导入需要多次导入
    Library mylib1
    Library mylib2
    Library mylib3
    
2、printarg用法

    >>>>可接收多个可变参数
    ${var2}=     convert to integer   22
    printarg     ${var2}   hello
    
    上面就是接收了数值22和字符串hello,可在log中查看
    
3、导入库提供参数相当于类的初始化(__init__)参数

    例如： Library    SeleniumLibrary     implicit_wait=10     5 