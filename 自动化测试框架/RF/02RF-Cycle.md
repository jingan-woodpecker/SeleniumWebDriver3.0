1��ѭ��

    *RF��FOR��ʵ��ѭ��
        > ����List����
        > IN RANGE���÷� 

```python
# mylib�ļ�
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

Example 1
    :FOR    ${animal}  IN   è   ��   ��
    \       Log To Console    ${animal}
    \       Log To Console    �ڶ���
    Log To Console   ѭ������
    

����list�б�
    ${list}=    returnlist
#    ȡ��Ԫ����Ҫʹ��@����
    :FOR    ${index}   IN    @{list}
    \       Log To Console   ${index}
    
range���÷�
    [Documentation]    Loops over values from 0 to 9
    :FOR    ${index}    IN RANGE   10
    \       Log To Console   ${index} 

```

forѭ��ʵ����������ϵͳ�Ŀγ��д���"java"��"python"���ſγ̣���python���Ժ�RF���Էֱ�ʵ�֣�
```python
# coding:utf8
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(4)

# ----------------------------
driver.get('http://ci.ytesting.com/mgr/login/login.html')
driver.find_element_by_id('username').send_keys('auto')
driver.find_element_by_id('password').send_keys('sdfsdfsdf')
driver.find_element_by_tag_name('button').click()

eles = driver.find_elements_by_css_selector('tr>td:nth-child(2)')

lessons = []
for ele in eles:
    lessons.append(ele.text)

expected = [u'java',u'python']

if  lessons == expected:
    print ('pass')
else:
    print ('fail!!')
# ----------------------------

driver.quit()
```

```robotframework
*** Settings ***
Library           Selenium2Library
Library           Collections

*** Test Cases ***
���γ�
    [Documentation]    ���γ��Ƿ����java��python

    Open Browser   http://ci.ytesting.com/mgr/login/login.html    chrome
    Set Selenium Implicit Wait   10

    Input Text   id=username    auto
    Input Text   id=password    sdfsdfsdf
    Click Element   tag=button


    ${eles}=    Get Webelements    css=tr>td:nth-child(2)
    ${lessons}=   Create List
    :FOR   ${ele}  IN    @{eles}
    \      Append To List    ${lessons}     ${ele.text}
    Log To Console    ${lessons}

#    ${eleTxts}=  Evaluate   [ele.text for ele in $eles]

    ${expected}=   Create List    java    python

    close browser

    Lists Should Be Equal   ${lessons}    ${expected}
    Should Be True    $lessons==$ecpected

```
