常用功能：

    jmeter的目录，它执行的东西是依靠左侧目录树，整个测试以测试计划为基础进行测试
    
测试计划：

    用来描述一个性能测试，所有内容都是基于这个计划
    
线程组：

![jmeter](../picture/jmeter5.png)

    一般常用线程组，可以理解成为虚拟用户组(也理解成LR的虚拟用户)
    
    
setup thread group,teardown thread group和线程组没什么区别，但他们有以下两个特点

    * setup thread group: 可用于执行预测试操作。这些线程的行为完全像一个正常的
      线程组元件。类似LR的init元件。
      
    * teardown thread group元件：可用于执行测试后的动作，这些线程的行为完全像一
      个正常的 线程组元件。类似于LR中的end.