st.py�ļ�
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
        # element�����"s"�ᱨ'WebElement' object does not support indexing ����
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
�û��ؼ���

    ͨ���ĴӲ��Կ�(python�ļ�)�����ṩ�Ĺؼ��ֽУ���ؼ���
    
    ��RF�ļ���ʵ�ֹؼ��֣����ֹؼ������ǳ�֮Ϊ�û��ؼ���
        1���û��ؼ���������RF����ĺ������Ѷ���ؼ��ֲ������һ��"��"���ؼ���
        2��������û��ؼ��ֺ󣬸ò����׼�����Ϳ���ʹ�ø��û��ؼ����ˣ�����ʹ�ÿ�ؼ���һ��
t2.robot�ļ�

```robotframework
*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Keywords ***
LoginWebsite
#    Arguments��ͷָ������
    [Arguments]      ${username}     ${password}

    Open Browser   http://localhost/mgr/login/login.html    chrome
    Set Selenium Implicit Wait   5
    Maximize Browser Window

    Input Text     id=username    ${username}
    Input Text     id=password    ${password}
    click element   tag=button

AddCourse
#    Arguments��ͷָ������
    [Arguments]       ${coursename}     ${coursedesc}     ${displayidx}

    click element   css=button[ng-click="showAddOne=true"]
    input text      css=input[ng-model="addData.name"]          ${coursename}
    input text      css=textarea[ng-model="addData.desc"]       ${coursedesc}
    input text      css=input[ng-model="addData.display_idx"]   ${displayidx}
    click element   css=button[ng-click="addOne()"]

#    ��ֹ������Ⱦ��ӵȴ�ʱ��
    sleep   1

GetLessonsList
    ${eles}=    Get Webelements    css=tr>td:nth-child(2)

    ${courses}=    create list
    :FOR   ${ele}   IN   @{eles}
       \   log to console    ${ele.text}
       \   Append To List   ${courses}   ${ele.text}

#       ��סҪ��ӷ�����Ϣ
    [Return]   ${courses}

```
��Դ�ļ�

    *�ڲ����׼��ļ��ж���ؼ��ֵ�����
        -->ֻ���ڱ������׼�����Ч���޷���������������׼�ʹ��
        
    *ʹ����Դ�ļ�(Resource)
    *��Դ�ļ���ʵ����RF����Ŀ��ļ�
        -->������԰�����������ı����͹ؼ���
        -->��Դ�ļ��ĸ�ʽ����Ҳ�Ͳ����׼��ļ�����
        
    *��������
        -->�������������ǰ�ļ���Ŀ¼ƥ������
        -->����Ҳ���������python��ģ������·��������
t1.robot�ļ�

```robotframework
*** Settings ***
Library           SeleniumLibrary
Library           Collections
Library           st
#������Դ�ļ���ʱ����Ҫ�����չ��(�������·����Ҳ���þ���·��)
Resource          t2.robot

*** Test Cases ***
test_one
    [Setup]    deleteAllCourse
    LoginWebsite    auto    sdfsdfsdf
    AddCourse    ��ѧ�����    ��ѧ������γ�����    2
    ${courses}=    GetLessonsList
    Should Be True    $courses==[u'��ѧ�����']
    Close Browser
    [Teardown]    deleteAllCourse

test_two
    [Setup]    deleteAllCourse
    LoginWebsite    auto    sdfsdfsdf
    AddCourse    javascript    javascript�γ�����    1
    ${courses}=    GetLessonsList
    Should Be True    $courses==[u'javascript']
    Close Browser
    [Teardown]    deleteAllCourse
```