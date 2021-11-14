while True:
    try:
        a = int(input("Введите первое целое число: "))
    except:
        print("Вы ввели не целое число, ошибка")
        continue
    break

while True:
    try:
        b = int(input("Введите второе целое число: "))
    except:
        print("Вы ввели не целое число, ошибка")
        continue
    break

def minus(c, d):
    return c - d
print("Ответ: ", minus(a, b))