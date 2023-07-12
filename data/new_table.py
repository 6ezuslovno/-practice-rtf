import pandas as pd
import xlsxwriter

# Создание таблицы с информацией о доступных местах
seats_data = {
    'program': [
        'Информатика и вычислительная техника',
        'Алгоритмы искусственного интеллекта',
        'Прикладная информатика',
        'Программная инженерия',
        'Безопасность компьютерных систем',
        'Электроника, радиотехника и системы связи (11.03.01, 11.03.02, 11.03.03)',
        'Радиотехника',
        'Инфокоммуникационные технологии и системы связи',
        'Конструирование и технология электронных средств',
        'Управление в технических системах',
        'Технология полиграфического и упаковочного производства'
    ],
    'seats': [
        120, 100, 199, 230, 80, 150, 150, 150, 150, 50, 45
    ]
}

# Создание DataFrame из таблицы с информацией о доступных местах
seats_df = pd.DataFrame(seats_data)

# Загрузка данных о поступающих из файла Excel
df = pd.read_excel('table of incoming radio faculty 2023-07-11.xlsx')
filtered_df = df[(df['compensation'] == 'бюджетная основа') & (df['priority'] == 1) & ((df['status'] == 'Рейтинг') | (df['status'] == 'К зачислению')) & (df['is_without_tests'] == False)]

# Группировка данных по программе и подсчет количества поступающих, приоритета 1 и статуса "К зачислению"
grouped_df = filtered_df.groupby('program').agg(
    {'regnum': 'count',
     'priority': lambda x: sum(x == 1),
     'status': lambda x: sum(x == 'К зачислению'),
     'total_mark': 'mean'}
).reset_index()

# Объединение с таблицей о доступных местах
merged_df = pd.merge(seats_df, grouped_df, on='program', how='left')
merged_df['количество поступающих'] = grouped_df['regnum']
merged_df['количество мест'] = seats_df['seats']

# Рассчет процента набора по программе
merged_df['набор в % по программе'] = (merged_df['status'] / merged_df['количество мест']) * 100

# Подсчет суммы баллов и количества студентов на каждой программе
# df_sorted = filtered_df.sort_values(by='total_mark', ascending=False)
# group_sorted = df_sorted.groupby('program').head(300)  # Выбираем первые 200 записей для каждой программы
# group_sorted = group_sorted.reset_index(drop=True)  # Сбрасываем индексы для удобства работы
# place_program1 = group_sorted.loc[group_sorted['program'] == 'Информатика и вычислительная техника'].iloc[119]
# place_program2 = group_sorted.loc[group_sorted['program'] == 'Алгоритмы искусственного интеллекта'].iloc[99]
# place_program3 = group_sorted.loc[group_sorted['program'] == 'Прикладная информатика'].iloc[198]
# place_program4 = group_sorted.loc[group_sorted['program'] == 'Программная инженерия'].iloc[229]
# place_program5 = group_sorted.loc[group_sorted['program'] == 'Безопасность компьютерных систем'].iloc[79]
# # place_program6 = group_sorted.loc[group_sorted['program'] == 'Управление в технических системах'].iloc[49]
# # place_program7 = group_sorted.loc[group_sorted['program'] == 'Технология полиграфического и упаковочного производства'].iloc[44]
#
# print(place_program1['total_mark'])
# print(place_program2['total_mark'])
# print(place_program3['total_mark'])
# print(place_program4['total_mark'])
# print(place_program5['total_mark'])
# # print(place_program6['total_mark'])
# # print(place_program7['total_mark'])

avg_score_df = filtered_df.groupby('program').agg({'total_mark': 'sum', 'regnum': 'count'}).reset_index()
avg_score_df.columns = ['program', 'сумма баллов', 'количество студентов']

# Рассчет среднего балла
avg_score_df['средний балл'] = avg_score_df['сумма баллов'] / avg_score_df['количество студентов']

# Объединение данных
merged_df = pd.merge(merged_df, avg_score_df, on='program', how='left')

# Вывод сводной таблицы
#pivot_table = merged_df[['program', 'количество мест', 'количество поступающих', 'priority', 'status', 'средний балл', 'набор в % по программе']]
#pivot_table.columns = ['program', 'количество мест', 'количество поступающих', 'Приоритет 1', 'Статус', 'Средний балл', 'набор в % по программе']
#print(pivot_table)
#pivot_table.to_excel('pivot_table-11-07-2.xlsx', index=False)

# Вывод сводной таблицы
pivot_table = merged_df[['program', 'seats', 'regnum', 'priority', 'status', 'средний балл', 'набор в % по программе']]
pivot_table.columns = ['Программа', 'количество мест', 'количество поступающих', 'Приоритет 1', 'К зачислению', 'Средний балл', 'Набор в % по программе']

# Сохранение в файл Excel с форматированием
writer = pd.ExcelWriter('pivot_table-07-11-7.xlsx', engine='xlsxwriter')
pivot_table.to_excel(writer, index=False, sheet_name='Sheet1', header=True)

# Получение объекта рабочей книги и листа
workbook = writer.book
worksheet = writer.sheets['Sheet1']

# Настройка форматирования заголовков
header_format = workbook.add_format({'bold': True, 'font_size': 14, 'align': 'center'})
worksheet.set_row(0, 30)  # Установка высоты строки для заголовков

# # Запись заголовка "Программа"
# worksheet.merge_range('A1:A1', 'Программа', header_format)
#
# # Запись заголовка "Бюджет"
# worksheet.merge_range('B1:G1', 'Бюджет', header_format)
#
# # Настройка ширины столбцов
# worksheet.set_column('A:A', 63)
# worksheet.set_column('B:G', 15)

# writer.save()
writer.close()