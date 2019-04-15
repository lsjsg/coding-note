# 使用vps搭建个人blog

## 1.创建screen会话

~~~ 
apt-get install screen # 若screen未安装
screen -S lamp
~~~

## 2.下载并安装lamp（linux apache mysql php）

~~~
wget -c http://soft.vpser.net/lnmp/lnmp1.5-full.tar.gz && tar -zxf lnmp1.5-full.tar.gz && cd lnmp1.5-full && ./install.sh lamp
~~~

* 其中MySQL版本，如果内存大小小于1G，则选择5.6以下版本

* InnoDB可随意选择

* php版本为php5.6或php7.0
* Jemalloc和TCmalloc为内存优化，可以选择安装
* 安装需要等待半小时左右
* apache版本建议2.4.33

成功安装lamp后关闭会话

~~~
killall screen 
~~~

## 创建虚拟主机

~~~c
lnmp vhost add
~~~



![æ¬ç¦å·¥ä¸é®å®è£ LNMP æ­å"º WordPress ç½ç"](https://static.banwagongzw.com/wp-content/uploads/2017/11/lnmp-vhost01.png)

这里要输入要添加网站的域名，这里以添加域名www.baidu.com为例（注意替换为自己的域名），输入域名www.baidu.com回车。

![搬瓦工一键安装 LNMP 搭建 WordPress 网站](https://static.banwagongzw.com/wp-content/uploads/2017/11/lnmp-vhost02.png)

这里询问是否添加更多域名，直接输入要绑定的域名，这里假设将baidu.com也绑上，多个域名空格隔开，如不需要绑其他域名就直接回车。

![搬瓦工一键安装 LNMP 搭建 WordPress 网站](https://static.banwagongzw.com/wp-content/uploads/2017/11/lnmp-vhost03.png)

这里需要设置网站的目录，如果没有特殊需要，可以直接回车默认即可。（默认目录：/home/wwwroot/域名）

![搬瓦工一键安装 LNMP 搭建 WordPress 网站](https://static.banwagongzw.com/wp-content/uploads/2017/11/lnmp-vhost04.png)

这里需要设置伪静态规则。设置伪静态可以使URL更加简洁也利于SEO。WordPress是支持的，所以我们输入y回车，然后再输入wordpress回车即可。

![搬瓦工一键安装 LNMP 搭建 WordPress 网站](https://static.banwagongzw.com/wp-content/uploads/2017/11/lnmp-vhost05.png)

这一步是设置日志，如启用日志输入y，不启用输入n回车。

如果启用需要再输入要设置的日志的名称，默认日志目录为：/home/wwwlogs/域名.log，回车确认。

![搬瓦工一键安装 LNMP 搭建 WordPress 网站](https://static.banwagongzw.com/wp-content/uploads/2017/11/lnmp-vhost06.png)

这一步需要询问是否添加数据库和数据库用户。我们输入y，然后回车继续。接下来输入之前设置的MySQL的root密码，输入时不会显示，输入完成后回车，提示OK, MySQL root password correct.则代表输入正确，否则请重新输入。然后需要输入数据库的名字，这里我们需要创建wordpress数据库，所以就输入wordpress然后回车，然后输入这个数据库的密码（不要和MySQL的root密码相同）再次回车。

![搬瓦工一键安装 LNMP 搭建 WordPress 网站](https://static.banwagongzw.com/wp-content/uploads/2017/11/lnmp-vhost07.png)

这里需要选择是否添加SSL证书，这里我们选择n回车继续。

提示Press any key to start create virtul host...后，回车确认便会开始创建虚拟主机。

添加成功会提示添加的域名、目录、伪静态、日志、数据库、FTP等相关信息，如下图：



![搬瓦工一键安装 LNMP 搭建 WordPress 网站](https://static.banwagongzw.com/wp-content/uploads/2017/11/lnmp-vhost08.png)

## 下载并安葬WordPress程序

~~~
wget https://cn.wordpress.org/wordpress-4.9.4-zh_CN.tar.gz
tar -zxvf wordpress-4.9.4-zh_CN.tar.gz
cd Wordpress
mv * /home/wwwroot/www.baidu.com
~~~

然后运行以下命令(注意将/home/wwwroot/www.baidu.com/替换成之前设置的网站目录)

~~~
chown www:www -R /home/wwwroot/www.baidu.com
~~~

提示chown: changing ownership of `/home/wwwroot/www.baidu.com/.user.ini': Operation not permitted，不用管。

LNMP1.4默认关闭scandir函数，可以使用

~~~
sed -i 's/,scandir//g' /usr/local/php/etc/php.ini && lnmp php-fpm restart
~~~

来解决更新问题

## 登陆自己的博客进行设置

数据库名为之前所建数据库名

用户名也是之前的用户名

密码

主机为localhost

表前缀为wp



reference:

https://www.seoimo.com/wordpress-vps/

https://www.banwagongzw.com/17.html