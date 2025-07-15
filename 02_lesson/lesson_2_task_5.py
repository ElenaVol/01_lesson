def month_to_season(month):
    if month in (12, 1, 2):
        print("Зима")
    if month in (3, 4, 5):
        print("Весна")
    if month in (6, 7, 8):
        print("Лето")
    if month in (9, 10, 11):
        print("Осень")
    else:
        print("Некорректный номер месяца")

month_to_season(15)
