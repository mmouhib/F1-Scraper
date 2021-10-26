import requests
from bs4 import BeautifulSoup as Bs


class Driver:
    def __init__(self, pos, name, nationality, team, points):
        self.pos = pos
        self.name = name
        self.nationality = nationality
        self.team = team
        self.points = points


year = 2021

url = f'https://www.formula1.com/en/results.html/{year}/drivers.html'

page = requests.get(url)

src = page.content

content = Bs(src, 'lxml')

table = content.find('table', class_='resultsarchive-table')

tbody = table.find('tbody')

tr = tbody.find_all('tr')

data = []

for team in tr:
    td = team.find_all('td')
    c = str(td[2].text.strip()).replace('\n', ' ')
    space = c.rindex(' ')
    c = c[:space]
    driver = Driver(td[1].text.strip(), c, td[3].text.strip(), td[4].text.strip(), td[5].text.strip())
    data.append(driver)
