import pandas as pd

data = pd.read_csv('storage/logs/c.csv')

# mean_M2 = round(data['M2'].mean(), 2)
# max_M1 = round(data['M1'].max(), 2)
# std_M3 = round(data['M3'].std(), 2)

# print(f"Среднее значение М2: {mean_M2}")
# print(f"Максимальное значение М1: {max_M1}")
# print(f"Стандартное отклонение М3: {std_M3}")

# most_common_material = data['material'].mode()[0]

# print(f"Наиболее часто встречающееся значение в столбце 'material': {most_common_material}")

# plastic_data = data[data['material'] == 'Plastic']

# mean_M3_plastic = round(plastic_data['M3'].mean(), 2)

# data['Country Coded'] = data['country'].apply(lambda x: 1 if x == 'Mexico' else 0)

# mean_country_coded = round(data['Country Coded'].mean(), 2)
# print(mean_country_coded)

# print(f"Среднее значение M3 для material = 'Plastic': {mean_M3_plastic}")

# missing_values_M2 = data['M2'].isnull().sum()

# print(f"Количество пропущенных значений в переменной M2: {missing_values_M2:.2f}")

median_M2 = data['M2'].median()

new_M2 = data['M2'].fillna(median_M2)

third_quartile = new_M2.quantile(0.75)

print(f"Значение третьего квартиля для новой переменной: {third_quartile:.2f}")