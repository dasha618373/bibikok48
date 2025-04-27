def fibonacci_rabbits (n, k):
    # Инициализация начальных условий
    F1, F2 = 1, 1

    # Расчет количества пар кроликов на n-й месяц
    for i in range(3, n + 1):
        F_current = F2 + k * F1
        F1 = F2
        F2 = F_current

    return F2

print(fibonacci_rabbits (5, 3))
