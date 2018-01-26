from urllib.request import urlopen

html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
# print(html)


import re
res = re.findall("<title>(.+?)</title>",html)
print("\nPage title is:",res[0])

import re
res = re.findall("<p>(.+?)</p>",html,flags=re.DOTALL)
print("\nPage paragraph is:",res[0])

res = re.findall(r'href="(.*?)"',html)
print("\nAll links:",res)