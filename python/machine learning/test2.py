import tensorflow as tf
import numpy as np
# 构造输入数据(我们用神经网络拟合x_data和y_data之间的关系
x_data=np.linspace(-1,1,300)[:,np.newaxis]  #-1到1等分300份形成的二维矩阵
noise=np.random.normal(0,0.05,x_data.shape) #噪声,形状同x_data在0-0.05符合正态分布的小数
y_data=np.square(x_data)-0.5+noise          #x_data的平方,减0.05,再加上噪声值

#输入层(1个神经元)
xs=tf.placeholder(tf.float32,[None,1])#占位符,None表示n*1维矩阵,其中n不确定
ys=tf.placeholder(tf.float32,[None,1])#占位符,None表示n*1维矩阵,其中n不确定

#隐层(10个神经元)
w1=tf.Variable(tf.random_normal([1,10]))#权重,1*10的矩阵,并用符合正态分布的随机数填充
b1=tf.Variable(tf.float32,[None,1])     #偏置,1*10的矩阵,使用0.1填充
wx_plus_b1=tf.matmul(xs,w1)+b1          #矩阵xs和w1相乘,然后加上偏置
output1=tf.nn.relu(wx_plus_b1)          #激活函数使用tf.nn.relu

#输出层
w2=tf.Variable(tf.random_normal([10,1]))
b2=tf.Variable(tf.zeros([1,1])+0.1)
wx_plus_b2=tf.matmul(output1,w2)+b2
output2=wx_plus_b2

#损失
loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-output2),reduction_indices=[1]))
#在第一维上使用偏差平方求和,再求平均值来计算损失
train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)
#使用梯度下降法,设置步长0.1,来最小化损失

#初始化
init=tf.global_variables_initializer()#初始化所有变量
sess=tf.Session()
sess.run(init)#变量初始化

#训练
for i in range(1000): #训练1000次
    _,loss_value=sess.run([train_step,loss],feed_dict={xs:x_data,ys:y_data})
    #梯度下降并计算每一步的损失
    if(i%50==0):
        print(loss_value)#每50步输出一次损失