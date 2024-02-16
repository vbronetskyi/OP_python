# Пояснення

## Трішки Firebase
-----
Якщо ще не встановлено, то потрібно встановити
```bash
pip install firebase-admin
```
\
Створення ініціалів із файла ключа, ініціалізація програми за ним, підключення до бази даних, і підключення до самго файлу grid
```python
cred = credentials.Certificate("key.json")

initialize_app(cred)

db = firestore.client()
grid_ref = db.collection('grid').document('grid')
```
\
Допоміжна функція яка приймає пошту і пароль. Якщо юзер є -> True, якщо ні, поверне повідомлення помилки
```python
def sign_in_with_email_and_password(email, password):
```
\
Проста реалізація реєстрації з використанням функції auth.create_user(), емейл і пароль беруться з форми
```python
@app.route('/register', methods = ['POST', 'GET'])
def signin_page():
    """
    Register form
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        try:
            user = auth.create_user(email = email, password = password)
            session['user'] = email
            return 'Successfully signed in'
        except:
            return 'Failed to sign in'
    
    else:
        return render_template('register_page.html')
```
\
get() бере дані з файлу на firebase, to_dict() перетворює їх у слвник, dumps - перетворює у стрічку, все разом у програмі передається із рендеренням main_page
```python
json.dumps(grid_ref.get().to_dict())
```

\
Прийом запиту зі html сторінки і збереження його данних у файл одразу на firebase
```
@app.route('/save_grid', methods=['POST'])
def send_data():
    """
    Receives the updated data
    """
    content = request.get_json()
    print(type(content))
    grid_ref.set(content)
    return 'OK'
```
\
Документація по можливостях **firebase** з **python**\
https://firebase.google.com/docs/reference/admin/python\
Те саме тільки у відео починаючи зі створення проєкту\
https://www.youtube.com/watch?v=b4W3YQdViTI

\
&nbsp;
## Як передавати змінні
-----
Ось тут я передав **access** разом із сторінкою в render_template
```python
return render_template('main_page.html',
                        grid = json.dumps(grid_ref.get().to_dict()), restart_timer=True, access = False)
```
\
Щоб зловити цю змінну у hlml можна зробити так. У даному випадку для того щоб показувати або не показувати кружечок account
```html
{% if access == True %}
<a class="account" href="/account_page">
    <div class="icon_app">
        <i class="fa-solid fa-user"></i>
    </div>
{%endif%}
```
\
Щоб зловити цю змінну у javascript ми у html її отакою штукою ловимо
```html
<script type='text/javascript'>
        var access = {{ access| tojson }};
</script>
```
\
А потім у javascript отаку магію творимо
```js
var click_enabled = JSON.parse(access);
```
\
Я впевнений що це можна простіше якось отак
```html
<script type='text/javascript'>
        var access = '{{ access }}';
</script>
```
і отак в js
```js
var click_enabled = access;
```
думаю ви розберетесь