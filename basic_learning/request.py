import sys
sys.path.append('D:\python\Lib\site-packages')
import requests
from bs4 import BeautifulSoup

def getHTML(url):
    r = requests.get(url)
    return r.content

if(__name__=="__main__"):
    url = 'http://docs.python-requests.org/en/master/user/quickstart/'
    html = getHTML(url)
    print(html)
