st.py文件
```python
from selenium import webdriver
import time

def deleteAllCourse():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get("http://localhost/mgr/login/login.html")
    driver.maximize_window()
    driver.find_element_by_id("username").send_keys("auto")
    driver.find_element_by_id("password").send_keys("sdfsdfsdf")

    driver.find_element_by_tag_name("button").click()

    # deleteButtons = driver.find_elements_by_css_selector('button[ng-click="delOne(one)"]')

    # for one in deleteButtons:
    #     one.click()
    #     driver.find_element_by_css_selector('button.btn-primary').click()

    driver.implicitly_wait(1)
    while True:
        # element不添加"s"会报'WebElement' object does not support indexing 问题
        deleteButtons = driver.find_elements_by_css_selector('button[ng-click="delOne(one)"]')
        if deleteButtons:
            deleteButtons[0].click()
            driver.find_element_by_css_selector("button.btn-primary").click()
            time.sleep(1)
        else:
            break
    driver.implicitly_wait(10)
    driver.quit()
```

上面的初始化清除也可以做成robotframework的关键字
```robotframework
*** Keywords ***
DeleteAllCourse
    LoginWebsite
    Set Selenium Implicit Wait 2
    
    :FOR  ${one}  IN RANGE    99999
    \     ${deleteButtons}=   Get Element   css=button[ng-click="delOne(one)
    \     exit for loop if    ${deleteButtons}==[][]
    \     click element       @{deleteButtons}[0]   
    \     click element       css=button.bn-primary
    \     sleep   1
    
    Set Selenium Implicit Wait 10 
    
    close browser 

```

用户关键字

    通常的从测试库(python文件)里面提供的关键字叫：库关键字
    
    在RF文件中实现关键字，这种关键字我们称之为用户关键字
        1、用户关键字类似于RF层面的函数，把多个关键字操作组成一个"宏"，关键字
        2、定义好用户关键字后，该测试套件里面就可以使用该用户关键字了，就像使用库关键字一样
t2.robot文件
```robotframework
*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Keywords ***
LoginWebsite
#    Arguments开头指定参数
    [Arguments]      ${username}     ${password}

    Open Browser   http://localhost/mgr/login/login.html    chrome
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
    

```
资源文件

    *在测试套件文件中定义关键字的问题
        -->只能在本测试套件中有效，无法共享给其它测试套件使用
        
    *使用资源文件(Resource)
    *资源文件其实就是RF层面的库文件
        -->里面可以包含用来共享的变量和关键字
        -->资源文件的格式基本也和测试套件文件类似
        
    *搜索规则
        -->首先相对搜索当前文件的目录匹配搜索
        -->如果找不到，就在python的模块搜索路径中搜索
t1.robot文件
```robotframework
*** Settings ***
Library           SeleniumLibrary
Library           Collections
Library           st
#加入资源文件的时候需要添加扩展名(可用相对路径，也可用绝对路径)
Resource          t2.robot

*** Test Cases ***
test_one
#    deleteAllCourse写在[Setup][Teardown]中即使用例中有错误，也会执行初始化清除操作
    [Setup]    deleteAllCourse
    LoginWebsite    auto    sdfsdfsdf
    AddCourse    大学计算机    大学计算机课程描述    2
    ${courses}=    GetLessonsList
    Should Be True    $courses==[u'大学计算机']
    Close Browser
    [Teardown]    deleteAllCourse

test_two
    [Setup]    deleteAllCourse
    LoginWebsite    auto    sdfsdfsdf
    AddCourse    javascript    javascript课程描述    1
    ${courses}=    GetLessonsList
    Should Be True    $courses==[u'javascript']
    Close Browser
    [Teardown]    deleteAllCourse
```