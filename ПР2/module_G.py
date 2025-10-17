import random

def generate_surname(is_female):
    common_surnames = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов", "Попов", "Васильев", "Соколов", "Михайлов", "Фёдоров"]
    prefixes = ["Бело", "Ново", "Старо", "Красно", "Черно", "Мало", "Велико", "Добро"]
    bases = ["вин", "бор", "град", "мир", "род", "слав", "поль", "рус", "ход", "яр"]
    suffixes_male = ["ов", "ев", "ин", "ский", "цкий", "ников", "ич", "енко"]
    suffixes_female = ["ова", "ева", "ина", "ская", "цкая", "никова", "ич", "енко"]

    if random.random() < 0.5:
        surname = random.choice(common_surnames)
        if is_female:
            return surname+"а"
    else:
        surname = random.choice(prefixes) + random.choice(bases) + random.choice(
            suffixes_male if not is_female else suffixes_female)

    return surname

def generate_full_name():
    name_index = random.randint(0, len(names) - 1)
    name = names[name_index]

    is_female = name_index < 20
    initial = random.choice(name)[0].upper() + "."
    surname = generate_surname(is_female)
    return f"{name} {initial} {surname}"

def generate_born_date():
    year = random.randint(1960,2011)
    day = random.randint(1,31)
    moth = random.randint(1,12)
    if moth == 2 and day>28 and year%4==0 and year%100!=0:
        day = 29
    elif moth == 2 and day>28:
        day = 28
    elif (moth == 4 or moth == 6 or moth == 11 or moth == 9) and day>30:
        day = 30
    return f"{day}.{moth}.{year}"

def generatepasnum():
    seria1 = random.randint(10,50)
    seria2 = random.randint(10,20)
    num = random.randint(0,999999)
    for i in range(6):
        if len(str(num)) < 6:
            num = "0"+str(num)
    return f"{seria1} {seria2} {num}"

def displaypasinfo(name,num,borndate):
    print(f"ФИО - {name}")
    print(f"Дата рождения - {borndate}")
    print(f"Серия и Номер - {num}")

def validitycheck(pasinfo):
    if int(pasinfo[1].split(" ")[2])<0 or int(pasinfo[1].split(" ")[2])>999999:
        return False
    elif int(pasinfo[1].split(" ")[1])>20 or int(pasinfo[1].split(" ")[1])<10: 
        return False
    elif int(pasinfo[1].split(" ")[0])>50 or int(pasinfo[1].split(" ")[0])<10: 
        return False
    else: return True

'''
names = ["София", "Анна", "Мария", "Ева", "Виктория", "Полина", "Алиса", "Варвара", "Василиса", "Александра", "Елизавета", "Арина", "Ксения", "Екатерина", "Дарья", "Милана", "Анастасия", "Мирослава", "Вероника", "Кира", "Михаил", "Александр", "Максим", "Артем", "Марк", "Лев", "Иван", "Матвей", "Даниил", "Дмитрий", "Тимофей", "Роман", "Мирон", "Мухаммад", "Кирилл", "Егор", "Илья", "Алексей", "Константин", "Федор"]
a = generate_full_name()
b = generate_born_date()
print("Дата:",b)
c = generatepasnum()
displaypasinfo(a,b,c)
d = [a, c, b]
print(validitycheck(d))
'''
