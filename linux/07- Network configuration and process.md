1、创建虚拟机

![centos](../picture/centos1.png)

    此处选择稍后安装操作系统。然后点击下一步。
    
![centos](../picture/centos2.png)

    选择Linux后，点击下一步

![centos](../picture/centos3.png)

    设置好名称和位置，这个位置就是你以后再次打开虚拟机时，所需要用到的地址，所以请记牢。点击下一步。

![centos](../picture/centos4.png)

    点击自定义硬件，进行虚拟机硬件配置。

![centos](../picture/centos5.png)

    内存最少要选择628MB，建议选择1G。CPU建议配置2核。  

![centos](../picture/centos6.png)

    光驱此处选择使用ISO映像文件，选择我们已下载ISO的存储路径；其他配置项均默认即可

![centos](../picture/centos7.png)

2、安装操作系统

    开启虚拟机
![centos](../picture/centos8.png)

    等待
![centos](../picture/centos9.png)

    选择语言，我们这里将鼠标拉到页面底部，选择中文，点击继续。
    
![centos](../picture/centos10.png)

    在设置首页，向下滑动至系统选项，选择安装位置

![centos](../picture/centos11.png)

    选中磁盘，点击“我要配置分区”后，点击完成

![centos](../picture/centos12.png)

    在手动分区页面，进行如下设置

    点击加号按钮，弹出选择挂载点框，首先添加一个swap分区，容量输入2048，点击添加挂载点。
    
![centos](../picture/centos13.png)

    同样方法，再次点击加号，添加根分区，挂载点选择/，大小输入可用空间容量即可（粉红按钮里显示的，比如输入16GB），点击添加挂载点。

    最后，再添加一个/boot分区，将添加的3个分区的设备类型都设置为标准分区：
    
![centos](../picture/centos14.png)

    点击左上角的完成按钮，会弹出一个页面，点击接收更改即可
    
![centos](../picture/centos15.png)

    配置网络和主机名
    设置页面，点击网络和主机名
    
![centos](../picture/centos16.png)

    由于我们的网络是NAT模式，它会通过DHCP自动获取IP，我们把网络开启，点击左上角完成。
    返回设置页面后，点击右下角的开始安装即可。
    
![centos](../picture/centos17.png)  

    设置用户名和密码
    点击root密码，进行root用户的密码设置。
    
![centos](../picture/centos18.png) 

    安装完成后，点击重启等待即可，不需要进行任何操作！。
    设置root用户密码
    安装完成后，点击重启等待即可，不需要进行任何操作！。
    
![centos](../picture/centos19.png)

![centos](../picture/centos20.png)

    安装成功页面
    
![centos](../picture/centos21.png)

3、虚拟机网络配置

    下面我们配置一下我们虚拟机的网络。关闭操作系统后，再次在主页，打开虚拟机。
    
![centos](../picture/centos22.png)

    虚拟机的打开路径即在安装过程中，设置的路径，见安装过程中设置的路径。选择.vmx打开即可。
    
![centos](../picture/centos23.png)    

    在下面的界面中，设置网络适配器为桥接模式（因为以后我们需要用xshell连接我们的虚拟机，所以需要让虚拟机有一个自己单独的局域网IP。
    其中，NAT模式和我们的本机共享IP，不适用。），再次开启虚拟机，就可联网了。

![centos](../picture/centos24.png)   
    
4、linux常用软件下载

    由于我们安装的是最小软件包，所以很多软件都需要我们手动去安装
    安装ifconfig命令
    用ifconfig命令来查看虚拟机ip，这时需要安装包含这个命令的软件包；
    
    通过yum search 这个命令发现ifconfig这个命令是在net-tools.x86_64这个包里，我们安装这个包就行了。安装过程中，默认输入y，回车。
    安装命令： yum install net-tools.x86_64
    
![centos](../picture/centos25.png)

![centos](../picture/centos26.png)

![centos](../picture/centos27.png)

5、添加硬盘

![centos](../picture/centos28.png)

    sdb 表示新的磁盘，fdisk表示分区
    
![centos](../picture/centos29.png)

了解：

    扩展文件格式化分区命令： [root@localhost dev]# mkfs.ext4 /dev/sdb1  (注意每个分区都要格式化最好)
    挂载的命令(先建立一个目录用来存放)：
      在opt下创建一个my_disk目录
     [root@localhost dev]# mkdir /opt/my_disk
      将分区挂载到my_disk目录中
     [root@localhost dev]# mount /dev/sdb1 /opt/my_disk
     进入到my_disk中
     [root@localhost dev]# cd /opt/my_disk/
     [root@localhost my_disk]#ls
     lost_found

查看或配置网卡信息

    ifconfig
   
测试远程主机连通性

    ping
    
查看网络情况

    netstat-ntpt
    
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
    
关机重启

    reboot、 shutdown、 init
    
检查磁盘空间： df

    用于检测文件系统的磁盘空间占用和空余情况，可以显示所有文件系统对节点和磁盘块的使用情况
    
    选项                         含义
     -a                          显示所有文件系统的磁盘使用情况
     -m                          以1024字节单位显示
     -t                          显示各指定文件系统的磁盘空间使用情况
     -T                          显示文件系统
     
检查目录所占磁盘空间： du

    用于统计目录或文件所占磁盘空间的大小，该命令执行的结果与df类似， du更侧重于磁盘的使用情况
    du命令的使用格式： du[选项] 目录或文件名
    
    选项                          含义
     -a                           递归显示目录或文件和子目录中文件占用数据块
     -s                           显示指定文件或目录占用的数据块
     -b                           以字节为单位显示磁盘占用情况
     -l                           计算所有文件大小，对硬链接文件计算多少次
     
tar 解压或者压缩
 
yum install lrzsz  上传文件rz


         

