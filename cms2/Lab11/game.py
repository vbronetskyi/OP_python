"""game x-o. Lab11.3"""
from board import Board

def play_game():
    """play_game with board"""
    board = Board()

    print("Welcome to Game!")
    print(board)

    while board.get_status() == 'continue':
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))

            board.make_move((row, col), 'x')
            print(board)

            if board.get_status() != 'continue':
                break

            print("Computer's turn...")
            board.make_computer_move()
            print(board)
        except (ValueError, IndexError) as e:
            print("Invalid move:", str(e))

    result = board.get_status()
    if result == 'x':
        print("Congratulations! You won!")
    elif result == '0':
        print("Computer wins!")
    else:
        print("It's a draw!")

play_game()
