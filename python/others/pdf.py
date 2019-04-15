# coding = UTF-8
 
import urllib.request
import re
import os
 
# open the url and read
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    page.close()
    return html
 
# compile the regular expressions and find
# all stuff we need
def getUrl(html):
    reg = r'([A-Z]\d+)' #匹配了G176200001
    url_re = re.compile(reg)
    url_lst = url_re.findall(html.decode('UTF-8')) #返回匹配的数组
    return(url_lst)
 

def getFile(url):
    file_name = url.split('/')[-1]
    u = urllib.request.urlopen(url)
    f = open(file_name, 'wb')
 
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
 
        f.write(buffer)
    f.close()
    print ("Sucessful to download" + " " + file_name)
 
 
root_url = 'https://edimension.sutd.edu.sg/bbcswebdav/pid-66985-dt-content-rid-1054805_1/courses/1830-100004/HW3_2018_final.pdf'  #下载地址中相同的部分
 
raw_url = 'file:///C:/User/lsjsg/Desktop/test'
 
html = getHtml(raw_url)
url_lst = getUrl(html)
 
os.mkdir('pdf_download')
os.chdir(os.path.join(os.getcwd(), 'pdf_download'))
 
for url in url_lst[:]:
    url = root_url + url+'/'+url+'.pdf'  #形成完整的下载地址
    getFile(url)
