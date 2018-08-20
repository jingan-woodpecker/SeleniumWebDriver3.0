1、条件判断

    RF中用Run Keyword If关键字做条件判断
        *条件表达式参数给python的eval函数
        *run keyword if   '2018' in $html    log to console 内容---->‘2018’ in $html成立就执行后面的语句

```python
# mylib文件
import  requests

def getWebInfo():
    respose = requests.get('http:mirrors.sonu.com/centos/timetamp.txt')
    return respose.text
```

```robotframework
*** Settings ***
Library   mylib

*** Test Cases ***
test 
    ${html}=     getWebInfo
#    换行书写加三个点，条件中不可随意添加空格
    run keyword if     '2018' in $html and 'UTC' in $html
    ...                log to console     \n2018年的，UTC时间
    ...    ELSE IF     '2018' in $html    log to console    \n2018年的
    ...    ELSE IF     'UTC' in $html     log to console    \n2018年的
    ...    ELSE        log to console     /n以上都不是
     
#    另一种条件不成立的关键字(无需与run keyword if同时存在)
    run keyword unless  '2018' in $html and 'UTC' in $html
    ...                 log to console     \n不是2018年的，UTC时间
   
```

2、循环里面的判断（Dialogs库）

```robotframework
*** Settings ***
Library   Diologs

*** Test Cases ***
test_one 
    ${weight}=    get value from user      请输入你的体重
    Logs To Console     体重为${weight}
    run keyword if      int($weight)>60    log to console   体重太重了
 
# Exit for loop 相当于break,  Continue for loop相当于continue   
test_two
    :for  ${one}  in range   99999
    \     ${weight}=   get value from user    请输入你的体重      60
    \     run keyword if    $weight=='over'   Exit for loop
    \     run keyword if    int($weight)>60   log to console    太重了    ELSE  log to console  太轻了
```

3、Evaluate

    直接用python代码表达式生成一个结果
    ${var}=    set variable    ${888}
    等价于
    ${var}=    evaluate    880

```robotframework
*** Settings ***
Library   Diologs

*** Test Cases ***
test_one 
    ${var1}=   Evaluate   ['Hello', 'world']
    Log To Console   ${var1}
```

4、初始化和清除

    *setup 是测试一个用例（或者套件）前要做的事
    *teardown 是测试后要做的事
    
    *在RF中，每个测试套件目录、测试套件文件、测试用例都可以有自己的setup和teardown
    *所有的setup和teardown操作都只能由一个关键字语句构成
    
    测试套件文件的setup、teardown
    *写在测试套件文件的settings表中
    *两种类型
        Suite setup/teardown
        进入和退出这个suite执行用例前后必须执行且只分别执行一次
        
        Test setup/teardown(不常用)
        如果suite内的用例本身没有setup/teardown,才执行(缺省初始化清除)

```robotframework
*** Settings ***
Suite Setup            log to console     \n---suite st setup---          
Suite Teardown         log to console     \n---suite st teardown--- 

Test Setup             log to console     \n---test st setup---
Test Teardown          log to console     \n---test st teardown---
*** Test Cases ***
test_one 
    [Setup]      log to console      \n --- case 测试1 setup ---
    log to console 测试用例主体部分1
    [Teardown]   log to console      \n --- case 测试1 teardown ---
   
test_two
    log to console 测试用例主体部分2
    
test_three
    log to console 测试用例主体部分3

```
    测试套件目录的setup、teardown
        *在其目录下的初始化文件 __init__.txt 或者 __init__.robot里的settings表中
        *两种类型
            Suite setup/teardown
            进入和退出这个suite执行用例前后必须执行且只分别执行一次
        
            Test setup/teardown(不常用)
            如果suite内的用例、或者子套件本身没有setup/teardown,才执行(缺省初始化清除)
       
需要在"__init__.robot"文件中先添加以下内容
```robotframework
*** Settings ***
Suite Setup            log to console     \n---suite big setup---
Suite Teardown         log to console     \n---suite big teardown---

Test Setup             log to console     \n---test big default setup---
Test Teardown          log to console     \n---test big default teardown---
```
st1.robot文件内容如下
```robotframework
*** Settings ***
Suite Setup            log to console     \n---suite st setup---
Suite Teardown         log to console     \n---suite st teardown---

Test Setup             log to console     \n---test st setup---
Test Teardown          log to console     \n---test st teardown---
*** Test Cases ***
test_one
    [Setup]      log to console      \n --- case 测试1 setup ---
    log to console 测试用例主体部分1
    [Teardown]   log to console      \n --- case 测试1 teardown ---

test_two
    log to console 测试用例主体部分2
```

st2.robot文件内容如下
```robotframework
*** Settings ***

*** Test Cases ***
test_three
    [Setup]      log to console      \n --- case 测试3 setup ---
    log to console 测试用例主体部分3
    [Teardown]   log to console      \n --- case 测试3 teardown ---

```
    目录如下
    >suite
        >__init__.robot
        >st1.robot
        >st2.robot
      