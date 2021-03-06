1、接口的定义

    * 接口泛指实体把自己提供给外界的一种抽象化物(可以为另一实体)，用以由内部操作
      分离出外部沟通方法，使其能修改内部而不影响外界其它实体与其交互的方式。
      
    * 人类与电脑等信息机器或人类与程序之间的接口称为用户界面，电脑等信息机器硬件
      组件间的接口叫硬件接口，电脑等信息机器软件组件间的接口叫软件接口
      
    * 类似我们黑盒测试功能，即内部具体结构你不知道，但你需要知道我输入什么，之后
      输出什么才是对的，什么才是错的。
      
2、HTTP请求与响应

    get请求：获取资源 ， post请求：数据提交
    
post 和 get区别：
    
    GET后退按钮/刷新无害，POST数据会被重新提交（浏览器应该告知用户数据会被重新提交）。
    GET书签可收藏，POST为书签不可收藏。
    GET能被缓存，POST不能缓存 。
    GET编码类型application/x-www-form-url，POST编码类型encodedapplication/x-www-form-urlencoded 或 multipart/form-data。为二进制数据使用多重编码。
    GET历史参数保留在浏览器历史中。POST参数不会保存在浏览器历史中。
    GET对数据长度有限制，当发送数据时，GET 方法向 URL 添加数据；URL 的长度是受限制的（URL 的最大长度是 2048 个字符）。POST无限制。
    GET只允许 ASCII 字符。POST没有限制。也允许二进制数据。
    与 POST 相比，GET 的安全性较差，因为所发送的数据是 URL 的一部分。在发送密码或其他敏感信息时绝不要使用 GET ！POST 比 GET 更安全，因为参数不会被保存在浏览器历史或 web 服务器日志中。
    GET的数据在 URL 中对所有人都是可见的。POST的数据不会显示在 URL 中。


http请求（由请求头，请求体组成）

    请求头：设置请求类型(json和非json)
    请求体：请求参数
    
get请求：主要关注

    是否是get方式请求，请求参数，请求地址
    
post请求：主要关注

    post一般都有请求参数，请求地址
    
响应的组成 (响应由响应头和响应体组成)

    * 状态行(200,404,500)
    * 消息报头
    * 空行
    * 响应正文(响应体)
    
状态代码有三位数字组成，第一个数字定义了响应的类别，且有五种可能取值：

    1xx：指示信息–表示请求已接收，继续处理
    2xx：成功–表示请求已被成功接收、理解、接受
    3xx：重定向–要完成请求必须进行更进一步的操作
    4xx：客户端错误–请求有语法错误或请求无法实现
    5xx：服务器端错误–服务器未能实现合法的请求
    
常见状态代码、状态描述、说明：

    200 OK     //客户端请求成功
    400 Bad Request  //客户端请求有语法错误，不能被服务器所理解
    401 Unauthorized //请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用
    403 Forbidden  //服务器收到请求，但是拒绝提供服务
    404 Not Found  //请求资源不存在，eg：输入了错误的URL
    500 Internal Server Error //服务器发生不可预期的错误
    503 Server Unavailable  //服务器当前不能处理客户端的请求，一段时间后可能恢复正常
    eg：HTTP/1.1 200 OK （CRLF）

