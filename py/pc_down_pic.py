import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nationalgeographic.com.cn/animals/'
html = requests.get(base_url).text
soup = BeautifulSoup(html, features='lxml')
img_ul = soup.find_all('ul', {'class': 'img_list'})
for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        img_name = url.split('/')[-1]
        with open('./img/%s' % img_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
            print('Save %s' %img_name)
