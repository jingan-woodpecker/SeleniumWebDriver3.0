测试库

    *通常关键字的是由测试库提供的
    *测试库就是python模块文件
    *python测试库里面的关键字的实现方式
        类的方法
        函数
        RF脚本使用函数名、方法名，大小写不敏感
        
    *RF发现库路径：和python程序一致，sys.path
repr()作用：查看是每个参数是什么类型

    >>> one='123'
    >>>print(repr(one))
    '123'
    
    >>>print(repr(haha))
    haha
库的导入

    *除了builtin库，无需声明导入，其它库必须要声明导入
    *库的导入方式
        一、在用例中使用关键字import library导入
        二、在settings表中声明导入(常用)
        
    *库导入可以携带参数(可查看seleniumlibrary官方文档)
    
```robotframework


*** Settings ***
Library    SeleniumLibrary    timeout=5     implicit_wait=10

#也可使用这种表达方式
Library    SeleniumLibrary   5    10
```

RF中的变量

    *RF中的变量实质上就是一个python变量
        它指向一个python对象
    
    *RF中对应的是什么python变量，它就是什么类型的变量
    *RF中，变量的不同用法
        (1) Scalar方法
                > ${var}
                > 直接把变量所对应的python对象传递给关键字对应的函数
                
        (2) List 方法
                > @{var}
                > 展开List中的每个元素，作为多个参数传入
                
        (3) Dictionary 方法
                > &{var}
                > 展开Dict中的每个元素，作为多个参数传入
                
    *访问环境变量  %{env_var}

mylib.py文件
```python
def printarg(*args,**kwargs):
    if len(args) == 0:
        print(" no----args")
    else:
        print("----args are-----")
        print("-----------------")
        for one in args:
            print(repr(one))
        print("=============")

    if len(kwargs) == 0:
        print(" no---kwargs")
    else:
        print("----kwargs are----")
        print("-------------------")
        for k,v in kwargs.items():
            print(repr(k)+":"+repr(v))
        print("--------------------")

def returnlist():
    return [1,2,3]
    
def returndict():
    return {
        'ele1':'male',
        'ele2':'female'
    }
```

```robotframework
*** Settings ***
Library    mylib
*** Test Cases ***
test_Scalar
    ${var1}=    returnlist
    printarg  ${var1}       
#pyton中定义的是什么类型就返回什么类型，所以返回结果就是一个列表[1,2,3]
 
    printarg hello${var1}
#返回的的时候会将其拼接“hello,[1,2,3]"

test_List
    ${var1}=    returnlist
    printarg  @{var1}[0]  
#只取出第一个元素打印结果为：  1


test_Dictionary
    ${var1}=    returndict
    printarg  &{var1}
#    打印结果如下
#ele1:'male'
#ele2:'female'
    printarg   &{var1}[0]    
#只取出第一个元素，所以结果为：  'male'

    printarg  %{path}
#    操作环境变量
Collections标准库

*对列表和字典的处理
*** Settings ***
Library    Collections

*** Test Cases ***
test_creatlist
#    注意添加数字的方式，需要添加${}
    ${list}=   Creat List   ${1}   ${2}
    Append To List  ${list}   jingan    liao
    log to console  ${list}

test_creatdictionary
    ${var}=   creat dictionary    a=${1}    b=2
    set to dictionary  ${var}     c=3 
    log to console     ${var}
```