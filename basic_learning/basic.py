import sys
sys.path.append('D:\python\Lib\site-packages')
import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.wise.xmu.edu.cn/people/faculty')
print(r)

html = r.content
# print(html)

soup = BeautifulSoup(html, 'html.parser')
print(soup)

div_people_list = soup.find('div',attrs={'class': 'people_list'})
# print(div_people_list)

a_s = div_people_list.find_all('a', attrs={'target':'_blank'})
for a in a_s:
    url = a['href']
    name = a.get_text()
#    print(name+"+"+url)