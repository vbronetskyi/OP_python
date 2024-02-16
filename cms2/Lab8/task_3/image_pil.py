from grayscale_image import GrayscaleImageATD

# Створення нового зображення
image = GrayscaleImageATD(100, 100)

# Отримання розмірів зображення
width = image.width()
height = image.height()

# Очищення зображення
image.clear(0)

# Встановлення значення пікселя
image.setitem(50,50,128)

# Отримання значення пікселя
pixel_value = image.getitem(50,50)

# Завантаження зображення з файлу
image = GrayscaleImageATD.from_file('1234.png')

# Стиснення та розжаття зображення LZW
image.lzw_compression()
image.lzw_decompression()
