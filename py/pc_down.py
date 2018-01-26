import os

path = './img/'
name = 'image1.png'
os.makedirs(path, exist_ok=True)
img_url = 'https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'

# 1.
# from urllib.request import urlretrieve
# urlretrieve(img_url,path+name)

# 2
import requests
r = requests.get(img_url)
with open(path+name,'wb') as f:
    f.write(r.content)

# 3
# import requests
# r = requests.get(img_url)
# with open(path + name, 'wb') as f:
#     for chunk in r.iter_content(chunk_size=128):
#         f.write(r.content)
