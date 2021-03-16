import requests
import json

###下载视频
def down(name,url):
    headers_down = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36',

    }
    r = requests.get(url,headers=headers_down)
    with open("lyc/"+str(name)+".mp4", 'wb+') as f:
        f.write(r.content)


##获取主页下所有视频
def getlist():
    sec_uid="MS4wLjABAAAAumvAfskbDW1CB77yOudtt4ecmpi3Mkdm8XCkrTfRZPQ"
    count = 25
    max_cursor = 0
    has_more = True
    videotitle_list=[]


    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
        "Accept": "application/json,text/javascript,*/*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip,deflate, br",
        "X-Requested-With": "XMLHttpRequest",
        'Access-Control-Allow-Origin': '*',
        "Connection": "keep-alive"
    }
    while(has_more):
        url = "https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid="+str(sec_uid)+"&count="+str(count)+"&max_cursor="+str(max_cursor)+"&aid=1128&_signature=z1epBAAArxEnjYt5fPWXJs9XqR&dytk="
        r = requests.get(url, headers=headers)
        r.encoding = 'utf-8'
        da = json.loads(r.text)
        aweme_list  = da['aweme_list']
        has_more = da['has_more']

        for i in aweme_list:
            title = i['desc']
            video_url = i['video']['play_addr']['url_list'][0]
            #print(title)
            videotitle_list.append(title)
            #print(video_url)
            down(title,video_url)
            print(title+"-下载完成！")

        videotitle_list = list(set(videotitle_list))
        print(len(videotitle_list))

        if (len(videotitle_list)>10):
            break

        if has_more:
            max_cursor = da['max_cursor']
        else:
            break




getlist()



""":cvar

李运辰
公众号：python爬虫数据分析挖掘

公众号回复：抖音视频

总结：
1.爬取抖音视频
2.异步反爬
3.解析下一页（max_cursor）

看完这个视频，下次不能再说自己不会爬取抖音视频了





"""
