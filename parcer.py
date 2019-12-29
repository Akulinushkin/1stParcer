import requests
from bs4 import BeautifulSoup


headers = {'accept': '*/*',
           'user-agent': 'Chrome/78.0.3904.108 '}
base_url = 'https://hh.ru/search/vacancy?clusters=true&area=1&enable_snippets=true&salary=&st=searchVacancy&text=Python'


def hh_parc(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'vacancy-serp-item'})
        for div in divs:
            title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
            print(title)
    else:
        print('ERROR')


hh_parc(base_url, headers)