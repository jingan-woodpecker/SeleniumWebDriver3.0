���Կ�

    *ͨ���ؼ��ֵ����ɲ��Կ��ṩ��
    *���Կ����pythonģ���ļ�
    *python���Կ�����Ĺؼ��ֵ�ʵ�ַ�ʽ
        ��ķ���
        ����
        RF�ű�ʹ�ú�����������������Сд������
        
    *RF���ֿ�·������python����һ�£�sys.path
    
repr()���ã��鿴��ÿ��������ʲô����
```idle
>>> one='123'
>>>print(repr(one))
'123'

>>>print(repr(haha))
haha
```

��ĵ���

    *����builtin�⣬�����������룬���������Ҫ��������
    *��ĵ��뷽ʽ
        һ����������ʹ�ùؼ���import library����
        ������settings������������(����)
        
    *�⵼�����Я������(�ɲ鿴seleniumlibrary�ٷ��ĵ�)
```robotframework
*** Settings ***
Library    SeleniumLibrary    timeout=5     implicit_wait=10

#Ҳ��ʹ�����ֱ�﷽ʽ
Library    SeleniumLibrary   5    10
```

RF�еı���

    *RF�еı���ʵ���Ͼ���һ��python����
        ��ָ��һ��python����
    
    *RF�ж�Ӧ����ʲôpython������������ʲô���͵ı���
    *RF�У������Ĳ�ͬ�÷�
        (1) Scalar����
                > ${var}
                > ֱ�Ӱѱ�������Ӧ��python���󴫵ݸ��ؼ��ֶ�Ӧ�ĺ���
                
        (2) List ����
                > @{var}
                > չ��List�е�ÿ��Ԫ�أ���Ϊ�����������
                
        (3) Dictionary ����
                > &{var}
                > չ��Dict�е�ÿ��Ԫ�أ���Ϊ�����������
                
    *���ʻ�������  %{env_var}
    
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
test_Scalar
    ${var1}=    returnlist
    printarg  ${var1}       
#pyton�ж������ʲô���;ͷ���ʲô���ͣ����Է��ؽ������һ���б�[1,2,3]
 
    printarg hello${var1}
#���صĵ�ʱ��Ὣ��ƴ�ӡ�hello,[1,2,3]"

test_List
    ${var1}=    returnlist
    printarg  @{var1}[0]  
#ֻȡ����һ��Ԫ�ش�ӡ���Ϊ��  1


test_Dictionary
    ${var1}=    returndict
    printarg  &{var1}
#    ��ӡ�������
#ele1:'male'
#ele2:'female'
    printarg   &{var1}[0]    
#ֻȡ����һ��Ԫ�أ����Խ��Ϊ��  'male'

    printarg  %{path}
#    ������������
```

Collections��׼��

    *���б���ֵ�Ĵ���
    
```robotframework
*** Settings ***
Library    Collections

*** Test Cases ***
test_creatlist
#    ע��������ֵķ�ʽ����Ҫ���${}
    ${list}=   Creat List   ${1}   ${2}
    Append To List  ${list}   jingan    liao
    log to console  ${list}

test_creatdictionary
    ${var}=   creat dictionary    a=${1}    b=2
    set to dictionary  ${var}     c=3 
    log to console     ${var}

```                  
        