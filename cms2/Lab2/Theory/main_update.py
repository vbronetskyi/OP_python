from fastapi import FastAPI #імпорт модуля
from http.client import HTTPException
from db import get_random_item, add_item, delete_item # імпорт функцій
import uvicorn

app = FastAPI(title="Winged phrase") #оголошення об'єкта сервера

@app.get("/") #визначення базового URL - ендпоінта
async def root(): #функція для реалізації ендпоінта (викликатиметься під час звернення)
    return {"message": "Hello World"}

@app.get("/get", response_description= "Winged phrase",
         description= "Get random phrase from database") # до сервера можна надіслати GET запит до /get ендпоінта
async def get(): # оголошення функції, яка викликатиметься, при запиті до ендпоінта
    try:
        phrase = get_random_item() # виклик функції для отримання фрази
    except IndexError:
        raise HTTPException(404, "Phrase list is empty") # todo check, possibly not correct
    return phrase # функція повертає словник з фразою та її id

@app.post("/add", response_description= "Add phrase with id parameter") # до сервера ми можна надіслати POST запит до /add ендпоінта
async def add(phrase: dict): # оголошення функції, яка викликатиметься, при запиті до ендпоінта
    phrase_out = add_item(phrase) # виклик функції для додавання фрази в словник
    return phrase_out # функція повертає фразу, що була додана

@app.delete("/delete", response_description= "Result of deletion") # до сервера можна надіслати DELETE запит до /delete ендпоінта
async def delete(id: int): # оголошення функції, яка викликатиметься, при запиті до ендпоінта
    try:
        delete_item(id) # виклик функції для видалення фрази
        return {"message": "ok"}  # функція повертає словник
    except ValueError as e: # обробка ValueError, згенерованої під час виклику функції delete_item
        raise HTTPException(404, str(e)) # функція повертає словник

if __name__ == "__main__":
    uvicorn.run(app)
