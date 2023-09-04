gameboard = [[" x", " x", " x"],
             [" x", " x", " x"],
             [" x", " x", " x"],
             ]

n = len(gameboard)
for row in gameboard:
    n -= 1
    print(f" |".join(row))
    if n != 0:
        print("-----------")

