# Clear input function (specific to IPython/Jupyter Notebook)
from IPython.display import clear_output

# Initial game board
theboard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' '}

# Function to draw the board
def drawBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

# Function to get user position
def user_position(board):
    possible_positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    while True:
        current_position = input('Select your position: ')
        
        if current_position in possible_positions and board[current_position] == ' ':
            return current_position
        else:
            clear_output()
            print("Sorry, the position is already filled or invalid. Please choose an empty position in the range (1 to 9).")

# Function to get user marker
def marker():
    possible_markers = ['X', 'O']
    
    while True:
        move = input("Make your Move [X or O]: ").upper()
        
        if move in possible_markers:
            return move
        else:
            clear_output()
            print("Sorry, I didn't understand. Please make sure to choose X or O.")

def check_winner(board, marker):
    # Define all possible winning combinations
    winning_combinations = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        ['7', '4', '1'],
        ['8', '5', '2'],
        ['9', '6', '3'],
        ['7', '5', '3'],
        ['9', '5', '1']
    ]
    
    # Check if any winning combination is found for the given marker
    for combination in winning_combinations:
        if all(board[position] == marker for position in combination):
            return True
    
    return False

while True:
    # existing code for getting user position and marker
    chosen_position = user_position(theboard)
    user_marker = marker()

    # Update the game board
    theboard[chosen_position] = user_marker

    # Draw the updated board
    drawBoard(theboard)

    # Check for a winner
    if check_winner(theboard, user_marker):
        print(f'Congratulations! Player {user_marker} wins!')
        
        play_again = input('Do you want to play again? (yes/no): ').lower()
        if play_again == 'yes':
            theboard = {'7': ' ' , '8': ' ' , '9': ' ' ,
                        '4': ' ' , '5': ' ' , '6': ' ' ,
                        '1': ' ' , '2': ' ' , '3': ' '};
            continue  # Reset the game and continue the loop
        else:
            print('Thanks for playing! Goodbye!')
            break  # End the game loop if the player doesn't want to play again
            
    else:
        if ' ' not in theboard.values():
            print('It\'s a draw! No one wins.')
            play_again = input('Do you want to play again? (yes/no): ').lower()
            if play_again == 'yes':
                theboard = {'7': ' ' , '8': ' ' , '9': ' ' ,
                            '4': ' ' , '5': ' ' , '6': ' ' ,
                            '1': ' ' , '2': ' ' , '3': ' '};
                continue  # Reset the game and continue the loop
            else:
                print('Thanks for playing! Goodbye!')
                break  # End the game loop if the player doesn't want to play again
            
