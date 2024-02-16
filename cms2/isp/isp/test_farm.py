from farm import *

storehouse = StoreHouse()
assert str(storehouse) == 'Empty storehouse'
assert storehouse.crops == {}


# У фермера є власне авто, на якому він добирається до ферми
car = Vehicle()
assert car.fuel_capacity == 50  # За замовчуванням бак авто 50л
assert car.fuel == 50  # На початку всі авто заправлені "до повного"
assert car.fuel_consumption == 0.1  # Розхід палива - 10л/100км

assert car.fuel == 50  # Ще нікуди не поїхали


car.ride(400)
assert car.fuel == 10  # після 400км залишилось ще 10л


# Добравшись на ферму, фермер оглядає поля
field1 = Field('corn', 100)
assert str(field1) == '100ha field with 100 corns on it'

assert field1.crop_type == 'corn'
assert field1.area == 100  # 100 гектарів
assert field1.crops == 100  # На кожному гектарі росте одна одиниця урожаю



# Руками збирати урожай з цілого поля - пропаща справа, нам на допомогу прийде трактор
tractor = Tractor(harvest_capacity=40)
assert isinstance(tractor, Vehicle)
assert isinstance(tractor, HarvestMixin)
assert tractor.harvest_capacity == 40  # Трактор вміщує 40 одиниць урожаю
assert tractor.fuel_capacity == 300  # Оце так бак
assert Tractor.fuel_capacity == 300

small_field = Field('corn', 1)
tractor.harvest(small_field)
assert tractor.harvested == [1, 'corn']
assert tractor.fuel == 290, tractor.fuel  # На збір урожаю з 1 гектара йде 10л пального

assert small_field.crops == 0

# На малому полі все зібрали, приступаємо до більшого
tractor.harvest(field1)
assert tractor.harvested == [30, 'corn'],tractor.harvested   # Трактор зібрав лише 30 рослин
assert tractor.fuel == 0  # Бо закінчилось пальне
assert field1.crops == 71  # На другому полі зібрали 29 рослин (і ще одна була зібрана на маленькому)
assert str(field1) == '71ha field with 71 corns on it', str(field1)

tractor.refill(10)  # долили з каністри 10л
assert tractor.fuel == 10

tractor.refill()  # до повного
assert tractor.fuel == 300


# Пора збирати моркву
field2 = Field('carrot', 50)

# Потрібно вивантажити кукурудзу, перш ніж збирати моркву
tractor.unload_to(storehouse)
assert tractor.harvested == [0, None]
assert str(storehouse) == 'Storehouse has 30 corns', str(storehouse)
assert storehouse.crops == {'corn': 30}

tractor.harvest(field2)
# assert tractor.harvested == [30, 'carrot'], tractor.harvested  # Трактор зібрав лише 30 рослин
assert tractor.fuel == 0  # Бо закінчилось пальне
assert field2.crops == 20


# Дозаправка і продовжуємо
tractor.refill()
tractor.harvest(field2)
# Хоча на полі ще є урожай і паливо в баці - ми зупинились, бо трактор переповнений
assert field2.crops == 0,  field2.crops
assert tractor.fuel == 200
assert tractor.harvested == [40, 'carrot']

tractor.unload_to(storehouse)
assert tractor.harvested == [0, None]
assert str(storehouse) == 'Storehouse has 30 corns, 40 carrots', str(storehouse)
assert storehouse.crops == {'corn': 30, 'carrot': 40}


# Пустим трактором повністю дозбируємо урожай
tractor.harvest(field2)
assert field2.crops == 0
assert tractor.fuel == 100
assert tractor.harvested == [10, 'carrot']

tractor.unload_to(storehouse)
assert str(storehouse) == 'Storehouse has 30 corns, 50 carrots', str(storehouse)

# Аж раптом буря знищила комору з усіма запасами
del storehouse.crops
assert storehouse.crops == {}


tractor.refill()
try:
    tractor.ride(3001)
    assert False
except FuelError:
    pass

# Щоб збільшити тривалість роботи, виробник покращив характеристики трактора
Tractor.upgrade_specs(fuel_capacity=400)

new_tractor = Tractor(harvest_capacity=40)
new_tractor.ride(3001)

assert Tractor.fuel_capacity == 400
assert Tractor(harvest_capacity=40).fuel_capacity == 400
assert tractor.fuel_capacity == 300  # На існуючі трактори зміна не поширюється
