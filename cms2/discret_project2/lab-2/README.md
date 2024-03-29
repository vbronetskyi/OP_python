Розподіл роботи:

Алгоритм Гаффмана, LZW – Азарова Олена

LZ77, Deflate – Бронецький Володимир

Алгоритм Гаффмана дає кращі результати, коли вхідні дані містять багато повторюваних символів. Тобто якщо вхідні дані мають нерівномірний розподіл символів (деякі символи зустрічаються набагато частіше, ніж інші), то алгоритм Гаффмана зазвичай дає кращі результати, ніж інші методи стиснення даних. Однак, якщо вхідні дані складаються з рівномірно розподілених символів, то алгоритм Гаффмана є менш ефективним.
Зазвичай використовують алгоритм Гаффмана при стисненні текстових файлів, але він може бути застосований до будь-яких послідовностей символів.

Порівняно з алгоритмом LZW алгоритм Гаффмана швидше кодує повідомлення, проте декодує повільніше і може давати менше стиснення на даних великих розмірів.

Алгоритм LZW буде ефективним, коли є багато повторюваних послідовностей даних.
Однак, якщо вхідні дані мають випадковий характер, інші методи стиснення даних можуть бути більш ефективними, наприклад алгоритм Гаффмана.
