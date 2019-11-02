import requests
from lxml import etree
import re

# 使用手机UA
def av(vid):
    headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
    }
# 视频url
    video_url = "https://m.bilibili.com/video/av%s.html"%vid
    html = requests.get(url=video_url, headers=headers).content.decode('utf-8')
# 获取弹幕url的参数
    cid = re.findall(r"comment: '//comment.bilibili.com/' \+ (.*?) \+ '.xml',", html)
    if cid!=[]:
        url = "https://comment.bilibili.com/" + cid[0] + ".xml"
        #print(url)
        response = requests.get(url, headers=headers)
        html = response.content

        xml = etree.HTML(html)
# 提取数据
        str_list = xml.xpath("//d/text()")
        str_list='.'.join(str_list)
        if " " in str_list:
            return vid
        if " " in str_list:
            return vid
def process(a,b,i):
    long=abs(b-a)
    now=abs(i-a)
    processes=float(now/long)
    processes=processes*100
    print('%f%% completed'%processes)
       
def core():
    ans=[]
    for i in range(17877000,17876000,-1):
        if (av(i)!=None):
            ans.append(av(i))
        process(17877000,17876000,i)
    print(ans)
core()       