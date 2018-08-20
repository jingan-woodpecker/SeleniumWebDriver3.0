Testcase:

    创建一个RF测试套件，包含下面的一个用例
    用例名：
    验证当系统中没有课程的时候，是否能成功添加一个课程
    
    前置条件：
    系统中没有课程
    
    测试步骤：
    添加课程，输入课程名、详情描述、展示次序，点击创建
    
    预期结果：
    创建的课程正确显示在下面的课程列表中。
    这里为了简化，我们只检查 课程名就可以了
    
    
    注意：
    这个用例的初始化和清除操作，都是需要设置为无课程状态。
    需要我们开发一个python测试库，使用selenium库开发关键字函数deleteAllCourse， 实现使用Python自动点击删除课程按钮
    
  
st.python文件
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

t1.robot文件
```robotframework
*** Settings ***
Library    SeleniumLibrary
Library    st
Library    Collections

*** Test Cases ***
test_one
#    初始化只可以使用一个关键字
    [Setup]        deleteAllCourse
    Open Browser   http://localhost/mgr/login/login.html    chrome
    Set Selenium Implicit Wait   5
    Maximize Browser Window

    Input Text     id=username    auto
    Input Text     id=password    sdfsdfsdf
    click element   tag=button
    click element   css=button[ng-click="showAddOne=true"]
    input text     css=input[ng-model="addData.name"]          selenium
    input text     css=textarea[ng-model="addData.desc"]       selenium课程描述
    input text     css=input[ng-model="addData.display_idx"]   3
    click element  css=button[ng-click="addOne()"]

#    防止二次渲染添加等待时间
    sleep   1

    ${eles}=      Get WebElements      css=tr>td:nth-child(2)

#    创建列表
    ${lessons}=   create list

#    for循环列表使用@
    :For      ${ele}    IN       @{eles}
    \         log to console     ${ele.text}

#    判断是否只存在selenium课程
    should be true     $lessons==['selenium']

    close browser

    [Teardown]    deleteAllCourse
```
