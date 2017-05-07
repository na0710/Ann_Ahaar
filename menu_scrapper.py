import requests
from bs4 import BeautifulSoup

url = 'http://www.bestofindiausa.com/menu.htm'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html,"lxml")
table = soup.find('div', attrs={'id': 'main'})
table1 = soup.find('div', attrs={'id': 'menu'})


for row in table1.findAll('tr'):
    for cell in row.findAll('td'):
        print(cell.text)
