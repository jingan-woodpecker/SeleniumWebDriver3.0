Postman使用

    不仅仅是测试工具，API开发支持
        *构建API
        *Mock Server
        *开发文档自动生成
        
安装的两种形式：

    1、本地的应用程序(https://www.getpostman.com/apps)
    2、Chrome浏览器的插件(有限制，不建议使用)
    
![postman](../picture/post.png)

![postman](../picture/post01.png)

**构建HTTP请求**

    Postman可以快速构建HTTP请求
    参与构造的部分主要是
        *Method(请求方法)
        *URL-----(1)URL参数query string; (2)encodeURICompoent
        *Headers(请求头)
        *消息体
            1、application/x-www-form-urlencoded
            2、application/json(序列化)
            3、application/xml
            4、multipart/form-data
            5、其它
    