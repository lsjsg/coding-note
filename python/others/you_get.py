import os
directory=r"C:/User/lsjsg/Desktop/test"
url=r"https://www.bilibili.com/watchlater/#/av26051982/p1"
command='you-get -o '+directory+' '+url
print(command)
os.system(command)
print('done')
