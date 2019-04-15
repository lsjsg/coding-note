# octave教程

## 基本技巧

注释方法: 使用(%) 来对后面内容进行注释

在语句后加上(;), 则回车后不会打印结果

octave use single quote to represent strings

同一行使用多个命令可以使用(,) or (;) 隔开, 逗号仍可打印, 但分号不可以

~~~ octave
2*3  2-3  2^3
hist(a) % 将会绘制出变量a的直方图
hist(a,50) % 绘制的图像包含更多小区间
PS1('>>>') % 可以修改命令前提示符
disp(a) % 将会打印出a
disp(sprintf('2 decimals: %0.2f',a)) % 将打印格式化
format long % 将结果显示为更多小数位数
format short % 将结果显示为更少小数位数
~~~

## 逻辑运算

真为1, 假为0, 等于是==, 不等于是~=

~~~octave
1 && 0 % && means "and"
1 || 0 % || means "or"
xor(1,0) % 异或运算
~~~

## 矩阵

~~~octave
% 创建矩阵的方法, 矩阵行在前,列在后(3,2)是个3行两列的矩阵
a=[1 2;3 4;5 6]
a(3,2) %will link to the variable at 3 row,2 column
a(2,:) %to fetch every thing in the second row
a(:,2) %to get every thing in the second column
a([1 3],:) % this means get all of the element of a from 1 and 3 row
a(:2)=[10;11;12] %this will change all the values in the second column
a=a[a,[100;101;102]] %append another column vector to the right
b=a(:) %this will put all the elements in a into a single column vector
a=ones(3,2)  % matrix only contain 1
a=zeros(3,2) % matrix only contain 0
a=rand(3,2)  % matrix with random number between (0,1)
a=randn(3,2) % 服从高斯分布的随机数,平均值为0 或者方差为1
a=eye(3)     % 将生成一个3*3的单位矩阵(左对角线全为1)
v=1:0.1:1.5  % one row vector start from 1,increment step of 0.1 till 1.5
v=1:6 % one row vector start from 1, increase till 6
size(a) % returns the size of the matrix(it self is returning a 1*2 matrix)
size(a,1) % return the first dimension of a(the number of the rows)
size(a,2) % return the second dimenison of a(the number of the columns)
length(a) %return the size of the longest dimension

c=[a b] % =[a,b] concatenating a and b onto each other
c=[a;b] % put the next thing at the bottom
~~~

## 加载文件及数据查找

~~~ octave
pwd % shows the current path that octave is in
cd  % stands for change directory
ls  % list out the directories
load 'file name'  % to load the file
load('file name') % to load the file
who % this command shows the variables that have in the workspace
whos% this command will show the information in more detail
clear 'name of the variable'%this command will delet the variable in the memory
clear %this will clear all variables in the memory
v=a(1:10)%gives the first 10 value in a to v
save hello.mat v % this will save the variable a into the disk(binary type)
save hello.txt v -ascii% this will save data as text
~~~

## 数据的运算操作

~~~ octave
a*b  % is the multiply of two matrixs
a.*b % every element in a will multiply with every coresponding elements in b
a.^2 % every element in a will be squered
% a dot (.) stands for the processing of every element in the matrix
log(v) % this is the processing of every element in v
exp(v) % e^v for every element 
abs(v) % the absolute value of every element in v
max(v) % this returns the max value of a
% if it is a matrix then it will return the max of every column
[val, ind]=max(v) %returns the max value and it's index
v + ones(length(v),1) % is to increase every element in v by 1
v + 1 % the same as the method above
a' % is the transpose of a(转置矩阵)
find(a<3) % this will find the index of the element that is less than 3
magic(3) % it will create a 3x3 matrix that all their rows and columns and diagonals sum up to the same thing
sum(a) % the sum of all the elements in a
prod(a) % the product of all the element in a
floor(a) %rounds down these element of a
ceil(a) % gets all the elements round up
max(rand(3),rand(3)) % create a matrix that is larger in the coresponding place
max(magic(3),[],1) % this takes the column wise maximum, 1 means take the max of the first dimension of a
max(max(a)) % used to find the max value of the whole matrix
max(a(:)) % is the same as put all the element into the vector and find the max
flipud(eye(9)) %flipud 表示矩阵的垂直翻转
pinv(a) % 求得a的伪逆矩阵
pinv(a) * a %几乎得到一个单位矩阵

~~~

## 数据的可视化处理

~~~ octave
t=[0:0.01:98]
y1=sin(t);
y2=cos(t);
plot(t,y1) % 即可获得y1关于t的图像
hold on % in order to plot new figures on the old graph or else octave will erase the original one and plot a new one
plot(t,y2,'r') % 'r' is used to plot y2 in red color
xlabel('time') % to label the x axis values
ylabel('time') % to label the y axis values
legend('sin','cos') % use to label the two lines
title('my fihure') % assign a title to the graph
print -dpng 'my plot.png' % to save the plot in a png file
close % command will close the plot
figure(1);plot(t,y1); % this will start up first figure
figure(2);plot(t,y2); % this will start up another figure, with another figure number
% then there will exist two figures at the same time
subplot(1,2,1) % it sub-divide the plot into a 1x2 grid(格子) and set now we are using the first grid right now
plot(t,y1); % then the software will plot the graph on the left side
axis([0.5 1 -1 1]) % the first two figures will set the x range and the last two digits will set the y range for the figure on the right
clf; % will clears a figure
a=magic(5)
imagesc(a)% wil plot a 5x5 grid of colors, differet colors coresponding to different values in the a matrix
colorbar % shows the sdandard of which color stand for what number
colormap gray % plot the grid in black and white
~~~

## octave 之控制语句

~~~ octave
% for loop
v=zeros(10,1);
for i=1:10,
	v(i)=i^2 % space does not matter at all
end;

indices=1:10; % create an array from 1 to 10
for i=indices % the same as for i=1:10

% while loop
i=1;
while i <=5,
	v(i)=100;
	i+=1;
end;
~~~



