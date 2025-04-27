def find_positions(s, t):

    positions = [] #Создает пустой список для хранения данных
    for i in range(len(s) - len(t) + 1): #  Цикл идет когда оставшаяся часть s станет короче, чем t.
        if s[i:i+len(t)] == t: # Сравниваем подстроку s с t/ Внутри цикла извлекается подстрока s длиной len(t)
            positions.append(i) # Добавляем индекс 

    return positions


s = input("what s?")  # Строка, в которой ищем
t = input("what t? ") # Подстрока, которую ищем

positions = find_positions(s, t)

# Выводим результаты
print(*positions)
