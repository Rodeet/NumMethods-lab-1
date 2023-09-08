eps = 0.01


def f(x):
    return (x - 2) * (x - 3)**2 * (x - 7)


def dih(x0, x1):
    if f(x0) * f(x1) < 0:
        if x0 > x1:
            x0, x1 = x1, x0
        x2 = (x0 + x1) / 2
        if f(x0)*f(x2) <= 0:
            if abs(f(x0)*f(x2)) < eps and abs(x0 - x2) < eps:
                return x2
            else:
                return dih(x0, x2)
        elif f(x1)*f(x2) <= 0:
            if abs(f(x1)*f(x2)) < eps and abs(x1 - x2) < eps:
                return x2
            else:
                return dih(x2, x1)
    else:
        print("Значения функций в заданных точках границ должны быть противоположны по знаку.")
        return None


if __name__ == "__main__":
    print("Данный метод дихотомии находит корень уравнения f(x) на промежутке [a, b]")
    a = float(input("Введите левую границу (a): "))
    b = float(input("Введите правую гранитицу (b): "))
    ans = dih(a, b)
    print("Ответ: x = %.2f" % ans)
