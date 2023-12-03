from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # 1.-2. Підготовка Даних/Отримання Поточної Дати
    today = datetime.today().date()
    birthdays_by_day = {}

    # 3.-4а. Перебір Користувачів та конвертація дати
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        # 4b. Оцінка Дати на Цей Рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # 4c. Порівняння з Поточною Датою
        delta_days = (birthday_this_year - today).days

        # 4d.-5. Визначення Дня Тижня/Зберігання Результату
        if delta_days < 7:
            day_of_week = (today + timedelta(days=delta_days)).strftime("%A")
            birthdays_by_day.setdefault(day_of_week, []).append(name)

    # 6. Виведення Результату
    for day, names in birthdays_by_day.items():
        print(f"{day}: {', '.join(names)}")

# Приклад використання:
users = [
    {"name": "Bill Gates", "birthday": datetime(1999, 12, 8)},
    {"name": "Jill Valentine", "birthday": datetime(1933, 12, 8)},
    {"name": "Kim Kardashian", "birthday": datetime(1945, 12, 3)},
    {"name": "Jan Koum", "birthday": datetime(1939, 8, 25)},
]

get_birthdays_per_week(users)
