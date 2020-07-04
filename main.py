import random
board = [
    '_', '_', '_',
    '_', '_', '_',
    '_', '_', '_'
]
symbols = ['x', 'o']


def display(board):
    print("\n")
    print("    "+board[0] + ' | ' + board[1] + " | " + board[2])
    print("    "+"__________")
    print("    "+board[3] + ' | ' + board[4] + " | " + board[5])
    print("    "+"__________")
    print("    "+board[6] + ' | ' + board[7] + " | " + board[8])
    print("\n")


def game_odds():
    odd1 = board[0] if board[0] == board[1] == board[2] != '_' or board[0] == board[
        4] == board[8] != '_' or board[0] == board[3] == board[6] != '_' else None
    odd2 = board[1] if board[1] == board[4] == board[7] != '_' else None
    odd3 = board[2] if board[2] == board[5] == board[8] != '_' or board[2] == board[4] == board[6] != '_' else None
    odd4 = board[3] if board[3] == board[4] == board[5] != '_' else None
    odd5 = board[6] if board[6] == board[7] == board[8] != '_' else None
    odd6 = '*' if "_" not in board else None
    odds = [odd1, odd2, odd3, odd4, odd5, odd6]
    for odd in odds:
        if odd:
            return odd


def symbol_request():
    while True:
        symbol = input('Do you like to play "X" or "O": ').lower()
        if symbol in symbols:
            return symbol
        else:
            print('invalid symbol!!')


def index_request():
    while True:
        try:
            index = int(input("Where to play [1:9]: "))-1
            if index in range(9) and board[index] not in symbols:
                return index
            else:
                print('invalid play!!')
        except ValueError:
            print('invalid play!!')


def bot_symbol_request(player_symbol):
    bot_symbol = list(set(symbols) - set(player_symbol))
    return bot_symbol[0]


def bot_index_request(player_symbol):
    bot_index = None
    for play in range(9):
        if board[play] not in symbols:
            board[play] = bot_symbol_request(player_symbol)
            if game_odds():
                bot_index = play
            board[play] = "_"
    if bot_index not in range(9):
        for play in range(9):
            if board[play] not in symbols:
                board[play] = player_symbol
                if game_odds():
                    bot_index = play
                board[play] = "_"
    while bot_index not in range(9):
        random_play = random.choice(range(9))
        if board[random_play] not in symbols:
            bot_index = random_play
    return bot_index


def winner_vs_bot(odd, player_symbol, bot_symbol):
    run = True
    if odd:
        display(board)
        if odd == player_symbol:
            print("Congrats!.. You won :)")
        elif odd == bot_symbol:
            print("You lost!.. Better luck next time.")
        else:
            print("----draw----")
        run = False
    return run


def winner_vs_player(odd, player1_symbol, player2_symbol):
    run = True
    if odd:
        display(board)
        if odd == player1_symbol:
            print("Player1 won!!")
        elif odd == player2_symbol:
            print("Player2 won!!")
        else:
            print("----draw----")
        run = False
    return run


def check_play_type():
    valid_input = False
    while not valid_input:
        play_vs_bot = input('Play vs (Bot / Player)? ')
        if play_vs_bot in ['bot', 'player']:
            valid_input = True
            if play_vs_bot == 'bot':
                play = True
            elif play_vs_bot == 'player':
                play = False
        else:
            print('invalid input!!')
    return play


def play_again():
    valid_input = False
    while not valid_input:
        play_again = input('play again (yes/no)? ')
        if play_again in ['yes', 'no']:
            valid_input = True
            if play_again == 'yes':
                play = True
                global board
                board = [
                    '_', '_', '_',
                    '_', '_', '_',
                    '_', '_', '_'
                ]
            elif play_again == 'no':
                play = False
        else:
            print('invalid input!!')
    return play


def play_vs_bot():
    player1_symbol = symbol_request()
    bot_symbol = bot_symbol_request(player1_symbol)
    running = True
    while running:
        # game_loop
        display(board)
        # player's turn
        if running:
            print("Player1's Turn.")
            player1_index = index_request()
            board[player1_index] = player1_symbol
            running = winner_vs_bot(game_odds(), player1_symbol, bot_symbol)
        # bot's turn
        if running:
            bot_index = bot_index_request(player1_symbol)
            board[bot_index] = bot_symbol
            running = winner_vs_bot(game_odds(), player1_symbol, bot_symbol)


def play_vs_player():
    player1_symbol = symbol_request()
    player2_symbol = bot_symbol_request(player1_symbol)
    running = True
    display(board)
    while running:
        # game_loop
        # player1 turn
        if running:
            print("Player1's Turn.")
            player1_index = index_request()
            board[player1_index] = player1_symbol
            display(board)
            running = winner_vs_player(
                game_odds(), player1_symbol, player2_symbol)
        # player2 turn
        if running:
            print("Player2's Turn.")
            player2_index = index_request()
            board[player2_index] = player2_symbol
            display(board)
            running = winner_vs_player(
                game_odds(), player1_symbol, player2_symbol)


play = True
while play:
    vs_bot = check_play_type()
    if vs_bot:
        play_vs_bot()
    else:
        play_vs_player()
    play = play_again()
