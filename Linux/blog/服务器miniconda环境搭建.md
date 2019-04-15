## 服务器miniconda环境搭建

### 下载并安装miniconda

~~~
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
~~~

### 创建conda环境

~~~
conda create -n env python=3.7
source ~/.bashrc
source activate env
source deavtivate env
~~~

### 直接创建python虚拟环境

~~~
mkdir tensor
cd tensor
python3 -m venv tensor
source tensor/bin/activate
~~~

