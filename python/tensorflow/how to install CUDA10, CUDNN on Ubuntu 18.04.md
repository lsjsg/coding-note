# how to install CUDA10, cuDNN

First download cuda 10 from NVIDIA website:

https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804

choose Linux, x86_64, Ubuntu, 18.04, runfile(local)

then use command:

~~~
sudo sh cuda_10.0.130_410.48_linux.run
~~~

if you have already installed the nvidia driver, then the options can be choose like this:

![img](https://img-blog.csdnimg.cn/20181116114710566.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMyNDA4Nzcz,size_16,color_FFFFFF,t_70)

after that if you see 

~~~
***WARNING: Incomplete installation! This installation did not install the CUDA Driver. A driver of version at least 384.00 is required for CUDA 10.0 functionality to work.
To install the driver using this installer, run the following command, replacing <CudaInstaller> with the name of this run file:
sudo <CudaInstaller>.run -silent -driver
~~~

this is note an error, but because we didn't install the nvidia driver, so long as you have already installed one that satisfies the demands then it is already alright.

The next step is adding cuda in to the path:

~~~
sudo nano ~/.bashrc
~~~

and add: 

~~~
export CUDA_HOME=/usr/local/cuda 
export PATH=$PATH:$CUDA_HOME/bin 
export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
~~~

save and exit then

~~~
source ~/.bashrc
~~~

now we can test whether we have installed it successfully

~~~
cd /usr/local/cuda/samples/1_Utilities/deviceQuery 
sudo make
./deviceQuery
~~~

if you see this then it shows that you have successfully installed cuda

![img](https://img-blog.csdnimg.cn/20181116115507854.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMyNDA4Nzcz,size_16,color_FFFFFF,t_70)

also download the cuDNN file from:

https://developer.nvidia.com/rdp/cudnn-download

select the same version as the cuda version, dowload the file and unzip it then

~~~
sudo cp cuda/include/cudnn.h /usr/local/cuda/include/ 
sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64/ 
sudo chmod a+r /usr/local/cuda/include/cudnn.h 
sudo chmod a+r /usr/local/cuda/lib64/libcudnn*
~~~

Finally you have finished install cuda and cuDNN

