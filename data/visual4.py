import pandas as pd
import matplotlib.pyplot as plt

date_lst = ['2023-07-07', '2023-07-08', '2023-07-09']

count_l = []

for i in range(len(date_lst)):
    counter = 0
    excel_file = pd.read_excel(f'table of incoming radio faculty {date_lst[i]}.xlsx')
    a = excel_file['edu_doc_original']
    for i in range(len(a)):
        if a[i]:
            counter += 1
    count_l.append(counter)
print(count_l)

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(date_lst, count_l)
ax.scatter(date_lst, count_l)
for i, (date, count) in enumerate(zip(date_lst, count_l)):
    ax.annotate(count, (date, count))
    # if i == 0:  # Индекс точки, которую нужно сместить (в данном случае третья точка).
    #     ax.annotate(count, (date, count), xytext=(10, 5), textcoords='offset points')
plt.show()


