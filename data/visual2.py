import pandas as pd
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

areas_of_training = ['Информатика и вычислительная техника',
                     'Алгоритмы искусственного интеллекта',
                     'Прикладная информатика',
                     'Программная инженерия',
                     'Безопасность компьютерных систем',
                     'Электроника, радиотехника и системы связи (11.03.01, 11.03.02, 11.03.03)',
                     'Управление в технических системах',
                     'Технология полиграфического и упаковочного производства']


excel_file = pd.read_excel('res.xlsx')
a = excel_file['program']
informatics_computer_engineering,\
artificial_intelligence_algorithms,\
applied_informatics,\
software_engineering,\
information_security,\
Electronics_radio_engineering , \
control_technical_systems, \
Technology_of_printing_production = 0, 0, 0, 0, 0, 0, 0, 0
for i in range(len(excel_file)):
    if a[i] == areas_of_training[0]:
        informatics_computer_engineering += 1
    elif a[i] == areas_of_training[1]:
        artificial_intelligence_algorithms += 1
    elif a[i] == areas_of_training[2]:
        applied_informatics += 1
    elif a[i] == areas_of_training[3]:
        software_engineering += 1
    elif a[i] == areas_of_training[4]:
        information_security += 1
    elif a[i] == areas_of_training[5]:
        Electronics_radio_engineering += 1
    elif a[i] == areas_of_training[6]:
        control_technical_systems += 1
    elif a[i] == areas_of_training[7]:
        Technology_of_printing_production += 1


applications_count = []
applications_count.append(informatics_computer_engineering)
applications_count.append(artificial_intelligence_algorithms)
applications_count.append(applied_informatics)
applications_count.append(software_engineering)
applications_count.append(information_security)
applications_count.append(Electronics_radio_engineering)
applications_count.append(control_technical_systems)
applications_count.append(Technology_of_printing_production)
print(applications_count)

bar_labels = ['red', 'blue', 'purple', 'orange', 'pink', 'gray', 'cyan', 'green']
bar_colors = ['tab:red', 'tab:blue', 'tab:purple', 'tab:orange', 'tab:pink', 'tab:gray', 'tab:cyan', 'tab:green']

ax.bar(bar_labels, applications_count, label=areas_of_training, color=bar_colors)

ax.set_ylabel('Количество заявлений')
ax.set_title('хз как')
ax.legend(title='что-то')

plt.show()

# print(informatics_computer_engineering,
# artificial_intelligence_algorithms,
# applied_informatics,
# software_engineering,
# information_security,
# Electronics_radio_engineering ,
# control_technical_systems,
# Technology_of_printing_production)


# Создание таблицы
# df = pd.DataFrame({'Направления подготовки': dict1['A'], 'Проходные баллы': dict2['C'], 'Array1': array1, 'Array2': array2})
# print(df)