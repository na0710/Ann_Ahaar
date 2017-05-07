import requests
from bs4 import BeautifulSoup

url = 'http://travel.cnn.com/explorations/eat/worlds-50-most-delicious-foods-067535/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html,"lxml")

table = soup.find('div', attrs={'id': 'page-wrapper'})
table1 = soup.find('div', attrs={'id': 'page'})
table2 = soup.find('div', attrs={'id': 'gutter-fix'})
table3 = soup.find('div', attrs={'id': 'main-wrapper'})
table4 = soup.find('div', attrs={'id': 'main', 'class':'clearfix'})
table5 = soup.find('div', attrs={'id': 'content', 'class':'column'})
table6 = soup.find('div', attrs={'class':'section'})

table7 = soup.find('div', attrs={'class':'region region-content'})
table8 = soup.find('div', attrs={'id': 'block-system-main', 'class':'block block-system first last odd'})
table9 = soup.find('div', attrs={'class':'content'})
table10 = soup.find('div', attrs={'id': 'node-124535', 'class':'node node-article view-mode-full clearfix divider'})
table11 = soup.find('div', attrs={'class':'content clearfix'})

table12 = soup.find('div', attrs={'class':'node-body'})
table13 = soup.find('div', attrs={'class':'field field-name-body field-type-text-with-summary field-label-hidden'})
table14 = soup.find('div', attrs={'class':'field-items'})
table15 = soup.find('div', attrs={'class':'field-item even'})

for row in table1.findAll('h2'):
	print(row.text)

"""
table = soup.find('div', attrs={'id': 'main'})
table1 = soup.find('div', attrs={'id': 'menu'})


for row in table1.findAll('tr'):
    for cell in row.findAll('td'):
        print(cell.text)
"""