 >（1）保证每次执行的**事件、序列是一致的**，用来复现问题，可使用"-s"参数
 >指定伪随机数生成器的seed（种子）值，如果seed值相同，事件序列就相同。
    
    **注意：最好每次执行测试都应该记录使用的命令以及用管道命令保存输出结果到文件**
    示例如下：
```sh 
adb shell monkey -p com.android.calendar -v 30 > D:\Monkey\log.txt
```   

>（2）"-p"参数用于约束限制，可指定**一个**或**多个**包（package)对应启动，若不指定则随机打开包
```sh
adb shell monkey -p com.android.calendar-p com.tencent.mobileqq
```

>（3）"--throttle"参数用来指定随机事件间的**延时**（单位：毫秒）
>>比如：向腾讯QQ应用发送50次随机事件，每次间隔3秒钟。
```sh
adb shell monkey -p com.tencent.mobileqq --throttle 3000 50
```

>（4）"--pct-touch <percent>"参数用于设置**触屏事件**生成的百分比
>>比如：向淘宝应用发送50次随机事件，每次事件间隔为3秒，触屏事件占比40%。
```sh
adb shell monkey -p com.taobao.taobao --pct-touch 40 --throttle 3000 50
```

>（5）"--pct-motion <percent>"参数用于设置**滑动事件**生成的百分比
>>比如：向email应用发送50次随机事件，每次事件间隔为3秒，滑动事件占比40%。
```sh
adb shell monkey -p com.android.email --pct-motion 40 --throttle 3000 50
```

>（6）"--pct-trackball <percent>"参数用于设置**轨迹球**(一系列随机移动和单击的事件)事件生成的百分比
>>比如：向腾讯新闻应用发送50次随机事件，每次事件间隔为3秒，轨迹球事件占比40%。
```sh
adb shell monkey -p com.tencent.news --pct-trackball 40 --throttle 3000 50
```

>（7）"--pct-nav <percent>"参数用于设置**基本导航**(向上、向下、向左、向右)事件生成的百分比
>>比如：向腾讯新闻应用发送50次随机事件，每次事件间隔为3秒，基本导航事件占比40%。
```sh
adb shell monkey -p com.tencent.news --pct-nav 40 --throttle 3000 50
```

>（8）"--pct-majornav <percent>"参数用于设置**主要导航**(Back键、Menu键)事件生成的百分比
>>比如：向中国体育彩票应用发送50次随机事件，每次事件间隔为3秒，主要导航事件占比40%。
```sh
adb shell monkey -p com.gov.lottery --pct-majornav 40 --throttle 3000 50
```

>（9）"--pct-syskeys <percent>"参数用于设备**系统按键**(拨号、音量、Home)事件生成的百分比
>>比如：向腾讯新闻应用发送50次随机事件，每次事件间隔为3秒，系统按键事件占比40%。
```sh
adb shell monkey -p com.tencent.news --pct-syskeys 40 --throttle 3000 50
```

>（10）"--pct-appswitch <percent>"参数用于设备**系统启动**(Activity)事件生成的百分比
>>比如：向腾讯新闻应用发送50次随机事件，每次事件间隔为3秒，启动活动事件占比40%。
```sh
adb shell monkey -p com.tencent.news --pct-appswitch 40 --throttle 3000 50
```

>（11）"--pct-anyevent <percent>"参数用于设备**系统其它类型**(普通按键、不常用设备按钮)事件的百分比
>>比如：向腾讯新闻应用发送50次随机事件，每次事件间隔为3秒，其它类型事件占比40%。
```sh
adb shell monkey -p com.tencent.news--pct-trackball 40 --throttle 3000 50
```

>（12）"--hrop"指定了该参数，Monkey会在发送事件序列的前后，**生成性能测试报告**。通常会在"data/misc"
目录下生成一个5MB左右大小的文件


    （13）"--ignore-crashes "参数可在**程序崩溃或发生异常**后继续向系统发送事件，直到全部发送完成
    比如：向日历应用发送100次随机事件测试过程中即使程序崩溃，依然会发送事件直到100为止。
```sh
adb shell monkey -p com.android.calendar --ignore-crashes 100
```

>（14）"--ignore-timeouts"参数可在程序发生**超时错误**继续向系统发送事件，直到全部发送完成
 >>比如：向日历应用发送100次随机事件测试过程中即使程序出现ANR错误，依然会发送事件直到100为止。
```sh
adb shell monkey -p com.android.calendar --ignore-timeouts 100
```
>（15）"--ignore-security-exceptions"参数可在程序发生**访问权限**问题继续向系统发送事件，直到全部发送完成
 >>比如：向日历应用发送100次随机事件测试过程中即使出现证书许可错误或网络许可错误等，依然会发送事件直到100为止。
```sh
adb shell monkey -p com.android.calendar --ignore-security-exceptions 100
```
>（16）"--kill-process-after-error"参数，当Monkey由于一个错误而停止时，出错的应用程序将继续处于运行状态。
当设定了此参数后，它将通知系统停止发生错误的进程。

>（17）"--monitor-native-crashes"参数，可**监视并报告**Android系统中本地代码的崩溃事件。如果设置了此参数，系统
将停止运行。

>（18）"--wait-dbg"参数，启动Monkey后，先中断其运行，等待调试器和它相连接。

```sh
adb shell monkey --ignore-crashes --ignore-timeouts --kill-process-after-error --ignore-
security-exceptions --throttle 2000 -v -s 6 500
```
>上述综合示例的命令指的是：向系统发送500次随机事件，各个随机事件的时间间隔是2秒，种子是6，测试过程中
应用程序忽略相关的安全、超时、崩溃等异常。

