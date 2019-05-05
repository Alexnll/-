import sys
sys.path.append('D:\python\Lib\site-packages')
from lxml import etree
import requests
from bs4 import BeautifulSoup
'''
html = etree.HTML(text)     # 构造Xpath接析对象
result = etree.tostring(html)    # 修正html码
print(result.decode('utf-8'))    # bytes类型转为str类型
'''
URL = 'https://www.bilibili.com/v/game'
html = requests.get(URL)
soup = BeautifulSoup(html.content, 'lxml')
# print(soup.prettify())
for span in soup.find_all():
    print(span.string)
