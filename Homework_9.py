# Задача 40: Работать с файлом california_housing_train.csv,
# который находится в папке sample_data.
# Определить среднюю стоимость дома,
# где кол-во людей от 0 до 500 (population).

import pandas as pd

data_file = pd.read_csv('sample_data/california_housing_train.csv')
print(f'Cредняя стоимость дома, где кол-во людей от 0 до 500: ')
print(data_file[(data_file['population'] >= 0) & (data_file['population'] <= 500)]['median_house_value'].mean())

# Задача 42: Узнать какая максимальная households
# в зоне минимального значения population.

print()
print('Максимальная households в зоне минимального значения population: ')
print(data_file[data_file['population'] == data_file['population'].min()]['households'].max())