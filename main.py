"""
Key:
0 = Empty
1 = Occupied
2 = Hit
"""

import random
import string

c_board = [[0 for _ in range(10)] for _ in range(10)]
p_board = [[0 for _ in range(10)] for _ in range(10)]
fleet = [("Carrier", 5), ("Battleship", 4), ("Cruiser", 3), ("Submarine", 3), ("Destroyer", 2)]

def c_place_boat(board, length):
    placed = False
    attempts = 0
    while not placed and attempts < 100:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        direction = random.randint(1, 4)  # 1 = Up, 2 = Down, 3 = Left, 4 = Right

        if direction == 1 and x - length + 1 >= 0:
            if all(board[x - i][y] == 0 for i in range(length)):
                for i in range(length):
                    board[x - i][y] = 1
                placed = True
        elif direction == 2 and x + length - 1 <= 9:
            if all(board[x + i][y] == 0 for i in range(length)):
                for i in range(length):
                    board[x + i][y] = 1
                placed = True
        elif direction == 3 and y - length + 1 >= 0:
            if all(board[x][y - i] == 0 for i in range(length)):
                for i in range(length):
                    board[x][y - i] = 1
                placed = True
        elif direction == 4 and y + length - 1 <= 9:
            if all(board[x][y + i] == 0 for i in range(length)):
                for i in range(length):
                    board[x][y + i] = 1
                placed = True
        attempts += 1

def p_place_boat(board, ship_name, ship_length):
    valid = False
    while not valid:
        direction = input(
            f"\nHow would you like to place your {ship_name} (length {ship_length})? (H for horizontally, V for vertically): ").strip().upper()

        if direction == "H":
            y_letter = input("Enter a letter from A-J for the row: ").strip().upper()
            x_start = input(f"Enter the *first* column (1-10) for your {ship_name}: ")
            x_end = input(f"Enter the *last* column (1-10) for your {ship_name}: ")

            if y_letter in letter_to_index and x_start.isdigit() and x_end.isdigit():
                y = letter_to_index[y_letter]
                x1 = min(int(x_start), int(x_end)) - 1
                x2 = max(int(x_start), int(x_end)) - 1

                if 0 <= x1 <= x2 <= 9 and x2 - x1 + 1 == ship_length:
                    if all(board[y][x] == 0 for x in range(x1, x2 + 1)):
                        for x in range(x1, x2 + 1):
                            board[y][x] = 1
                        valid = True
                    else:
                        print("Invalid placement: overlapping another ship.")
                else:
                    print("Invalid horizontal placement: wrong length or out of bounds.")
            else:
                print("Invalid input format.")

        elif direction == "V":
            x_input = input("Enter the column number from 1-10: ")
            y_start = input(f"Enter the *first* row letter (A-J) for your {ship_name}: ").strip().upper()
            y_end = input(f"Enter the *last* row letter (A-J) for your {ship_name}: ").strip().upper()

            if x_input.isdigit() and y_start in letter_to_index and y_end in letter_to_index:
                x = int(x_input) - 1
                y1 = min(letter_to_index[y_start], letter_to_index[y_end])
                y2 = max(letter_to_index[y_start], letter_to_index[y_end])

                if 0 <= y1 <= y2 <= 9 and y2 - y1 + 1 == ship_length:
                    if all(board[y][x] == 0 for y in range(y1, y2 + 1)):
                        for y in range(y1, y2 + 1):
                            board[y][x] = 1
                        valid = True
                    else:
                        print("Invalid placement: overlapping another ship.")
                else:
                    print("Invalid vertical placement: wrong length or out of bounds.")
            else:
                print("Invalid input format.")

        else:
            print("Direction must be 'H' or 'V'.")

def print_board(board):
    print("\n   ", end="")
    for col in range(1, 11):
        print(f"{col:2}", end=" ")
    print()
    for i in range(10):
        print(f"{string.ascii_uppercase[i]}  ", end="")
        for j in range(10):
            print(f"{board[i][j]:2}", end=" ")
        print()
    print()

letter_to_index = {letter: idx for idx, letter in enumerate(string.ascii_uppercase[:10])}

for ship_name, ship_length in fleet:
    c_place_boat(c_board, ship_length)

for name, length in fleet:
    print_board(p_board)
    p_place_boat(p_board, name, length)
