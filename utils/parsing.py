from bs4 import BeautifulSoup as bs
from utils import utils
import requests

url = 'https://sbis.ru/contragents/9731082118/773101001'


def get_sbis_info(url):
    response = requests.get(url)
    if response.status != 200:
        return 'Failed to get SBIS info'
    soup = bs(response.text, features="lxml")

    sources = ['cCard__Contacts', 'cCard__Owners', 'cCard__Reliability']
    target_class = 'cCard__BlockMaskSum'

    res = []
    for source in sources:
        resp = soup.find(class_=source).find(class_=target_class).text
        resp = utils.get_millions(resp)
        res.append(resp)

    return {
        'revenue': res[0],
        'profit': res[1],
        'cost': res[2],
    }


def get_market_size(category_codes=[]):
    assert category_codes != [], 'Не выбрано ниодной категории'
    category_sum = 0

    for category in category_codes:
        page_counter = 1

        while True:
            url = f'https://checko.ru/company/select?code={category}&active=true&page={page_counter}'
            resp = requests.get(url)

            if resp.status_code != 200:
                break

            companies_table = bs(resp.text, features="lxml").find(class_="uk-table uk-table-responsive data-table")

            if companies_table is None:
                break

            companies = companies_table.find_all(class_='select-data-block')

            for tag in companies:
                if 'Выручка за' in tag.text:
                    category_sum += utils.get_millions(tag.text[20:].replace(',', '.'))

            page_counter += 1

    return round(category_sum, 3)


def get_competitors_info():
    pass