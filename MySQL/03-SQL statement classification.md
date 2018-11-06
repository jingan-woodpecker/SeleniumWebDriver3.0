1、SQL(Structured Query Language)介绍

        是一种特殊目的的编程语言，是一种数据库查询和程序设计语言
    用于存储数据以及查询、更新和管理关系数据库系统。
    
2、SQL可以做什么

    * 数据库数据的增删改查(CURD)
    * 数据库对象的创建，修改和删除
        数据库对象(创建数据库、创建表、创建关系、创建约束、创建索引)
    * 用户权限的授予和取消(grant)
    * 事物控制
    
3、SQL语句分类

    * DQL(数据查询语言)---重点
        select
    * DML(数据操作语言)
        insert、update、delete
    * DDL(数据定义语言)
        create、drop、alter
    * DCL(数据控制语言)
        grant、revoke
    * TCL(事物控制语言)
        SAVEPOINT、ROLLBACK、SET TRANSACTION、COMMIT
        
4、数据库操作(ddl---database DecorationDefined language )

    * 创建数据库
    creat database 数据库名 charset=utf-8;
    
    * 删除数据库
    drop database 数据库名;
    
    * 切换数据库
    use database;
    
    * 查看当前选择的数据库
    select database();
    
表操作(ddl)

    * 查看当前数据库中所有表
    show tables;
    
    * 创建表
    * auto_increment 表示自动增长
    create table 表名(列及类型)
    
    比如：
    create table student(id int auto_increment primary key,
    sname varchar(10) not null);
    
    (字段 字段类型 约束条件 , 字段 字段类型 约束条件，...)
    用图形界面创建的表可以右键选择对象信息，下方选择DDL查看SQL语句
    "-- "后面可以写注释内容
    
    * 修改表
    alert table  表名 add|change|drop 列名 类型;
    比如： alert table student add birthday datetime 
    
    * 删除表
    drop table 表名
    
    * 查看表结构
    desc 表名
    
    * 更改表名称
    rename table 原表名 to 新表名
    
    * 查看表的创建语句
    show create table '表名'
    
    