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
```