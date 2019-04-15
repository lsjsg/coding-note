## tensorflow识别手写数字

1. 创建python虚拟化环境

   ~~~
   mkdir tensor
   cd tensor
   python3 -m venv tensor
   source tensor tensor/bin/activate
   ~~~

2. 安装libraries

   ~~~
   nano requirements.txt
   	image==1.5.20
   	numpy==1.14.3
   	tensorflow==1.4.0
   pip install -r requirements.txt
   ~~~

3. 程序创建main.py

   ~~~python
   from tensorflow.examples.tutorials.mnist import input_data
   mnist = input_data.read_data_sets("MNIST_data/", one_hot=True) # y labels are oh-encoded
   ~~~

   我们使用one-hot-encoding来表示这些符号，one-hot-encoding是一种用二进制向量来表示数字或者分类的值。我们要表示的符号为0到9，这些向量含有10个值每个都由一位数表示。其中一个值被设为1，来表示指数的位数，其他的值都设为0，例如，数字3就用向量[0,0,0,1,0,0,0,0,0,0]。因为指数3的位置的值为1，所以这个向量表示数字3。

   来表示实际的照片，28x28的像素被平面化为1D的784像素的向量。每个784像素包含从0到255的数值，这表示了像素点的灰度，由于我们的图片仅仅是黑白的。所以黑色的像素点由255表示，白色像素点由0表示，在此之间有不同深浅程度的灰色。
































