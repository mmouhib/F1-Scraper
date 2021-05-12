import requests
from bs4 import BeautifulSoup as Bs


class GrandPrix:
    def __init__(self, location, date, winner, team, laps, duration):
        self.location = location
        self.date = date
        self.winner = winner
        self.team = team
        self.laps = laps
        self.duration = duration


year = 2021

url = f'https://www.formula1.com/en/results.html/{year}/races.html'

page = requests.get(url)

src = page.content

content = Bs(src, 'lxml')

table = content.find('table', class_='resultsarchive-table')

tbody = table.find('tbody')

tr = tbody.find_all('tr')

data = []

for full_team_data in tr:
    td = full_team_data.find_all('td')

    c = str(td[3].text.strip()).replace('\n', ' ')
    space = c.rindex(' ')
    c = c[:space]

    gp = GrandPrix(td[1].text.strip(), td[2].text.strip(), c, td[4].text.strip(), td[5].text.strip(),
                   td[6].text.strip())
    data.append(gp)
