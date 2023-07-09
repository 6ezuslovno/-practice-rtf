import json
import pandas as pd


with open('api_2023-07-07.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    df = pd.json_normalize(data, "applications", ["regnum", "snils"])
    filtered_df = df[df['institute'] == 'ИРИТ-РТФ']
    filtered_df.to_excel('table of incoming radio faculty.xlsx', index=False)