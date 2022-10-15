# Программа универсальна и работает для любого варианта
# Мой вариант - 5
# Ожидаемый ввод: 2 4 10 y n
user_input = input('Решение для задачи с рюкзаком на 7 ячеек (y/n): ')

flag_7 = True
match user_input:
    case 'y':
        BP_SIZE = 7
        BP_W = 2
        BP_L = 4
    case _:
        BP_SIZE = 'undefined'
        flag_7 = False

# Ввод исходных данных
if not flag_7:
    BP_W = int(input('Введите ширину рюкзака: '))
    BP_L = int(input('Введите длину рюкзака: '))


    # Вычисление размера рюкзака (количества ячеек)
    BP_SIZE = BP_W * BP_L

s_points = int(input('Начальное кол-во очков: '))

# Инициализация массива для вещей, которые Том возьмет с собой
backpack = []

# Ввод данных о наличии астмы/заражения
while True:
    asthma = input('Наличие астмы (y/n): ')
    match asthma:
        case 'y':
            asthma = True
            break
        case 'n':
            asthma = False
            break
        case _:
            print('Вы ввели неправильное значение')

while True:
    infection = input('Наличие заражения (y/n): ')
    match infection:
        case 'y':
            infection = True
            break
        case 'n':
            infection = False
            break
        case _:
            print('Вы ввели неправильное значение, повторите попытку')

print('\nНачальное положение:')
print(f'Размер рюкзака: {BP_SIZE}\nНаличие астмы: {asthma}\nНаличие заражения: {infection}')


# Создание класса для предмета, который Том может взять с собой
class Item:
    def __init__(self, icon, size, points, needed):
        # Обозначение предмета
        self.icon = icon  # str expected
        # Занимаемый предметом размер
        self.size = size  # int expected
        # Очки выживания предмета
        self.points = points  # int expected
        # Необходимость предмета (например, при астме или заражении)
        self.needed = needed  # boolean expected

    # Вычисление эффективности предмета
    def get_efficiency(self):
        return self.points/self.size

    # Проверка предмета на обязательность наличия (астма/заражение)
    def check_obligatory(self):
        return self.needed


# Функция добавления предмета в массив
# (мы используем предмет и созданный ранее backpack)
# Функция добавляет кортеж, состоящий из средней эффективности предмета, его иконки,
# размера и необходимости.
def append_item(array, item):
    array.append((round(item.get_efficiency(), 1), item.icon, item.size, item.check_obligatory()))


# Создаем массив для пула предметов
item_arr = []

# Создание предмета "Ингалятор"
# Присвоение True атрибуту needed при астме и False при её отсутствии
inhaler = Item('и', 1, 5, 'undefined')
match asthma:
    case True:
        inhaler.needed = True
        append_item(item_arr, inhaler)
    case False:
        inhaler.needed = False
        append_item(item_arr, inhaler)

# Создание предмета "Антидот"
# Присвоение True атрибуту needed при заражении и False при её отсутствии
radaway = Item('д', 1, 10, 'undefined')
match infection:
    case True:
        radaway.needed = True
        append_item(item_arr, radaway)
    case False:
        radaway.needed = False
        append_item(item_arr, radaway)

# Создание оставшихся предметов
rifle = Item('в', 3, 25, False)
append_item(item_arr, rifle)

pistol = Item('п', 2, 15, False)
append_item(item_arr, pistol)

ammo = Item('б', 2, 15, False)
append_item(item_arr, ammo)

medpack = Item('а', 2, 20, False)
append_item(item_arr, medpack)

knife = Item('н', 1, 15, False)
append_item(item_arr, knife)

axe = Item('т', 3, 20, False)
append_item(item_arr, axe)

amulet = Item('о', 1, 25, False)
append_item(item_arr, amulet)

bottle = Item('ф', 1, 15, False)
append_item(item_arr, bottle)

food = Item('к', 2, 20, False)
append_item(item_arr, food)

crossbow = Item('р', 2, 20, False)
append_item(item_arr, crossbow)

# Сортировка массива по средней эффективности предмета
item_sorted = list(reversed((sorted(item_arr))))


# Берём с собой необходимые предметы, если такие имеются
for i in item_sorted:
    if i[3] == True:
        backpack.append(i[1])
        BP_SIZE -= i[2]
        s_points += i[0] * i[2]
        item_sorted.remove(i)

# Берём все оставшиеся предметы, пока не закончится место в рюкзаке
# Одновременно с этим добавляем Тому очки выживания

# Массив для предметов, которые не берём с собой
item_out = []
while True:
    if len(item_sorted) <= 0:
        break
    if BP_SIZE - item_sorted[0][2] >= 0:
        for i in range(item_sorted[0][2]):
            backpack.append(item_sorted[0][1])
        BP_SIZE -= item_sorted[0][2]
        s_points += item_sorted[0][0] * item_sorted[0][2]
        item_sorted.pop(0)
    # Случай, когда места в рюкзаке не хватает для того, чтобы взять предмет
    elif BP_SIZE - item_sorted[0][2] < 0:
        item_out.append(item_sorted[0])
        item_sorted.pop(0)
        if len(item_sorted) == 0:
            break

# Вычитаем очки выживания за предметы, которые не удалось взять с собой
for i in item_out:
    s_points -= round(i[0] * i[2])

# Создаем двумерный массив
backpack_f = []
for i in range(BP_W):
    backpack_f.append(['' for k in range(BP_L)])

# Наполняем двумерный массив
item_count = 0
for i in range(BP_W):
    for j in range(BP_L):
        if len(backpack) > item_count:
            backpack_f[i][j] = backpack[item_count]
        else:
            backpack_f[i][j] = ' '
        item_count += 1

# Вывод итоговых данных
print('Рюкзак Тома:')
for i in backpack_f:
    print(i)

print('Итоговое кол-во очков:')
print(round(s_points))

if s_points <= 0:
    print('Том, вероятнее всего, не выживет')
else:
    print('Том способен выжить с таким инвентарём')









