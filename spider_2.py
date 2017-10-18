
import os
import random
import requests
import re
from bs4 import BeautifulSoup
import json
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


head_user_agent = [    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                       'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                       'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                       'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11'
                       ]

proxy = []
def get_IP():
    fp = open('D:\PycharmProjects\spider/spyder0/proxy/host_tested.txt','r')
    ips = fp.readlines()

    for i in ips:
        ip = i.strip('\n')
        proxy.append(eval(ip))
    fp.close()

get_IP()


'''''
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap['phantomjs.page.settings.userAgent'] = (random.choice(head_user_agent))
dcap['phantomjs.page.settings.loadImages'] = False

driver = webdriver.PhantomJS(executable_path=r'D:\phantomjs/bin\phantomjs.exe',desired_capabilities=dcap)
driver.get('https://unsplash.com')
bs = BeautifulSoup(driver.page_source,'lxml')
category = bs.find_all('h2',class_ = '_3iawX _3myVE _27ROS')
j = 0
for i in category:
    category[j] = i.text
    j+=1
driver.close()
random.shuffle(category)
print(category)
'''''


count = 14226
for i in ['Japan', 'Work', 'Shopping', 'Bike', 'Pug', 'Team', 'Wedding', 'Social media', 'Food', 'NASA', 'Home', 'Watch', 'Flowers', 'Family', 'Laptop', 'Office', 'Health', 'Business', 'iPhone', 'Space', 'Computer', 'People', 'Autumn', 'Love', 'Mountains', 'Clothing', 'Landscape', 'Road', 'Canada', 'Restaurant', 'Girl', 'Friends', 'Typewriter', 'Fitness', 'Yoga', 'Tree', 'Feet', 'Desk', 'Summer', 'Rain', 'Sky', 'Clock', 'Music', 'City', 'Man', 'Couple', 'House', 'Woman', 'New York', 'Coffee','Nature','Happy']:
    print('now:' + i)
    headers = {
        'User-Agent':random.choice(head_user_agent),
        'accept':'*/*',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.8',
        'accept-version':'v1',
        'authorization':'Client-ID c94869b36aa272dd62dfaeefed769d4115fb3189a9d1ec88ed457207747be626',
        'dnt':'1',
        'dpr':'1.25',
        'referer':'https://unsplash.com/search/photos/' + str(i)
    }
    url = 'https://unsplash.com/napi/search/photos?query=' +str(i) + '&xp=&per_page=20&page=1'
    html = requests.get(url,headers = headers,proxies = random.choice(proxy))
    res = html.text
    json_res = json.loads(res)
    total_pages = json_res['total_pages']
    print('total_pages:' + str(total_pages))
    for j in range(1,total_pages + 1):
        print('page: %d' %j)
        url = 'https://unsplash.com/napi/search/photos?query=' + str(i) + '&xp=&per_page=20&page='+str(j)
        try:
            html = requests.get(url, headers=headers, proxies=random.choice(proxy))
            res = html.text
            json_res = json.loads(res)
            for k in json_res['results']:
                start = time.clock()
                id = k['id']
                name = k['user']['name']
                img_url = k['urls']['full']
                name = name.replace('\\', '').replace('/', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('>', '').replace('<', '').replace('|', '').replace(' ','_M')
                path = 'G:/unsplash_img/'+ str(name)
                if not os.path.exists(path):
                    os.makedirs(path)
                with open(path + '/' + str(id)+ '.jpg','wb') as fp:
                    headers_1 = {
                        'User-Agent': random.choice(head_user_agent)
                    }
                    t = random.choice(proxy)
                    print(t)
                    try:
                        data = requests.get(img_url,headers = headers_1, proxies=t,timeout =10)
                        fp.write(data.content)
                    except:
                        L = open('G:/urls/img_url.txt','a')
                        L.write(img_url)
                        L.write('\n')
                        L.close()
                        count -= 1
                    finally:
                        count += 1
                        print('这是第%d张img' %count)
                        print('耗时：%.2f' %(time.clock()-start))
        except:
            P = open('G:/urls/url.txt', 'a')
            P.write(url)
            P.write('\n')
            P.close()










