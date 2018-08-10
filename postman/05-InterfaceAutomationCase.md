webapi.py文件内容
```python
import requests,pprint

def login(username,password):
    payload = {
        'username': username,
        'password': password
    }
    # data参数 就是构造消息体的
    response = requests.post("http://localhost/api/mgr/loginReq",
                             data=payload)

    # 获取结果，返回给调用者
    retDict = response.json()
    # 打印出结果
    print(retDict)

    # 返回结果和cookies
    return retDict,response.cookies

# 增加课程
def add_course(name,desc,displayidx,sessionid):
    pl = {
        'action': 'add_course',
        'data' : '''
                {
                    "name":"%s",
                    "desc":"%s",
                    "display_idx":"%s"
                }
        ''' % (name,desc,displayidx)
    }

    response = requests.post("http://localhost/api/mgr/sq_mgr/",
                             data=pl,
                             cookies={'sessionid': sessionid})
    retDict=response.json()

    print(retDict)
    return retDict

# 列出课程
def list_course(sessionid):
    # 文档中参数固定，所以不用设置变量
    params = {'action':'list_course', 'pagenum':'1', 'pagesize':20}
    response = requests.get("http://localhost/api/mgr/sq_mgr/",
                            params=params,
                            cookies={'sessionid': sessionid})

    retDict = response.json()
    pprint.pprint(retDict)
    return retDict

# 修改课程
def modify_course(courseid,name,desc,displayidx,sessionid):
    pl = {
        'action':'modify_course',
        'id':courseid,
        'newdata':f'''
                {{
                    "name":"{name}",
                    "desc":"{desc}",
                    "display_idx":"{displayidx}"
                }}
        '''
    }
    response = requests.put("http://loclhost/api/mgr/sq_mgr/",
                            data=pl,
                            cookies={'sessionid': sessionid})
    retDict = response.json()
    print(retDict)
    return retDict

# 删除课程
def delete_course(courseid,sessionid):
    payload = {
        'action': 'delete_course',
        'id': f'{courseid}'
    }

    response = requests.delete("http://localhost/api/mgr/sq_mgr/",
                               data=payload,
                               cookies={'sessionid': sessionid})

    r = response.json()
    pprint.pprint(r)
    return r
```

case01
```python
from webapi import *

# 先登录
loginRet,cookies = login('auto','sdfsdfsdf')

if loginRet["retcode"] != 0:
    raise Exception('认证失败')

# 记录下sessionid
sessionid =cookies['sessionid']

# 先列出未添加新课程之前的所有课程
courseListBefore = list_course(sessionid)['retlist']

# 添加一门课程
retDict = add_course('js','js语言','6',sessionid)
assert retDict['retcode']==0


# 再列出添加课程后，所有的课程
courseListAfter = list_course(sessionid)['retlist']

createCount = len(courseListAfter) - len(courseListBefore)
assert createCount==1

# 取出多出来的一门课程对象
newcourse = None
for one in courseListAfter:
    if one not in courseListBefore:
        newcourse = one
        break

# 检查是否是刚刚添加的课程
assert newcourse!=None
assert newcourse['name']=='js'
assert newcourse['desc']=='js语言'
assert newcourse['display_idx']==6

# 清除环境操作
delete_course(newcourse['id'],sessionid)

print('\n========= test case pass =============')
```

case02
```python
from  webapi import  *


# 先登录
loginRet,cookies = login('auto','sdfsdfsdf')

if loginRet["retcode"] != 0:
    raise Exception('认证失败')

# 记录下sessionid
sessionid =cookies['sessionid']


# 先添加一门课程
from datetime import datetime
courseName = f'python_{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}'
retDict = add_course(courseName,'python语言','2',sessionid)
assert retDict['retcode'] == 0


# 先列出课程
coureListBefore = list_course(sessionid)['retlist']


# 添加一门课程
retDict = add_course(courseName,'python语言','2',sessionid)
assert  retDict['retcode'] == 0


# 再列出课程
coureListAfter = list_course(sessionid)['retlist']


# 检查课程没有变化
assert coureListBefore == coureListAfter


# 清除环境操作
for one in coureListBefore :
    if one['name'] == courseName:
        delete_course(one['id'],sessionid)

print('\n========= test case pass =============')

```