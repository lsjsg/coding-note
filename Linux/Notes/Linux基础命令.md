# Linux基础命令

## 文件管理

### ls

列出指定目录下的内容

`ls [OPTION]… [FILE]…`

`ls -a` 可以用来查看隐藏文件

`ls -A` 显示除..之外的所有文件

`ls -l` 长格式列表，显示文件的详细属性信息

` ls -h` 把文件大小单位换算，换算后可能会是非精确值

`ls -d` 看目录自身而非其内部文件列表

` ls -r`逆序显示

`ls -R` 递归显示

`ls -t` 显示最后一次修改的文件

`ls -lh` 改变文件详细信息中文件大小的显示格式, 使其更具有可读性

`ls -i`  显示文件的inode信息

### pwd

显示当前工作目录

### cd

我们用`cd ..` 来返回上一级目录, 同时可使用`cd ../file/`来进入上一级目录下的某一目录

`cd ~`切回自己的/home目录, 波浪线~表示家目录(root用户的家目录是/root)

`cd ~ USERNAME` 切换到指定用户的家目录

`cd -` 上一次所在的目录与当前目录之间来回切换

### touch

用于创建一个新文件或修改文件时间戳

`touch [OPTION]… FILE…`

`touch -c`   指定的文件路径不存在时不予创建

`touch -a`   仅修改访问时间access time

`touch -m`  仅修改modify time（文件内容修改）

`touch -t`   使用指定的日期时间，而非现在的时间

## cp

单源复制：`cp [OPTION]… [-T] SOURCE DEST`

多源复制：`cp [OPTION]… SOURCE… DIRECTORY`

`cp -i`：交互式复制，即覆盖之前提醒用户确认；

`cp -f`：强制覆盖目标文件；

`cp -r` ` cp -R`：递归复制目录；

`cp -d`：复制符号链接文件本身，而非其指向的源文件；

`cp -a`：用于实现归档；

`cp -p` 不跟随源文件中的符号链接

`cp -r` 递归循环复制一个目录t

### mkdir 

`mkdir -p`  通俗地说对于不存在的父和子目录一起创建出来

`mkdir -v` 显示过程

`mkdir -m` 直接给定权限

## mv

`mv [OPTION]… [-T] SOURCE DEST`

`mv [OPTION]… SOURCE… DIRECTORY`

`mv [OPTION]… -t DIRECTORY SOURCE…`

`mv file dire` 移动一个文件

`mv file1 file2` 重命名文件

`mv -f` 强制移动

`mv -i` 交互式

## rm

`rm -r` 递归删除目录下的所有文件

`rm -f` 强制删除

`rm -i` 交互

通常为了防止误删文件可以将文件先移动到某个目录然后类似于回收站定期删除

## file

`file` 查看文件类型, 需要什么类型的程序来运行它

## 权限管理

## su

`su - jack` 可以直接从超级用户切换为用户jack

`sudo su`则是由普通用户切换到root用户

### chmod



## 开关机类命令

### shutdown 

`shutdown[OPTIONS…][TIME]`

`shutdown -r`  关机后重启

`shutdown -h` 将系统关机

`shutdown -c`  取消关机

`shutdown -h now` 表示立即关机

 `shutdnow  +30` 30分钟后关机

### halt

停止系统运行但不关闭电源

### poweroff 

关闭系统并且切断电源

### reboot 

用来重新启动正在运行的Linux操作系统

## 文件查看类命令

## cat 

查看文本内容

`cat -n` 给每行编号，包括空行

`cat -E` 显示空格符，包括空行

### tac

将文件以行为单位反序输出，最后一行先显示

### less

按一下回车键往文件尾部查看一行，按空格键往文件尾部翻一屏

按pageup和pagedown键前后翻屏，按上下箭头可以上下翻一行

### more

从头到尾查看文件，不可以回头

### head

显示文件的前n行，默认是显示前十行

-c<字节> 显示字节数。  head  -c 50 /etc/rc.d/init.d/functions 显示前50字节，要是改为-50.则显示文件后50字节。

-n<行数> 显示的行数。显示文件的前50行：head  -50 /etc/rc.d/init.d/functions

### tail

显示指定文件末尾内容，不指定文件时，作为输入信息进行处理。常用查看日志文件。

`tail -n`  ：查看文件尾部n行

`tail -f`：查看文件尾部内容结束后不退出，接着显示更新的行。





## Important directories 

**In Linux the name of the files are shorter than 255 characters, and can use any other symbols except / When you name it, prevent from using *and the brackets or else it maybe troublesome to delete them.** 

/usr is the short for Unix system resources

To save the files related to the programs we have installed

/bin is the short for binary, where the binary code can be executed. 





 





