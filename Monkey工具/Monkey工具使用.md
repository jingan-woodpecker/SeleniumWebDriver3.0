>了解：Monkey（猴子测试）是Android系统自带的一个命令行工具，可在模拟器或真实设备中
运行，Monkey可向被测试应用程序发送**伪随机的用户事件流**（按键、触屏等），主要是用来测
试软件的**稳定性和健壮性**。
    
```sh
C:\Users\myoffer>adb shell monkey
args: []
usage: monkey [-p ALLOWED_PACKAGE [-p ALLOWED_PACKAGE] ...]
              [-c MAIN_CATEGORY [-c MAIN_CATEGORY] ...]
              [--ignore-crashes] [--ignore-timeouts]
              [--ignore-security-exceptions]
              [--monitor-native-crashes] [--ignore-native-crashes]
              [--kill-process-after-error] [--hprof]
              [--match-description TEXT]
              [--pct-touch PERCENT] [--pct-motion PERCENT]
              [--pct-trackball PERCENT] [--pct-syskeys PERCENT]
              [--pct-nav PERCENT] [--pct-majornav PERCENT]
              [--pct-appswitch PERCENT] [--pct-flip PERCENT]
              [--pct-anyevent PERCENT] [--pct-pinchzoom PERCENT]
              [--pct-permission PERCENT]
              [--pkg-blacklist-file PACKAGE_BLACKLIST_FILE]
              [--pkg-whitelist-file PACKAGE_WHITELIST_FILE]
              [--wait-dbg] [--dbg-no-events]
              [--setup scriptfile] [-f scriptfile [-f scriptfile] ...]
              [--port port]
              [-s SEED] [-v [-v] ...]
              [--throttle MILLISEC] [--randomize-throttle]
              [--profile-wait MILLISEC]
              [--device-sleep-time MILLISEC]
              [--randomize-script]
              [--script-log]
              [--bugreport]
              [--periodic-bugreport]
              [--permission-target-system]
              COUNT
```
>上面的"-p"参数指定要运行哪个包，在运行一个包（日历）之前，需要先获取权限并找到对应的包名。

    步骤如下：
    1、adb shell 回车；
    2、su root 回车；
    3、cd data 回车；
    4、cd data 回车；
    5、ls 回车；
    6、找到包名（com.android.calendar）；
       
        
```sh
C:\Users\myoffer>adb shell
HWPRA-H:/ $ su root
HWPRA-H:/ # cd data
HWPRA-H:/data # cd data
HWPRA-H:/data/data # ls
albert.com.mapsdk
android
androidhwext
cn.gov.lottery
cn.wps.moffice_eng
com.android.backupconfirm
com.android.bips
com.android.bluetooth
com.android.bluetoothmidiservice
com.android.calculator2
com.android.calendar
eu.chainfire.supersu
huawei.android.widget
org.simalliance.openmobileapi.service
```

>重新输入"adb shell monkey -p com.android.calendar 400"（发送400次随机事件）成功可看到：网络统计耗时1850ms,耗费在手机上0ms,耗费在无线网络上0ms,浪费在没连接1850ms  
 ```sh
 C:\Users\myoffer>adb shell monkey -p com.android.calendar 400
  bash arg: -p
  bash arg: com.android.calendar
  bash arg: 400
args: [-p, com.android.calendar, 400]
 arg: "-p"
 arg: "com.android.calendar"
 arg: "400"
data="com.android.calendar"
Events injected: 400
## Network stats: elapsed time=1850ms (0ms mobile, 0ms wifi, 1850ms not connecte)
 ```

    查看Monkey执行过程信息指令：添加一个v表示增加一级日志
        1、adb shell monkey -p com.android.calendar -v 400
        2、adb shell monkey -p com.android.calendar -v-v 400
        3、adb shell monkey -p com.android.calendar -v-v-v 400
>示例如下：
    
```sh
C:\Users\myoffer>adb shell monkey -p com.android.calendar -v 50
  bash arg: -p
  bash arg: com.android.calendar
  bash arg: -v
  bash arg: 50
args: [-p, com.android.calendar, -v, 50]
 arg: "-p"
 arg: "com.android.calendar"
 arg: "-v"
 arg: "50"
data="com.android.calendar"
:Monkey: seed=1532123674649 count=50
:AllowPackage: com.android.calendar
:IncludeCategory: android.intent.category.LAUNCHER
:IncludeCategory: android.intent.category.MONKEY
// Event percentages:
//   0: 15.0%
//   1: 10.0%
//   2: 2.0%
//   3: 15.0%
//   4: -0.0%
//   5: -0.0%
//   6: 25.0%
//   7: 15.0%
//   8: 2.0%
//   9: 2.0%
//   10: 1.0%
//   11: 13.0%
:Switch: #Intent;action=android.intent.action.MAIN;category=android.intent.categ
ory.LAUNCHER;launchFlags=0x10200000;component=com.android.calendar/.AllInOneActi
vity;end
    // Allowing start of Intent { act=android.intent.action.MAIN cat=[android.in
tent.category.LAUNCHER] cmp=com.android.calendar/.AllInOneActivity } in package
com.android.calendar
:Sending Touch (ACTION_DOWN): 0:(732.0,1758.0)
:Sending Touch (ACTION_UP): 0:(728.2122,1753.3601)
:Sending Touch (ACTION_DOWN): 0:(70.0,1216.0)
:Sending Touch (ACTION_UP): 0:(62.07508,1236.4476)
:Sending Touch (ACTION_DOWN): 0:(588.0,1030.0)
:Sending Touch (ACTION_UP): 0:(493.43823,1089.8765)
:Sending Touch (ACTION_DOWN): 0:(385.0,1667.0)
:Sending Touch (ACTION_UP): 0:(394.35175,1670.9885)
:Sending Touch (ACTION_DOWN): 0:(338.0,444.0)
:Sending Touch (ACTION_UP): 0:(341.6738,449.71533)
:Sending Trackball (ACTION_MOVE): 0:(0.0,-4.0)
Events injected: 50
:Sending rotation degree=0, persist=false
:Dropped: keys=0 pointers=0 trackballs=0 flips=0 rotations=0
## Network stats: elapsed time=802ms (0ms mobile, 0ms wifi, 802ms not connected)

// Monkey finished
```

    输出内容的分析如下：
    :Monkey: seed=1532123674649 count=50
    seed：指定的随机种子；   count：产生的随机个数；
    
    :AllowPackage: com.android.calendar
    只启动在"com.android.calendar"包中的Activity（活动）
    
    :IncludeCategory: android.intent.category.LAUNCHER
    :IncludeCategory: android.intent.category.MONKEY
    启动的意图重量为"LAUNCHER"和"MONKEY"的活动。
    
    // Event percentages:
    //   0: 15.0%
    //   1: 10.0%
    //   2: 2.0%
    //   3: 15.0%
    //   4: -0.0%
    ...
    本次随机事件中（按键，触屏等）各种类型的事件比例。
    
    :Switch: #Intent;action=android.intent.action.MAIN;category=android.intent.categ
    ory.LAUNCHER;launchFlags=0x10200000;component=com.android.calendar/.AllInOneActi
    vity;end
    跳转到"com.android.calendar"包里面的"ALLInOnActivity"这个活动。
    
    :Sending Touch (ACTION_DOWN): 0:(732.0,1758.0)
    :Sending Touch (ACTION_UP): 0:(728.2122,1753.3601)
    :Sending Touch (ACTION_DOWN): 0:(70.0,1216.0)
    ......
    本次Monkey命令过程中依据前面的随机事件比例而执行的具体随机事件。
    
    Events injected: 50
    产生了50次注入事件。
    
    :Sending rotation degree=0, persist=false
    屏幕旋转相关信息，旋转角度为0，是否保持旋转状态，为假。
    
    :Dropped: keys=0 pointers=0 trackballs=0 flips=0 rotations=0
    屏幕旋转相关丢弃信息：“丢弃:键=0，指针=0，轨迹球=0，键盘轻弹=0，屏幕翻转=0”。
    
    
    
    
    
        