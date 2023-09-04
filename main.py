title = """
___    __     ___       __     ___  __   ___ 
 |  | /  `     |   /\  /  `     |  /  \ |__  
 |  | \__,     |  /~~\ \__,     |  \__/ |___ 
                                             
"""

gameboard = [["  ", "  ", "  "],
             ["  ", "  ", "  "],
             ["  ", "  ", "  "],
             ]

continue_game = True

while continue_game:
    print(title)
    print("Welcome to the Tic Tac Toe Game")

    player1 = input("Which player do you want to be - 'X' or 'O'?: ").upper()
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    n = len(gameboard)
    for row in gameboard:
        n -= 1
        print(f" |".join(row))
        if n != 0:
            print("-----------")
    print("To play, you have to choose the location with row and column, e.g. first row third column - 13")
    choice_player1 = input("Where do you wanna play?: ")
    pos_player1 = list(choice_player1)
    row_p1 = int(pos_player1[0]) - 1
    column_p1 = int(pos_player1[1]) - 1
    gameboard[row_p1][column_p1] = player1

    n = len(gameboard)
    for row in gameboard:
        n -= 1
        print(f" |".join(row))
        if n != 0:
            print("-----------")

