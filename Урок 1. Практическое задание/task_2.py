"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
sec_count = int(input("Введите время в секундах: "))
hrs_count = sec_count // 3600
min_count = (sec_count - hrs_count * 3600) // 60
print(f"{sec_count} секунд - это {hrs_count}ч:{min_count}м:{sec_count - hrs_count * 3600 - min_count * 60}с")
