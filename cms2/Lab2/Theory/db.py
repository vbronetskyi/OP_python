import random # імпорт модуля

items = {} # оголошення словника, в якому будуть зберігатись фрази

def get_random_item():
    # функція повертає випадкове значення з словника
    return random.choice(list(items.values()))

def add_item(phrase: dict): # функція для додавання фрази в словник
     id = len(items) + 1 # унікальне значення для нової фрази
     phrase.update({"id": id}) # додаємо значення id до фрази
     items[id] = phrase # зберігаємо оновлене значення в словник фраз
     return phrase # функція повертає словник

def delete_item(id):
    if id in items: # перевірка на наявність ключа в словника
        del items[id] # видалення значення з словника
    else:
        raise ValueError("Phrase doesn`t exist")  # виклик помилки, якщо ключа
#в словнику немає. Ця помилка оброблятиметься в місці виклику функції.