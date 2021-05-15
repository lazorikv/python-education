"""Tic - tac - toe game for 2 gamers. Format: enter the number
in which you want to put your sign - X or O"""

import logging

print("$" * 10, " Крестики-нолики для двух игроков ", "$" * 10)

board = list(range(1, 10))  # list of numbers for cells

# logging victories into myapp.log
logging.basicConfig(level=logging.DEBUG, filename='myapp.log', format='%(asctime)s: %(message)s')

COUNT = 0  # count for replays


def menu():
    """Game menu. User enter number into variable - char"""

    print('\nНачать игру - 1\nПосмотреть результаты предыдущих игр - 2\n'
          'Очистить логи - 3\nВыйти из игры - 4')
    char = input('Введите цифру: ')
    try:
        if char == '1':  # start game
            main(board)
        elif char == '2':  # open logging file
            with open('myapp.log', 'r') as file:
                line = file.read()
            if len(line) == 0:
                print("Список пуст\n")
            else:
                print(line)
            menu()
        elif char == '3':  # clean logging file
            with open('myapp.log', 'w'):
                pass
            print('Список успешно очищен!!!\n')
            menu()
        elif char == '4':  # quit
            exit_from_game()
        else:
            print('\nВведите нужную цифру!!!')
            menu()
    except (ValueError, IndexError):
        print('Введите нужную цифру!!!')
        menu()


def draw_board(d_board):
    """draw board in console"""
    print("-" * 13)
    for i in range(3):
        print("|", d_board[0 + i * 3], "|", d_board[1 + i * 3], "|", d_board[2 + i * 3], "|")
        print("-" * 13)


def take_input(player_token, sub_board):
    """the player's turn. replacing a digit in a shape with a sign"""
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)  # Int check
        except Exception:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= 9:
            if str(sub_board[player_answer - 1]) not in "XO":
                sub_board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(c_board):
    """Check game moment for win"""
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))  # victory options
    for each in win_coord:
        if c_board[each[0]] == c_board[each[1]] == c_board[each[2]]:  # check for victory
            return c_board[each[0]]
    return False


def restart_game(winner):
    """In case of victory, the function implements
     a replay with statistics recording"""

    print('Играть заново - 1\nВыйти - 2')
    char = int(input('Введите число: '))
    global COUNT
    try:
        if char == 1:
            COUNT += 1
            stat[sm_dict[str(winner)]] += 1
            print('Результат:')
            for key, value in stat.items():
                print(f'{key}: {value}\n')
            main(board)
        elif char == 2:
            exit_from_game()
        else:
            print('Введите нужную цифру!!!')
            restart_game(winner)
    except ValueError:
        print('Введите нужную цифру!!!')
        restart_game(winner)


def exit_from_game():
    """Exit from game"""
    raise SystemExit(1)


def main(s_board):
    """Implements the process of the game. Checks the number of
    moves to determine the state of the game"""

    global board
    counter = 0  # counter for determining the turn of the move
    win = False
    while not win:
        draw_board(s_board)
        if counter % 2 == 0:  # if the counter is even, then move X, if odd - О
            take_input("X", board)
        else:
            take_input("O", board)
        counter += 1
        if counter > 4:  # min count of moves for win - 4
            tmp = check_win(s_board)
            if tmp:
                print(sm_dict[str(tmp)], "выиграл!")
                logging.debug(f'Победил - {sm_dict[str(tmp)]}, который ставил - {tmp}')
                win = True
                board = list(range(1, 10))
                restart_game(tmp)
        if counter == 9:  # if counter = 9 and the game is not over - draw
            print("Ничья!")
            break


name1 = input('Введите имя игрока1: ')
name2 = input('Введите имя игрока2: ')
sm_dict = {'X': name1, 'O': name2}  # dict for init players
stat = {name1: 0, name2: 0}  # dict for statistic of the games
menu()
