class BWT:
    def __init__(self):
        self.transformed_data = ''

    def transform(self, data):
        self.transformed_data = self.bwt_transform(data)

    def restore(self):
        return self.bwt_restore(self.transformed_data)

    @staticmethod
    def bwt_transform(data):
        data += '$'  # Додаємо спеціальний символ на кінець рядка
        rotations = [data[i:] + data[:i] for i in range(len(data))]  # Створюємо всі можливі ротації рядка
        rotations.sort()  # Сортуємо ротації лексикографічно
        transformed_data = ''.join([rotation[-1] for rotation in rotations])  # Формуємо BWT перетворений рядок
        return transformed_data

    @staticmethod
    def bwt_restore(transformed_data):
        table = [''] * len(transformed_data)  # Створюємо таблицю для відновлення
        for _ in range(len(transformed_data)):
            table = sorted([transformed_data[i] + table[i] for i in range(len(transformed_data))])  # Сортуємо таблицю
        restored_data = next(item for item in table if item.endswith('$'))[:-1]  # Знаходимо рядок, що закінчується на '$' та відкидаємо його
        return restored_data


# Приклад використання
with open('text1.txt', 'r', encoding="utf-8") as file:
    data = file.read()
bwt = BWT()

# Стиснення даних
bwt.transform(data)
compressed_data = bwt.transformed_data
print(len(compressed_data))

# Розтиснення даних
restored_data = bwt.restore()
print(len(restored_data))
