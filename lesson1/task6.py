a = float(input("Введите результат в первый день пробежки: "))
b = float(input("Введите минимальный желаемый результат: "))

if a < b:
    i = 0
    while (a * 1.1 ** (i-1) < b):
        print("{0}-й день: {1:.2f}".format(i + 1, a * 1.1 ** i))
        i += 1

    print("На {0}-й день спортсмен достиг результата — не менее {1} км".format(i, b))
else:
    print("Вы уже достигли желаемого результата")
