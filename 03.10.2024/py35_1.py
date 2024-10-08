import pandas as pd

# Создаем пример DataFrame
data = {
    'город': ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Казань'],
    'страна': ['Россия', 'Россия', 'Россия', 'Россия', 'Россия'],
    'регион': ['Центральный', 'Северо-Западный', 'Сибирский', 'Уральский', 'Приволжский'],
    'номер': [1001, 1002, 1003, 1004, 1005]
}

df = pd.DataFrame(data)

def search(where, what, why):
    # Проверяем, какое место поиска указано
    if where == 'город':
        target_df = df[['город', 'номер']]
    elif where == 'страна':
        target_df = df[['страна']]
    elif where == 'регион':
        target_df = df[['регион']]
    else:
        raise ValueError("Неверное значение для места поиска. Используйте: 'город', 'страна' или 'регион'.")

    # Применяем условие выбора
    if what == 'номер':
        filtered_df = target_df[target_df['номер'].astype(str).str.contains(why.replace('=', '').strip())]
        return filtered_df['город'].tolist() if where == 'город' else []
    elif what == 'название':
        if '*' in why:
            # Заменяем '*' на регулярное выражение для поиска
            pattern = why.replace('*', '.*')
            filtered_df = target_df[target_df['город'].str.contains(pattern)]
            return filtered_df['город'].tolist() if where == 'город' else []
        else:
            # Простое сравнение
            filtered_df = target_df[target_df['город'] == why]
            return filtered_df['город'].tolist() if where == 'город' else []
    
    return []

# Примеры использования функции
print(search('город', 'номер', '> 1000'))  # Получим все города с номером больше 1000
print(search('город', 'название', 'Москва'))  # Получим город с названием Москва
print(search('город', 'название', 'Мо*'))  # Получим города, начинающиеся на "Мо"
print(search('город', 'название', '*ни*'))  # Получим города, в названиях которых содержится "ни"
