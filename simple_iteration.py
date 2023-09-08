eps = 0.01


def iteration(a):
    x0 = a
    x1 = 1 / 2 * (a / x0 + x0)
    while abs(x1 - x0) > eps:
        x0 = x1
        x1 = 1 / 2 * (a / x0 + x0)
    return x1


if __name__ == "__main__":
    print("Данный метод простой итерации вычисляет корень уравнения: x = √a")
    a = float(input("Введите a: "))
    ans = iteration(a)
    print("Ответ: x = %.2f" % ans)

