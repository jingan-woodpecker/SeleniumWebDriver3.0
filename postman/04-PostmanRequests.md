Python requests库(查看文档：http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)
    
    *特点：简便易用、功能强大
    *安装
    *请求的构建：method、url、header、body
    *响应的查看
    

1、请求方法使用：
    
    *导入requests模块；
    *获取某个网页
    
```python
# 请求方法的使用：用data参数说明放在消息体中
import requests

r1 = requests.get('https://api.github.com/events')
r2 = requests.put('http://httpbin.org/put',data = {'key':'value'})
r3 = requests.delete('http://httpbin.org/delete')
r4 = requests.post('http://httpbin.org/post', data = {'key':'value'})
```

2、URL参数的使用：

    *方法一：可以数据键值对形式置于URL中，跟在一个问号后面
    *方法二：使用params关键字参数，以一个字符串字典来提供这些参数

```python
# 参数的使用:使用params参数说明放在urlencode中
import requests,pprint

# 方法一
r1 = requests.get("http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20")
pprint.pprint(r1.json())

# 方法二
params = {'action':'list_course', 'pagenum':'1', 'pagesize':'20'}
r = requests.get("http://localhost/api/mgr/sq_mgr/", params=params)
pprint.pprint(r.json())
```

3、定制请求头的使用：

    传递一个dict给headers参数即可
    注意: 定制 header 的优先级低于某些特定的信息源，例如：

    如果在 .netrc 中设置了用户认证信息，使用 headers= 设置的授权就不会生效。而如果设置了 auth= 参数，``.netrc`` 的设置就无效了。
    如果被重定向到别的主机，授权 header 就会被删除。
    代理授权 header 会被 URL 中提供的代理身份覆盖掉。
    在我们能判断内容长度的情况下，header 的 Content-Length 会被改写。
    更进一步讲，Requests 不会基于定制 header 的具体情况改变自己的行为。只不过在最后的请求中，所有的 header 信息都会被传递进去。

    注意: 所有的 header 值必须是 string、bytestring 或者 unicode。尽管传递 unicode header 也是允许的，但不建议这样做。
    
```python
# 定制请求头
import requests

headers = {'user':'jingan',
           'password':'123456'}
response = requests.get("http://localhost/api/mgr/sq_mgr/", headers=headers)

rj =response.text
print(rj)
```

4、复杂的post请求及响应内容

    你想要发送一些编码为表单形式的数据——非常像一个 HTML 表单。要实现这个，只需简单地传递一个字典给 data 参数。
    你的数据字典在发出请求时会自动编码为表单形式：
    
x-www-form-urlencoded格式

```python
# 复杂post请求（x-www-form-urlencoded）转换为json格式对象，方便数据处理
import requests

pl = {
    'action': 'add_course',
    'data' : '''
            {
                "name":"php",
                "desc":"php课程",
                "display_idx":"3"
            }'''
}

response = requests.post("http://localhost/api/mgr/sq_mgr/",data=pl)
ret=response.json()

if ret['retcode'] == 0:
    print("pass")
else:
    print("error")
```

json格式

```python
# 复杂post请求
import requests

payload = {
  "action" : "add_course_json",
  "data"	 : {
    "name":"初中数学",
    "desc":"初中数学课程",
    "display_idx":"4"
  }
}
response = requests.post("http://localhost/apijson/mgr/sq_mgr/", json=payload)

rj =response.text
print(rj)
```