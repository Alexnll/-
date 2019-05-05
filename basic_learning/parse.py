import sys
sys.path.append('D:\python\Lib\site-packages')
import requests
from bs4 import BeautifulSoup
import codecs
import csv


def getHTML(url):
    r = requests.get(url)
    return r.content

def parseHTML(html):
    soup = BeautifulSoup(html,'html.parser')
    body = soup.body
    course_main_content = body.find('div',attrs={'class':'main-content'})
    course_container = course_main_content.find('div',attrs={'class':'container container-content'})
    course_list = []
    for course_ul in course_container.find_all('ul',attrs={'class':'subject-list'}):
        for course_li in course_ul('li'):
            course_url = course_li.a['href']
            course_name = course_li.a['title']
            course_list.append([course_name.encode('utf-8'),course_url.encode('utf-8')])
    return course_list

def writeCSV(file_name, data_list):
    with open(file_name,'w') as f:
        writer = csv.writer(f)
        for data in data_list:
            writer.writerow(data)


URL = 'https://prog-crs.ust.hk/pgcourse'
HTML = getHTML(URL)
data_lists = parseHTML(HTML)
writeCSV('test.csv',data_lists)
