import requests
import json
from datetime import date
import pandas as pd

url = 'https://urfu.ru/api/entrant/'
params = {'page': 1, 'size': 100}
data = {}
current_date = date.today()
items = []
while True:
    response = requests.get(url, params=params)
    page_data = response.json()
    items += page_data['items']
    if not page_data['items']:
        break

    params['page'] += 1  # Переходим на следующую страницу
    print(params['page'])
    print(len(items))

print(items)
with open(f'api_{current_date}.json', 'a', encoding='utf-8') as json_file:
        json.dump(items, json_file, ensure_ascii=False)
        json_file.write('\n')