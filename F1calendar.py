import requests
from bs4 import BeautifulSoup as Bs


class Calendar:
    def __init__(self, date, gp_name, time_or_winner, IsDone):
        self.date = date
        self.gp_name = gp_name
        self.time_or_winner = time_or_winner
        self.IsDone = IsDone


# the following function test if a string contains a digit or not
def has_digit(string):
    for character in string:
        if character.isdigit():
            return True
    return False


year = 2021  # minimum year is 1994

url = f'https://www.espn.com/f1/schedule/_/year/{year}'

page = requests.get(url)

src = page.content

content = Bs(src, 'lxml')

table = content.find('table', class_='Table')

tbody = table.find('tbody')

tr = tbody.find_all('tr')

data = []

for i in tr:
    td = i.find_all('td')
    gp_date = td[0].text
    gp_time = td[2].text

    if has_digit(gp_time):
        finished = False
    else:
        finished = True

    country = td[1].find('a').text

    calendar = Calendar(gp_date, country, gp_time, finished)

    data.append(calendar)
