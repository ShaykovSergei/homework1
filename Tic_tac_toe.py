def greeting():
    print('Х0Х0Х0Х0Х0Х0Х0Х0Х0Х0')
    print('|  Начинаем игру   |')
    print('| Крестики-Нолики! |')
    print('--------------------')
    print('|  Правила  игры:  |')
    print('--------------------')
    print('|   x - строка     |')
    print('|   y - колонка    |')
    print('|  Ввод координат: |')
    print('|x y (через пробел)|')
    print('0Х0Х0Х0Х0Х0Х0Х0Х0Х0Х')


def show():
    print('     0   1   2')
    print('   -------------')
    for i, row in enumerate(field):
        row_str = f"{i} | {' | '.join(row)} | "
        print(row_str)
        print('   -------------')


def ask():
    while True:
        coords = input('Ваш ход:  ').split()
        print()
        if len(coords) != 2:
            print('Введите две координаты через пробел')
            continue
        x, y = coords
        if not ''.join(coords).isdigit():
            print('Введите только числа')
            continue
        x, y = int(x), int(y)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Введите координаты от 0 до 2')
            continue
        if field[x][y] != ' ':
            print('Клетка уже занята')
            continue
        return x, y

  
def game():
    count = 0
    while True:
        count += 1
        if count % 2 == 1:
            print('Ходит крестик!')
        else:
            print('Ходит нолик!')
        x, y = ask()
        if count % 2 == 1:
            field[x][y] = 'Х'
        else:
            field[x][y] = '0'
        show()
        if check_win():
            break
        if count == 9:
            print('Ничья!')
            break


def check_win():
    win_coords = (((0, 0), (0, 1), (0, 2)),((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)),((0, 2), (1, 1), (2, 0)))
    combination = []
    for win in win_coords:
        combination.append(''.join([field[w[0]][w[1]] for w in win]))
               
    for comb in combination:
        if comb == 'ХХХ':
            print()
            print('Выиграл крестик! (Х)')
            return True
        elif comb == '000':
            print()
            print('Выиграл нолик! (0)')
            return True

    return False


def start():
    while True:
        greeting()
        show()
        game()
        print('====================')
        cont = input('Продолжить игру? Да - Y, Нет - any key: ')
        if cont.lower() != 'y':
            print('Игра завершена!')
            break
        else:
            global field
            field = [[" "] * 3 for _ in range(3)]


field = [[" "] * 3 for _ in range(3)]
start()
