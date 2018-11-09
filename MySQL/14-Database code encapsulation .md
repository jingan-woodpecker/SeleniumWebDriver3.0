数据库代码封装

```python
import pymysql

class MysqlHelper(object):
    # 这个是写在专门的文件中的，要改变代码就在config文件中修改
    # 类属性config
    config = {
        "host":"localhost",
        "user":"root",
        "password":"Lja199514*",
        "db":"test1",
        "charset":"utf8"
              }
    def __init__(self):
        self.connection = None
        self.cursor = None

    #该函数专门从数据库表中查询一行数据的,第一个参数传入sql语句，第二个参数为元组
    def getone(self,sql,*args):
        try:
            #把connection当成对象的属性,创建数据库连接
            # 类名.属性名调用类属性
            self.connection = pymysql.connect(**MysqlHelper.config)
            #创建cursor
            self.cursor = self.connection.cursor()
            #执行sql语句
            self.cursor.execute(sql,args)
            return self.cursor.fetchone()
        except Exception as ex:
            print(ex)
        finally:
            self.close()

    # 该函数专门从数据库表中查询多行数据的
    def getlist(self, sql, *args):
        try:
            # 把connection当成对象的属性,创建数据库连接
            self.connection = pymysql.connect(**MysqlHelper.config)
            # 创建cursor
            self.cursor = self.connection.cursor()
            # 执行sql语句
            self.cursor.execute(sql, args)
            return self.cursor.fetall()
        except Exception as ex:
             print(ex)
        finally:
            self.close()

    # 对数据库进行增，删，改
    def executeDML(self, sql, *args):
        try:
             # 把connection当成对象的属性,创建数据库连接
            self.connection = pymysql.connect(**MysqlHelper.config)
            # 创建cursor
            self.cursor = self.connection.cursor()
            # 返回sql语句执行后影响的行数
            num = self.cursor.execute(sql, args)
            self.connection.commit()
            return num

        except Exception as ex:
            self.connection.rollback()
            print(ex)
        finally:
            self.close()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

if __name__=="__main__":
    helper = MysqlHelper()
    print(helper.executeDML("delete from dept where deptno=%s"%(50)))
```