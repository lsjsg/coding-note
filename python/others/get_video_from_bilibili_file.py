import os
import shutil
def rename(path):
    i=1
    for file in os.listdir(path):
        filedir=path+'\\'+ file
        for files in os.listdir(filedir):
            filesdir=filedir+'\\'+files
            print(filesdir)
            if os.path.isdir(filesdir):
                for video in os.listdir(filesdir):
                    if video[-3:]=='blv':
                        videodir = filesdir + '\\' + video
                        os.rename(videodir,str(i)+'.blv')
                        i+=1
        os.system('rd /s /q filedir')
rename(r'C:\Users\lsjsg\Desktop\download\test')