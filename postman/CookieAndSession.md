    cookie是什么？
        *cookie是我们在访问一个网站时，通常由网站服务器返回的一种标记为cookie类型数据
        *要求我们存储在浏览器所在电脑上
        *以后每次访问本网站，浏览器都会在http请求中将该数据发送过来
        
        session (比如用户登录就会携带sessionid,然后在服务器查找看是否存在)有效期看服务端的设置
        cookie是保存任何数据的机制，session只是其中一种数据
        
     sesssion弊端当存储数据太大，磁盘读写就会变慢，产生性能瓶颈，查看数据就会损耗很长时间
     当数据过多需要水平扩容数据库的时候，复杂度较大，需要保持数据同步
     
     token概念
        token包含数据信息(data)和验证信息(HMAC)
        *Hash算法产生Token
        *数据信息改变、验证信息也会改变，HMAC算法
        *HmacFunc(密钥+data)=HHMAC