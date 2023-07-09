import pandas as pd
import matplotlib.pyplot as plt

date_lst = ['2023-07-07', '2023-07-08', '2023-07-09']
avg_l = []
informatics_computer_engineering,\
artificial_intelligence_algorithms,\
applied_informatics,\
software_engineering,\
information_security,\
Electronics_radio_engineering , \
control_technical_systems, \
Technology_of_printing_production,\
counter_informatics_computer_engineering,\
counter_artificial_intelligence_algorithms,\
counter_applied_informatics,\
counter_software_engineering,\
counter_information_security,\
counter_Electronics_radio_engineering,\
counter_control_technical_systems,\
counter_Technology_of_printing_production = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

avg_dict = {}
result = []

areas_of_training = ['Информатика и вычислительная техника',
                     'Алгоритмы искусственного интеллекта',
                     'Прикладная информатика',
                     'Программная инженерия',
                     'Безопасность компьютерных систем',
                     'Электроника, радиотехника и системы связи (11.03.01, 11.03.02, 11.03.03)',
                     'Управление в технических системах',
                     'Технология полиграфического и упаковочного производства']

areas_of_training_nums = ['09.03.01',
                     '09.03.01(ИИ)',
                     '09.03.03',
                     '09.03.04',
                     '10.03.01',
                     '11.00.00',
                     '27.03.04',
                     '29.03.03']

# for i in range(len(date_lst)):
#     excel_file = pd.read_excel(f'table of incoming radio faculty {date_lst[i]}.xlsx')
#     a = excel_file['edu_doc_original']
#     b = excel_file['total_mark']
#     c = excel_file['program']
#     for i in range(len(a)):
#         if a[i] and c[i] == areas_of_training[0]:
#             informatics_computer_engineering += b[i]
#             counter_informatics_computer_engineering += 1
#         elif a[i] and c[i] == areas_of_training[1]:
#             artificial_intelligence_algorithms += b[i]
#             counter_artificial_intelligence_algorithms += 1
#         elif a[i] and c[i] == areas_of_training[2]:
#             applied_informatics += b[i]
#             counter_applied_informatics += 1
#         elif a[i] and c[i] == areas_of_training[3]:
#             software_engineering += b[i]
#             counter_software_engineering += 1
#         elif a[i] and c[i] == areas_of_training[4]:
#             information_security += b[i]
#             counter_information_security += 1
#         elif a[i] and c[i] == areas_of_training[5]:
#             Electronics_radio_engineering += b[i]
#             counter_Electronics_radio_engineering += 1
#         elif a[i] and c[i] == areas_of_training[6]:
#             control_technical_systems += b[i]
#             counter_control_technical_systems += 1
#         elif a[i] and c[i] == areas_of_training[7]:
#             Technology_of_printing_production += b[i]
#             counter_Technology_of_printing_production += 1
#     print(informatics_computer_engineering // counter_informatics_computer_engineering)
#     print(artificial_intelligence_algorithms // counter_artificial_intelligence_algorithms)
#     print(applied_informatics // counter_applied_informatics)
#     print(software_engineering // counter_software_engineering)
#     print(information_security // counter_information_security)
#     print(Electronics_radio_engineering // counter_Electronics_radio_engineering)
#     print(control_technical_systems // counter_control_technical_systems)
#     print(Technology_of_printing_production // counter_Technology_of_printing_production)
    # avg_l.append(summ // counter)
# print(avg_l)


excel_file = pd.read_excel(f'table of incoming radio faculty {date_lst[2]}.xlsx')
a = excel_file['edu_doc_original']
b = excel_file['total_mark']
c = excel_file['program']
for i in range(len(a)):
    if a[i] and c[i] == areas_of_training[0]:
        informatics_computer_engineering += b[i]
        counter_informatics_computer_engineering += 1
    elif a[i] and c[i] == areas_of_training[1]:
        artificial_intelligence_algorithms += b[i]
        counter_artificial_intelligence_algorithms += 1
    elif a[i] and c[i] == areas_of_training[2]:
        applied_informatics += b[i]
        counter_applied_informatics += 1
    elif a[i] and c[i] == areas_of_training[3]:
        software_engineering += b[i]
        counter_software_engineering += 1
    elif a[i] and c[i] == areas_of_training[4]:
        information_security += b[i]
        counter_information_security += 1
    elif a[i] and c[i] == areas_of_training[5]:
        Electronics_radio_engineering += b[i]
        counter_Electronics_radio_engineering += 1
    elif a[i] and c[i] == areas_of_training[6]:
        control_technical_systems += b[i]
        counter_control_technical_systems += 1
    elif a[i] and c[i] == areas_of_training[7]:
        Technology_of_printing_production += b[i]
        counter_Technology_of_printing_production += 1
result.append(informatics_computer_engineering // counter_informatics_computer_engineering)
result.append(artificial_intelligence_algorithms // counter_artificial_intelligence_algorithms)
result.append(applied_informatics // counter_applied_informatics)
result.append(software_engineering // counter_software_engineering)
result.append(information_security // counter_information_security)
result.append(Electronics_radio_engineering // counter_Electronics_radio_engineering)
result.append(control_technical_systems // counter_control_technical_systems)
result.append(Technology_of_printing_production // counter_Technology_of_printing_production)


for i in range(8):
    avg_dict[areas_of_training[i]] = result[i]
avg_list = avg_dict.values()

fig, ax = plt.subplots(figsize=(12, 7))
bar_labels = ['red', 'blue', 'purple', 'orange', 'pink', 'gray', 'cyan', 'green']
bar_colors = ['tab:red', 'tab:blue', 'tab:purple', 'tab:orange', 'tab:pink', 'tab:gray', 'tab:cyan', 'tab:green']

ax.bar(areas_of_training_nums, avg_list, color=bar_colors)


ax.set_title('Средний балл по направлениям')

# ax.legend(title='Направления', bbox_to_anchor=(0.82, 0.2), loc='center left')

for i, v in enumerate(avg_list):
    ax.text(i, v+0.2, str(v), ha='center')

plt.show()