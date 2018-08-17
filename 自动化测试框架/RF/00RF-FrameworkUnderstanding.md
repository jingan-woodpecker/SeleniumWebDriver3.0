Robot Framework 

    1、通用型的自动化测试框架
        *组织自动化脚本
        *选择测试脚本执行(批量执行或指定执行)
        *测试结果中清晰的反馈每个测试脚本，各个脚本是否通过
        *执行的结果以容易查看的报告形式提交给别人查阅
        
        *自动测试用例的实例方法
        *自动测试用例的开发支持(IDE、ku)
        *和用例管理系统的集成(禅道)
        *测试执行--->相关测试套件和测试用例执行的规则
                    初始化和清除
                    测试报告
                    
    2、结构
            自动测试用例数据文件
            
            Robot Framework 
                                -------->   被测系统
            测试库
            
            测试工具1  测试工具n
            
     *测试人员开发测试数据文件(Test Data)对应一个个测试用例
     *测试数据文件里面使用的功能小模块叫"关键字",由测试库(Test Library)实现
     *Robot Framework加载测试库，并解释执行测试用例
     
    3、特点
        （1）以关键字的形式来开发测试用例
            *标准库提供了常用的功能
            *第三方扩展库
            *开发者根据产品自行开发库
                自动化测试框架、库开发者
                自动化用例开发者
                
        （2）定义了灵活且易理解的测试用例执行控制（包括初始化和清除环境）
        （3）清晰的日志和报表功能，可以清除的查看测试执行结果
RF的安装

    RF的安装：pip install robotframework
    
    RIDE的安装（一般不用）
        *简单的IDE
        *提供了RF自动化测试用例的可视化的编辑功能 pip install robotframework-ride
        *wxpython的安装---RIDE依赖wxpython的图形库2.8.12.1
        
    seleniumlibrary的安装
        *支持selenium自动化的RF扩展库
        *pip install --upgrade robotframework-seleniumlibrary
        
        安装插件使代码高亮显示(IntelliBot)
        
    SeleniumLibrary文档网址：robotframework.org/SeleniumLibrary/SeleniumLibrary.html
    标准库网址：robotframework.org/#libraries
    
套件（数据文件）文件中的表

    RF支持四种的表
        *分别为Settings, Variables, Test Cases, Keywords
        *表名必须出现在第一个单元格中，表名大小写不敏感
        
    一、Settings表，是这个测试套件的全局配置表，比如，说明这个测试套件要使用的测试库，资源文件，测试
    套件的环境初始化（setup）和清除（teardown），该套件内的标签等
    二、Variables表------->测试套件全局变量表
    三、Test Cases表------>定义这个测试套件的测试用例
    四、Keywords表-------->定义测试套件的用户关键字
        
测试用例表语法

    测试用例表里面的每个测试用例大概可以分为：
        *配置部分
        *主体部分
    用例配置部分
        *[Documentation]
        该用例的文字说明
        *[Tags]
        该用例的标签
        *[Setup],[Teardown]
        该用例的初始化和清除操作
        *[Template]
        声明该用例是模板关键字驱动的
        *[Timeout]
        设置用例超时时间
    用例的主体部分主要由关键字组成
    *关键字的来源
        测试库
        资源文件
        用例所在的文件的关键字表
    *用例的主体部分也包含变量赋值
    
常用关键字

    *Import Library
    
    *Should Be Equal
        Should Be Equal  10  010    当做是字符串进行比较，所以结果是False
        Should Be Equal As Integer  10   010     这就把其转换成数字对象进行比较，结果为True
        
    *Should Contain
    
    *set variable
        ${var}   set variable   ${EMPTY}   设置空字符串
        
    *log to console  打印在控制台
        log to console 32  表示字符串’32’
        log to console ${32}  表示数字32
        
    *log 
    *sleep
    *Convert To Integer  转换成字符串
    
    *Convert To Number   转换成浮点数
    
    *Should Be True
       ${str1} =  set varuabke  hello
       Should Be True  $str1=='hello'
        
    *eval        动态输入合法表达式
        exp = input('请输入表达式:')
        print(eval(exp))
        