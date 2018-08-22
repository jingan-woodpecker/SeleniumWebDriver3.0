    解决多次浏览器打开和关闭的问题:在套件初始化清除的操作中做成关键字，
    并将用例表和关键字表中关闭浏览器关键字删除
   
```robotframework
*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Variables ***
${MgLoginUrl}          http://localhost/mgr/login/login.html
&{adminuser}           name=auto     pw=sdfsdf

*** Keywords ***
Setup WebTest   
#    默认的不一定就是打开网址
    Open Browser   http://localhost    chrome
    Set Selenium Implicit Wait   5
    
Teardown  WebTest
    close browser

LoginWebsite
#    Arguments开头指定参数
    [Arguments]      ${username}     ${password}
#    进入某个页面使用goto关键字
    go to     ${MgLoginUrl}
    Set Selenium Implicit Wait   5
    Maximize Browser Window

    Input Text     id=username    ${username}
    Input Text     id=password    ${password}
    click element   tag=button

AddCourse
#    Arguments开头指定参数
    [Arguments]       ${coursename}     ${coursedesc}     ${displayidx}

    click element   css=button[ng-click="showAddOne=true"]
    input text      css=input[ng-model="addData.name"]          ${coursename}
    input text      css=textarea[ng-model="addData.desc"]       ${coursedesc}
    input text      css=input[ng-model="addData.display_idx"]   ${displayidx}
    click element   css=button[ng-click="addOne()"]

#    防止二次渲染添加等待时间
    sleep   1

GetLessonsList
    ${eles}=    Get Webelements    css=tr>td:nth-child(2)

    ${courses}=    create list
    :FOR   ${ele}   IN   @{eles}
       \   log to console    ${ele.text}
       \   Append To List   ${courses}   ${ele.text}

#       记住要添加返回信息
    [Return]   ${courses}
    
DeleteAllCourse
    LoginWebsite      &{adminuser}[name]     &{adminuser}[pw]
    Set Selenium Implicit Wait 2
    
    :FOR  ${one}  IN RANGE    99999
    \     ${deleteButtons}=   Get Element   css=button[ng-click="delOne(one)
    \     exit for loop if    ${deleteButtons}==[][]
    \     click element       @{deleteButtons}[0]   
    \     click element       css=button.bn-primary
    \     sleep   1
    
    Set Selenium Implicit Wait 10  
    
```

t1.robot文件
```robotframework
*** Settings ***
Library           SeleniumLibrary
Library           Collections
#加入资源文件的时候需要添加扩展名(可用相对路径，也可用绝对路径)
Resource          t2.robot
Suite Setup       WebTest
Suite Teardown    WebTest

*** Test Cases ***
test_one
#    deleteAllCourse写在[Setup][Teardown]中即使用例中有错误，也会执行初始化清除操作
    [Setup]        DeleteAllCourse
    LoginWebsite    &{adminuser}[name]     &{adminuser}[pw]
    AddCourse      大学计算机    大学计算机课程描述    2
    ${courses}=    GetLessonsList
    Should Be True    $courses==[u'大学计算机']
    [Teardown]     DeleteAllCourse

test_two
    [Setup]        DeleteAllCourse
    LoginWebsite    &{adminuser}[name]     &{adminuser}[pw]
    AddCourse      javascript    javascript课程描述    1
    ${courses}=    GetLessonsList
    Should Be True    $courses==[u'javascript']
    [Teardown]     DeleteAllCourse
```

变量表中声明变量

    *首先创建Variables表
    *定义列表方式：List变量
        @{xxxx}    
    *定义字典方式：Dict变量(需要以键值对形式存在)
        &{user1}    name=auto   pw=sdfsdfsdf
```robotframework
*** Variables ***
${MgLoginUrl}          http://localhost/mgr/login/login.html
${StudentsLoginUrl}    http://localhost/student/login/login.html

@{database}       127.0.0.1    3306

&{user1}    name=auto   pw=sdfsdfsdf
   
*** Test Cases ***
case1
    log to console    ${MgLoginUrl}
    log to console    ${StudentsLoginUrl}
#    指向什么类型就是什么类型，所以就会打印出列表,也可单独取出一个就用下标
    log to console    @{database}[0]
    
    log to console    &{user1}[name]
```

使用python文件提供公共变量给RF使用，只需要直接定义变量即可，完全使用python

    1、RF中声明使用变量文件在settings表中导入
        *** Settings ***
        Variables   cfg.py
        
    2、变量文件声明的时候可以使用相对路径也可以使用绝对路径
        使用相对路径的时候，RF的搜索规则和资源文件的搜索规则一样：
            >先在相对当前文件的目录，匹配搜索
            >在python模块搜索路径中搜索，可以用--pythonpath参数
            d:\rmp\rf>robot --pythonpath . tc\t1.robot
            
    3、命令行参数指定变量文件
        robot --variablefile cfg\cfg.py tc\t1.robot 
    目录结构如下：
        >rf D:\tmp\rf
            >cfg
                cfg.py
            >tc
                login
                t1.robot
                rc1.robot
    
```python
MgLoginUrl=       'http://localhost/mgr/login/login.html'
StudentsLoginUrl= 'http://localhost/student/login/login.html'

database= ['127.0.0.1','3306']

user1= {'name':'auto', 'pw':'sdfsdfsdf'}
```

