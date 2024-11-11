import pandas as pd


"""
1.	Общее число оценок в файле
2.	Общее количество пользователей, поставивших оценки
3.	Общее количество оцененных фильмов
4.	ID самого активного пользователя
5.	Фильм, собравший наибольшее количество оценок
"""

file_path = "../data/ratings_small.csv"

df = pd.read_csv(file_path)
print(df)
# pd.read_csv(filepath, **kwargs): Читает .csv файл и возвращает объект DataFrame.
# df.to_csv(filepath, **kwargs): Сохраняет DataFrame в файл .csv
# df.head(n): Возвращает первые n строк (по умолчанию 5).
# df.tail(n): Возвращает последние n строк.
# df.info(): Выводит информацию о типах данных и количестве ненулевых значений в каждом столбце.
# df.describe(): Возвращает статистическое описание числовых столбцов (среднее, медиана и т.д.).
# df['column']: Выбор столбца.
# df[['col1', 'col2']]: Выбор нескольких столбцов.
# df.iloc[]: Индексация по номерам строк и столбцов.
# df.loc[]: Индексация по меткам строк и именам столбцов.
# df_filtered = df[df['column'] > 10]  # фильтр по значению в столбце 'column'
# df.dropna(): Удаление строк с пропущенными значениями (NaN).
# df.fillna(value): Замена пропущенных значений (NaN) указанным значением.
# df.drop_duplicates(): Удаление дублирующихся строк.
# df.groupby('column').mean(): Группировка по значению в столбце и вычисление среднего значения для каждой группы.
# df['column'].value_counts(): Подсчёт количества уникальных значений в столбце.
# df.sort_values(by='column', ascending=True): Сортировка по значению в указанном столбце.
# df.sort_index(): Сортировка по индексу.
# pd.merge(df1, df2, on='column', how='inner'): Соединение двух DataFrame по общему столбцу.
# df['column'] = df['column'].astype('int'): Изменение типа данных столбца.
# pd.to_datetime(df['date_column']): Преобразование столбца в формат даты.


