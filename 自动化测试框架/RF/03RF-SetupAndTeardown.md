1�������ж�

    RF����Run Keyword If�ؼ����������ж�
        *�������ʽ������python��eval����
        *run keyword if   '2018' in $html    log to console ����---->��2018�� in $html������ִ�к�������

```python
# mylib�ļ�
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
#    ������д�������㣬�����в���������ӿո�
    run keyword if     '2018' in $html and 'UTC' in $html
    ...                log to console     \n2018��ģ�UTCʱ��
```