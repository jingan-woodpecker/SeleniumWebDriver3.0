Testcase:

    ����һ��RF�����׼������������һ������
    ��������
    ��֤��ϵͳ��û�пγ̵�ʱ���Ƿ��ܳɹ����һ���γ�
    
    ǰ��������
    ϵͳ��û�пγ�
    
    ���Բ��裺
    ��ӿγ̣�����γ���������������չʾ���򣬵������
    
    Ԥ�ڽ����
    �����Ŀγ���ȷ��ʾ������Ŀγ��б��С�
    ����Ϊ�˼򻯣�����ֻ��� �γ����Ϳ�����
    
    
    ע�⣺
    ��������ĳ�ʼ�������������������Ҫ����Ϊ�޿γ�״̬��
    ��Ҫ���ǿ���һ��python���Կ⣬ʹ��selenium�⿪���ؼ��ֺ���deleteAllCourse�� ʵ��ʹ��Python�Զ����ɾ���γ̰�ť

st.python�ļ�
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

t1.robot�ļ�
```robotframework
*** Settings ***
Library    SeleniumLibrary
Library    st
Library    Collections

*** Test Cases ***
test_one
#    ��ʼ��ֻ����ʹ��һ���ؼ���
    [Setup]        deleteAllCourse
    Open Browser   http://localhost/mgr/login/login.html    chrome
    Set Selenium Implicit Wait   5
    Maximize Browser Window

    Input Text     id=username    auto
    Input Text     id=password    sdfsdfsdf
    click element   tag=button
    click element   css=button[ng-click="showAddOne=true"]
    input text     css=input[ng-model="addData.name"]          selenium
    input text     css=textarea[ng-model="addData.desc"]       selenium�γ�����
    input text     css=input[ng-model="addData.display_idx"]   3
    click element  css=button[ng-click="addOne()"]

#    ��ֹ������Ⱦ��ӵȴ�ʱ��
    sleep   1

    ${eles}=      Get WebElements      css=tr>td:nth-child(2)

#    �����б�
    ${lessons}=   create list

#    forѭ���б�ʹ��@
    :For      ${ele}    IN       @{eles}
    \         log to console     ${ele.text}

#    �ж��Ƿ�ֻ����selenium�γ�
    should be true     $lessons==['selenium']

    close browser

    [Teardown]    deleteAllCourse


```