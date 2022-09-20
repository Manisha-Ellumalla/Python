import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#url = raw_input('Enter - ')
url = ' http://py4e-data.dr-chuck.net/known_by_Ghyll.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)
# print soup
count = int(raw_input('Enter count: '))+1
position = int(raw_input('Enter position: '))


tags = soup('a')
# next line gets count tags starting from position
my_tags = tags[position: position+count]
tags_lst = []
for tag in my_tags:
    needed_tag = tag.get('href', None)
    tags_lst.append(needed_tag)
print (tags_lst)
