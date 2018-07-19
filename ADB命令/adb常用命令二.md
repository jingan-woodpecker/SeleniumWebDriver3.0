    （1）获取手机设备序列号指令：adb get-serialno
    注意：adb get-state指令可用来获取模拟器/设备当前状态
    
 ```sh
 C:\Users\myoffer>adb get-serialno
 27b9a026
 
 C:\Users\myoffer>adb get-state
device
 ```
 
    （2）查看和跟踪系统日志缓冲区的信息指令：adb logcat
    由上至下越来越高的不同级别的日志：
        1、V：冗余级别的日志信息；
        2、D：调试级别的日志信息；
        3、I：信息级别的日志信息；
        4、W：警告级别的日志信息；
        5、E：错误级别的日志信息；
        
    如果只想输出优先级别大于“警告”级别的日志可以输入："adb logcat*:W"
```sh
C:\Users\myoffer>adb logcat*:W
Android Debug Bridge version 1.0.39
Revision 3db08f2c6889-android
Installed as D:\android\AndroidSDK\platform-tools\adb.exe

global options:
 -a         listen on all network interfaces, not just localhost
 -d         use USB device (error if multiple devices connected)
 -e         use TCP/IP device (error if multiple TCP/IP devices available)
 -s SERIAL
     use device with given serial number (overrides $ANDROID_SERIAL)
 -p PRODUCT
     name or path ('angler'/'out/target/product/angler');
     default $ANDROID_PRODUCT_OUT
 -H         name of adb server host [default=localhost]
 ......
```

    Android日志系统并不是所有的消息都被发送到默认缓冲区，可以使用“-b”参数
    选项查看这些附加缓冲区，其中要注意的是：
    1、main：查看主缓冲区相关的消息；
    2、events：查看事件相关的消息；
    3、radio：查看包含无线/电话相关的缓冲区消息。
    
```sh
 C:\Users\myoffer>adb logcat -b main | more
07-19 12:41:53.581   926  1609 I hash_map_utils: key: 'hifi_mode' value: ''
07-19 12:41:53.777 23484 23484 I chatty  : uid=10131(u0_a131) com.tencent.qqlive
 expire 20 lines
07-19 12:41:53.781   732 20670 D audio_hw_extn: audio_extn_get_parameters: retur
ns
07-19 12:41:53.781   732 20670 V msm8974_platform: platform_get_parameters: exit
: returns -
07-19 12:41:53.781   926  1609 I hash_map_utils: key: 'hifi_mode' value: ''
07-19 12:41:53.784 23484 23723 I chatty  : uid=10131(u0_a131) com.tencent.qqlive
 expire 10 lines
07-19 12:41:53.843  5561  5615 I TrafficManageService: mina mTrafficStatsReceive
r onReceive
07-19 12:41:54.703   732 20670 D audio_hw_extn: audio_extn_get_parameters: retur
ns  
-- More  -- 
```

    （3）启动和关闭adb服务的指令：
        adb start-server
        adb kill-server
        
    （4）将本机端口重定向到模拟器或者设备端口上，比如我将本机的9292端口
    重定向到设备的5565端口上，这样所有发往9292端口的数据将会被转发到5565端口上
    "adb forward tcp: 9292 tcp: 5565
    
    （5）pm（package manager）指令：adb shell pm list packages打印所有包信息
    
        1、-d：查看 disabled packages;
        2、-e：查看 enabled package;
        3、-s：查看系统package;
        4、-i：查看package对应安装者；
        5、-u：查看曾被卸载过的package；
        6、-f：查看应用apk的位置跟对应包名
        
        
    

    
 