import random
import string

def c_place_boat(board, length, symbol):
    placed = False
    attempts = 0
    while not placed and attempts < 100:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        direction = random.randint(1, 4)  # 1 = Up, 2 = Down, 3 = Left, 4 = Right

        if direction == 1 and x - length + 1 >= 0:
            if all(board[x - i][y] == "_" for i in range(length)):
                for i in range(length):
                    board[x - i][y] = symbol
                placed = True

        elif direction == 2 and x + length - 1 <= 9:
            if all(board[x + i][y] == "_" for i in range(length)):
                for i in range(length):
                    board[x + i][y] = symbol
                placed = True

        elif direction == 3 and y - length + 1 >= 0:
            if all(board[x][y - i] == "_" for i in range(length)):
                for i in range(length):
                    board[x][y - i] = symbol
                placed = True

        elif direction == 4 and y + length - 1 <= 9:
            if all(board[x][y + i] == "_" for i in range(length)):
                for i in range(length):
                    board[x][y + i] = symbol
                placed = True

        attempts += 1

def p_place_boat(board, ship_name, ship_length, ship_symbol):
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
                    if all(board[y][x] == "_" for x in range(x1, x2 + 1)):
                        for x in range(x1, x2 + 1):
                            board[y][x] = ship_symbol
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
                    if all(board[y][x] == "_" for y in range(y1, y2 + 1)):
                        for y in range(y1, y2 + 1):
                            board[y][x] = ship_symbol
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

# Setup
c_board = [["_" for _ in range(10)] for _ in range(10)]
p_board = [["_" for _ in range(10)] for _ in range(10)]
fleet = [("Carrier", 5), ("Battleship", 4), ("Cruiser", 3), ("Submarine", 3), ("Destroyer", 2)]
ship_names = {"Ca": "Carrier", "B": "Battleship", "Cr": "Cruiser", "S": "Submarine", "D": "Destroyer"}
name_to_code = {v: k for k, v in ship_names.items()}

letter_to_index = {chr(i): i - 65 for i in range(65, 75)}

for name, size in fleet:
    code = name_to_code[name]
    c_place_boat(c_board, size, code)

"""
print_board(p_board)
for name, size in fleet:
    code = name_to_code[name]
    p_place_boat(p_board, name, size, code)

print("\nYour ship placements:")
print_board(p_board)
"""

print("\nComputer ship placements:")
print_board(c_board)

def get_target_coordinates():
    target_x = int(input("Enter the x coordinate of the target location (1-10): "))
    while target_x < 1 or target_x > 10:
        print("Invalid input.")
        target_x = int(input("Enter the x coordinate of the target location (1-10): "))

    target_y = input("Enter the y coordinate of the target location (A-J): ").strip().upper()
    while target_y not in "ABCDEFGHIJ":
        print("Invalid input.")
        target_y = input("Enter the y coordinate of the target location (A-J): ").strip().upper()

    return target_x - 1, ord(target_y) - 65

# Begin
game_board = [["_" for _ in range(10)] for _ in range(10)]
c_ship_health = {"Ca": 5, "B": 4, "S": 3, "Cr": 3, "D": 2}
player_turn = True
game_over = False

while not game_over:
    if player_turn:
        x, y = get_target_coordinates()

        if game_board[y][x] in ("H", "M"):
            print("You already fired at this location.")
            continue

        if c_board[y][x] != "_":
            ship = c_board[y][x]
            ship_code = c_board[y][x]
            print(f"Hit! You hit the computer's {ship_names[ship_code]}!")
            game_board[y][x] = "H"
            c_ship_health[ship_code] -= 1

            if c_ship_health[ship_code] == 0:
                print(f"You sunk the computer's {ship_names[ship_code]}!")
        else:
            print("Miss!")
            game_board[y][x] = "M"

        print_board(game_board)

        if all(health == 0 for health in c_ship_health.values()):
            print("Congratulations! You sank all the computer's ships!")
            game_over = True

        #player_turn = False