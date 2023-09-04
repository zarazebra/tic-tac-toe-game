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



