SchoolClassLib.py
```python
import requests
from cfg import g_vcode
from pprint import pprint

class SchoolClassLib:
    URL = "http://ci.ytesting.com/api/3school/school_classes"

    def __init__(self):
        self.vcode = g_vcode

    def list_school_class(self,gradeid=None):
        if gradeid != None:
            params = {
                'vcode' : self.vcode,
                'action' : 'list_classes_by_schoolgrade',
                'gradeid' : int(gradeid)
            }
        else:
            params = {
                'vcode' : self.vcode,
                'action' : 'list_classes_by_schoolgrade'
            }

        response = requests.get(self.URL,params=params)

        bodyDict = response.json()
        pprint (bodyDict, indent=2)
        return bodyDict

    def add_school_class(self,grade,name,studentlimit):
        payload = {
            'vcode' : self.vcode,
            'action' : 'add',
            'grade' : int(grade),
            'name' : name,
            'studentlimit' : int(studentlimit)
        }

        response = requests.post(self.URL,data=payload)

        bodyDict =response.json()
        pprint(bodyDict, indent=2)
        return  bodyDict

    def delete_school_class(self,classid):
        payload = {
            'vcode' : self.vcode
        }

        url = '{}/{}'.format(self.URL,classid)

        response = requests.delete(url,data=payload)

    def delete_all_school_classes(self):
        #先列出所有班级
        rd = self.list_school_class()
        pprint(rd,indent=2)

        #删除所有列出的班级
        for one in rd['retlist']:
            self.delete_school_class(one['id'])

        #再列出七年级所有班级
        rd = self.list_school_class(1)
        pprint(rd,indent=2)

        if rd['retlist'] != []:
            raise Exception ("cannot delete all school class")

if __name__ == '__main__':
    scm = SchoolClassLib()
    ret = scm.list_school_class(1)
```

添加班级.robot
```robotframework
*** Settings ***
Library   pylib.SchoolClassLib


*** Test Cases ***
添加班级1 - tc000001
    ${ret1}=       add school class    1    1班    60
    should be true       ${ret1}['retcode']==0

#列出班级，进行检验
    ${ret2}=       list school class   1
    ${fc}=    evaluate    ${ret2}['retlist'][0]
    should be true        ${fc}['id']==${ret1}['id']
    should be true        ${fc}['invitecode']==${ret1}['invitecode']

    [Teardown]       delete school class     &{ret1}[id]
```

__init__robot
```robotframework
*** Settings ***
Library       pylib.SchoolClassLib
Suite Setup   delete all school classes
```

cfg.py
```python
g_vcode = '00000001858114554618'
```