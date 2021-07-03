
yearInput = int(input("Введите год:"))
if yearInput % 4 != 0:
    print("Обычный")
elif yearInput % 100 == 0:
    if yearInput % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Високосный")