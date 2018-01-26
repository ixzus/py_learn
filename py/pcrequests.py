import webbrowser

import requests

# base_url = "http://www.baidu.com/s"
#
# param = {'wd': 'Android'}
# r = requests.get(base_url, params=param)
# print(r.url)
# webbrowser.open(r.url)


# file = {'uploadFile': open('./image.png', 'rb')}
# r = requests.post('http://pythonscraping.com/files/processing2.php', files=file)
# print(r.text)

# url = 'http://pythonscraping.com/pages/cookies/welcome.php'
# payload = {'username':'Xyz','password':'password'}
# r = requests.post(url,data=payload)
# print(r.cookies.get_dict())
#
# nurl = 'http://pythonscraping.com/pages/cookies/profile.php'
# r= requests.get(nurl,cookies = r.cookies)
# print(r.text)

session = requests.Session()
url = 'http://pythonscraping.com/pages/cookies/welcome.php'
payload = {'username':'Xyz','password':'password'}
r = session.post(url,data=payload)
print(r.cookies.get_dict())

nurl = 'http://pythonscraping.com/pages/cookies/profile.php'
r= session.get(nurl)
print(r.text)