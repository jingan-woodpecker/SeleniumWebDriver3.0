系统管理命令： ps -aux

    ps命令可以查看进程的详细进程
    
    选项                         含义
     -a                          显示终端上所有进程，包括其他用户的进程
     -u                          显示进程的详细状态
     -x                          显示没有控制终端的进程
     -w                          显示加宽，以便显示更多的信息
     -r                          只显示正在运行的进程   
     
top命令

    用来动态显示运行中的进程。top命令能在运行后，在指定的时间间隔更新显示信息。
    可以在使用top命令时加上-d来指定显示信息更新的时间间隔。
    在top命令执行后，可以按下按键得到对显示的结果进行排序：
    
    按键                       含义
     M                         根据内存使用量来排序
     P                         根据CPU占有率来排序
     T                         根据进程运行时间的长短来排序
     U                         可以根据后面输入的用户名来筛选进程
     K                         可以根据后面输入的PID来杀死进程
     q                         退出
     h                         获得帮助
     
终止进程

    kill和killall
    
    例如杀掉进程号为3986的 ---->  kill -9 3986
    
关机重启

    reboot、 shutdown、 init0
    
检查磁盘空间： df

    用于检测文件系统的磁盘空间占用和空余情况，可以显示所有文件系统对节点和磁盘块的使用情况
    
    选项                         含义
     -a                          显示所有文件系统的磁盘使用情况
     -m                          以1024字节单位显示
     -t                          显示各指定文件系统的磁盘空间使用情况
     -T                          显示文件系统
     
查看或配置网卡信息

    ifconfig
    
![ifconfig](../picture/ifconfig.png)
    
    重启整台机器网络的命令： service network restart
   
测试远程主机连通性

    ping
    只ping一次的命令：  ping -c1 www.baidu.com
    
查看网络情况

    netstat-ntpt
    
tar 解压或者压缩(z:表示压缩格式，c：压缩的意思，v:显示压缩的时候的详细情况)

    例如：将"x"目录压缩成名称为"x.tar.gz" 且格式为"gz"的压缩包，命令如下
    [root@localhost home]# tar -zcvf x.tar.gz x/

![tar](../picture/tar.png)    

    解压包的命令(x:表示解压) tar -zxvf x.tar.gz
    
![tarx](../picture/tarx.png)

    