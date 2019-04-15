import os
def rename(path):
    i=1
    for file in os.listdir(path):
        print(os.path.exists('file'))
        for files in os.listdir(file):
            if os.path.isdir(files):
                for video in files:
                    if video[-2:]=='blv':
                        os.rename(video,str(i)+'.blv')
                        i+=1

rename('E:\download\python')
