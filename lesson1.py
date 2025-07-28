# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
сторона_3 = 3 # не совсем корректно делать нейминг переменной на каком либо языке кроме английского,
              # но в целом, такую переменную можно вызвать и она будет работать
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + сторона_3 + storona_4
print(perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apples = 4
pears = apples + 5
plums = apples - 2
fruits_sum = apples + pears + plums
print(
    "У нас есть: ",
    f"Яблок - {apples}",
    f"Груш - {pears}",
    f"Слив - {plums}",
    f"Если мы сложим кол-во всех плодов, то получим {fruits_sum}",
    sep="\n"
    )
# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
morning_temp = 5
day_temp = morning_temp - 10
evening_temp = day_temp + 4
print(evening_temp)


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys / 2
today_boys = boys - 1
today_girls = girls - 2
sum_children = today_boys + today_girls
print(sum_children)


# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""

first_book = 8
second_book = first_book + 2
third_book = (first_book / 2) + (second_book / 2)
sum_price = first_book + second_book + third_book
print(sum_price)