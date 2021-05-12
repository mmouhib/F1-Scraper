import requests
from bs4 import BeautifulSoup as Bs


class Constructor:
    def __init__(self, pos, name, points):
        self.pos = pos
        self.name = name
        self.points = points


# >= 1950
year = 2021

url = f'https://www.formula1.com/en/results.html/{year}/team.html'

page = requests.get(url)

src = page.content

content = Bs(src, 'lxml')

tbody = content.find('tbody')

tr = tbody.find_all('tr')

data = []

with open("./html/constructors.html", "w") as file:
    file.write(str(tbody))

for team in tr:
    td = team.find_all('td')
    constructor = Constructor(td[3].text.strip(), td[2].text.strip(), td[1].text.strip())
    data.append(constructor)
