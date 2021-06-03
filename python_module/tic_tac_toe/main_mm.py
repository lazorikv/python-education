import logging
from random import choice
import sys
import constants
import exit_game

board = list(range(1, 10))  # list of numbers for cells
count = 1
variable = {}
for i in range(1, 4):
    for j in range(1, 4):
        variable[(i, j)] = count
        count += 1

VARIANT = None
NAME1 = None
NAME2 = None

class Menu:
    """Class menu for printing menu"""
    def __init__(self):
        self.name3 = None

    @staticmethod
    def start_choice() -> int:
        print('\nНачать игру - 1\nПосмотреть результаты предыдущих игр - 2\n'
              'Очистить логи - 3\nВыйти из игры - 4')
        while True:
            try:
                char = int(input('Введите цифру: '))
                if char not in [1, 2, 3, 4]:
                    raise ValueError
            except ValueError:
                continue
            return char

    @staticmethod
    def turn_mode() -> int:
        mode = int(input('PvP - 1\nPlayer vs Computer - 2\nEnter: '))
        return mode

    def choice(self):
        global VARIANT
        global NAME1, NAME2
        while True:
            try:
                start = self.start_choice()
                if start == 1:
                    VARIANT = self.turn_mode()
                    # if VARIANT == 1:
                    #     players_names = Names
                    #     NAME1, NAME2 = players_names.naming()
                    if VARIANT == 2:
                        self.name3 = input('Enter your name: ')
                    main()
                elif start == 2:  # open logging file
                    with open('myapp.log', 'r') as file:
                        line = file.read()
                    if len(line) == 0:
                        print("Список пуст\n")
                    else:
                        print(line)
                        continue
                elif start == 3:  # clean logging file
                    with open('myapp.log', 'w'):
                        pass
                    print('Список успешно очищен!!!\n')
                    continue
                elif start == 4:  # quit
                    exit_game.exit_from_game()
                else:
                    print('\nВведите нужную цифру!!!')
                    continue
            except (ValueError, IndexError):
                print('Введите нужную цифру!!!')
                continue


class AskNumber:

    def __init__(self, question, a_board):
        self.a_board = a_board
        self.question = question

    def ask_number(self):
        """Ask for a number within a range."""
        response = int(input(self.question))
        char = True
        while char:
            if str(self.a_board[response-1]) not in 'XO':
                char = False
                return response
            else:
                print("\nThat square is already occupied. Choose another.\n")
                self.ask_number()


class Piece:

    def __init__(self):
        self.string = 'XO'

    def pieces(self):
        """Determine if player or computer goes first."""
        char = choice(self.string)
        play1 = char
        play2 = self.string.replace(char, '')
        return play1, play2


class Names:

    def __init__(self):
        pass

    @staticmethod
    def naming():
        name1 = input('Enter name first player: ')
        name2 = input('Enter name second player: ')
        return name1, name2


class BuildBoard:

    def __init__(self, b_board):
        self.b_board = b_board

    # @staticmethod
    # def new_board():
    #     """Create new game board."""
    #     d_board = list(range(1, 10))
    #     print("-" * 13)
    #     for i in range(3):
    #         print("|", d_board[0 + i * 3], "|", d_board[1 + i * 3], "|", d_board[2 + i * 3], "|")
    #         print("-" * 13)
    #     return d_board

    def display_board(self):
        """Display game board on screen."""
        print("-" * 13)
        for i in range(3):
            print("|", self.b_board[0 + i * 3], "|", self.b_board[1 + i * 3], "|", self.b_board[2 + i * 3], "|")
            print("-" * 13)


def legal_moves(l_board):
    """Create list of legal moves."""
    moves = []
    for square in range(constants.NUM_SQUARES - 1):
        if str(l_board[square]) not in 'XO':
            moves.append(square)
    return moves


class Win:

    def __init__(self, c_board):
        self.c_board = c_board
        self.count = 0

    def winner(self):
        """Determine the game winner."""
        self.count = 0
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                     (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))  # victory options
        for each in win_coord:
            if self.c_board[each[0]] == self.c_board[each[1]] == self.c_board[each[2]]:  # check for victory
                return self.c_board[each[0]]
        for elem in self.c_board:
            a = str(elem)
            if a.isdigit():
                self.count += 1
        if self.count == 0:
            return constants.TIE
        return None


class Addplayers:

    def __init__(self):
        self.play1_sign = None
        self.play2_sign = None
        self.sm_dict = {player1: NAME1, player2: NAME2}
        self.stat = {NAME1: 0, NAME2: 0}

    def add_p(self, win_char):
        self.stat[self.sm_dict[win_char]] += 1
        return self.stat


class Moves:

    def __init__(self, eboard, play1_char, play2_char):
        self.eboard = eboard
        self.play1_char = play1_char
        self.play2_char = play2_char

    def human_move(self):
        """Get human move."""
        turn = AskNumber(f"Where will you move {self.play1_char}? (1-9): ", self.eboard)
        move = turn.ask_number()
        board[move-1] = self.play1_char

    def player2_move(self):
        """Make computer move."""
        second_turn = AskNumber(f"Where will you move {self.play2_char}? "
                                f"(1-9): ", self.eboard)
        move = second_turn.ask_number()
        board[move - 1] = self.play2_char


class CompTurn:

    def __init__(self):
        pass

    @staticmethod
    def minimax(board, depth, is_ai_turn):
        some_player = Win(board)
        if some_player.winner() == player2:
            return scores[player2]
        if some_player.winner() == player1:
            return scores[player1]
        if some_player.winner() == constants.TIE:
            return scores['draw']
        if is_ai_turn:
            # выбираем ход который нам выгодней
            best_score = - sys.maxsize
            for elem in range(constants.NUM_SQUARES-1):
                if str(board[elem]) not in 'XO':
                    label = board[elem]
                    board[elem] = player2
                    score = CompTurn.minimax(board, depth + 1, constants.USER_TURN)
                    board[elem] = label
                    best_score = max(best_score, score)
        else:
            # противник выбирает ход который нам не выгоден
            best_score = sys.maxsize
            for elem in range(constants.NUM_SQUARES-1):
                if str(board[elem]) not in 'XO':
                    a = board[elem]
                    board[elem] = player1
                    score = CompTurn.minimax(board, depth + 1, constants.AI_TURN)
                    board[elem] = a
                    best_score = min(best_score, score)
        return best_score

    @staticmethod
    def get_computer_position():
        print('I will move')
        move = None
        best_score = -sys.maxsize
        for elem in range(constants.NUM_SQUARES-1):
            if str(board[elem]) not in 'XO':
                past = board[elem]
                board[elem] = player2
                score = CompTurn.minimax(board, 0, constants.USER_TURN)
                board[elem] = past
                if score > best_score:
                    best_score = score
                    move = elem

        return move


class RestartGame:

    def __init__(self):
        self.count = 0

    def restart(self):
        self.count += 1
        main()


def next_turn(turn):
    """Switch turns."""
    if turn == constants.X:
        return constants.O
    else:
        return constants.X


def congrat_winner(the_winner, play_2, play_1):
    """Congratulate the winner."""
    if the_winner != constants.TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")

    if the_winner == play_2:
        print('player2 - win')
        # logging.debug(f'Winner - , who put - {player2}')

    elif the_winner == play_1:
        print("player1 - win")
        # logging.debug(f'Winner - , who put {player1} ')

    elif the_winner == constants.TIE:
        print("TIE")


def main():
    global board
    win = False
    turn = constants.X
    s_play = Win(board)
    moving = Moves(board, player1, player2)
    some_board = BuildBoard(board)
    while not win:
        some_board.display_board()
        if turn == player1:
            moving.human_move()
        else:
            if VARIANT == 1:
                moving.player2_move()
            if VARIANT == 2:
                ai = CompTurn
                move = ai.get_computer_position()
                board[move] = player2
        if s_play.winner():
            win = True
        turn = next_turn(turn)
    some_board.display_board()
    the_winner = s_play.winner()
    congrat_winner(the_winner, player2, player1)
    if VARIANT == 1:
        while True:
            try:
                answer = input('Do you want continue game? (y/n)').lower()
                if answer == 'y':
                    board = list(range(1, 10))  # list of numbers for cells
                    stat[sm_dict[the_winner]] += 1
                    print('Score:')
                    for key, value in stat.items():
                        print(f'{key}: {value}\n')
                    RestartGame().restart()
                elif answer == 'n':
                    exit_game.exit_from_game()
                else:
                    raise ValueError
            except ValueError:
                print('Enter incorrect. Try again')
                continue



player1, player2 = Piece().pieces()
players = Addplayers()
scores = {
        player1: -100,
        player2: 100,
        'draw': 0
    }
grand = Menu()
grand.choice()
sm_dict = {player1: NAME1, player2: NAME2}
stat = {NAME1: 0, NAME2: 0}


# sm_dict = {player1: NAME1, player2: NAME2}
# stat = {NAME1: 0, NAME2: 0}  # dict for statistic of the games

input("\n\nPress the enter key to quit.")
