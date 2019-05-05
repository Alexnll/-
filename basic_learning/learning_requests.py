import sys
sys.path.append('D:\python\Lib\site-packages')
import requests
import re
import json
import time
'''
# request用法，headers, write
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
r = requests.get('https://github.com/favicon.ico', headers = headers)
with open('fa.ico','wb') as f:
    f.write(r.content)
'''
'''
# post用法
data = {
    'name': 'germey',
    'age': '22'
}
r = requests.post('https://httpbin.org/post',data=data)
print(r.text)
'''
'''
# 正则表达式
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
r = requests.get('https://www.zhihu.com/explore', headers=headers)

results = re.findall('<a.*?Title">\n(.*?)\n</a>',r.text,re.S)
for result in results:
    print(result)
'''
# 抓取猫眼电影排行
def get_one_page(URL):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    r = requests.get(URL,headers)
    if r.status_code == 200:
        return r.text
    else:
        return None

def parse_one_page(text):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?name.*?title.*?>(.*?)<.*?'
        'star.*?主演：(.*?)</p>.*?releasetime.*?>上映时间：(.*?)<.*?</dd>', re.S)
    items = re.findall(pattern, text)
    for item in items:
        yield {
            '排名': item[0],
            '电影': item[1],
            '主演': item[2].strip(),
            '上映时间': item[3]
        }

# 通过JSON库的dumps()使字典序列化
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')

def main(URL,offset):
    text = get_one_page(URL+'?offset='+str(offset))
    items = parse_one_page(text)
    for item in items:
        print(item)
        write_to_file(item)

if __name__=='__main__':
    url = 'https://maoyan.com/board/4'
    for i in range(5):
        main(url,i*10)
        time.sleep(1)

'''

index = re.compile('<dd>.*board-index.*?>(/d+)</i>',re.S)
pic = re.compile('<img.*src="(.*?)">',re.S)
name = re.compile('<p\bclass="name".*title="(.*?)".*?</p>',re.S)
acters = re.compile('<p\bclass="star">(.*?)</p>',re.S)
time = re.compile('<p\bclass="releasetime">(.*?)</p>',re.S)
'''