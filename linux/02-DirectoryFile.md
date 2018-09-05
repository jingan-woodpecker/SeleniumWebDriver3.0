目录文件
    
    （1）
    *在linux中所有的文件和目录都组织成一个以根节点开始的倒置的树状结构；
    *目录相当于windows中的文件夹，目录中存放的既可以是文件，也可以是其它的子目录；
    *顶层根目录使用左斜杠"/"
    
    （2）
    . 表示当前目录，即用户所在的工作目录
    .. 表示父目录，即当前目录的上一层目录
    cd.   或者   cd..   pwd显示你在哪个目录  
    补充ls -a显示隐藏文件  lsa
    
    (3)
    先输入ls /   可以看出里面的bin目录
    再输入ls /bin/  命令，就会显示一系列可执行文件
    所以bin目录是用来存放常用的可执行文件
    
    (4)
    输入ls /sbin/命令进行查看，可以看出sbin目录是用来存放系统的可执行文件的
    
    (5)
    家目录：用来存放用户自己的文件或目录，其中超级用户root的家目录是/root(可用ls /root/查看),
          普通用户的家目录被存放在/home目录下，并使用用户名作为最后一级目录的名称(例如：tom用户的家目录/home/tom),新建的用户查看时可加上ls -a
          
    (6)
    dev目录：设备文件目录(ls /dev/进行查看)
    
    (7)
    etc目录：配置文件目录
    补充可随意使用的目录： mmt目录，opt目录， media目录 ， tmp临时目录
    挂载点(目录)：通常可移除式硬件会被挂载在/media或/mnt目录之下
    
路径

    a  绝对路径：必须以一个正斜线（/）开始。绝对路径包括从文件系统的根节点开始到要查找的对象（目录或文件）
               所必须遍历的每一个目录的名字，它是文件位置的完整路标，因此在任何情况下都可以使用绝对路径找到所需的文件。
               
    b  相对路径：不是以正斜线（/）开始，相对路径可以包含从当前目到要查找的对象（目录或文件）所必须遍历的每一个目录的名字

    