# Tic-Tac-Toe Game
The Python code is a simple implementation of a tic-tac-toe game. The code allows two players to take turns entering their positions (from 1 to 9) on the game board. 
The game board is displayed after each move. The program checks for a winner after every move and detects a draw if there are no empty spaces left on the board. 
If a player wins or the game ends in a draw, the program asks if the player want to play again. If the players choose to continue, the game board is reset, and the game continues. 
If the players choose not to continue, the program ends with a goodbye message.

Note: The code is specific to IPython/Jupyter Notebook due to the usage of `clear_output()` function for clearing the cell output.

Some useful functions that are used in this python file are as follows:
1. `drawBoard(board)`: This function takes the current state of the game board as input (a dictionary representing the board positions and markers) and prints the tic-tac-toe grid.
   It visually displays the current state of the game board after each move.

3. `user_position(board)`: This function prompts the user to input their desired position (from 1 to 9) on the game board. It ensures that the input is valid (i.e., within the range of 1 to 9 and
    the chosen position is not already filled) and returns the chosen position.

3. `marker()`: This function asks the user to input their marker choice, either 'X' or 'O'. It validates the input and ensures the user selects a valid marker. The function returns the chosen marker.

4. `check_winner(board, marker)`: This function checks the game board for a winning combination based on the specified marker ('X' or 'O').
  It compares the current state of the board with predefined winning combinations. If a winning combination is found for the given marker, the function returns `True`; otherwise, it returns `False`.

The `drawBoard()` function handles the visual representation of the game, while `user_position()` and `marker()` functions ensure valid user inputs. 
The `check_winner()` function is crucial for determining if a player has won the game, enabling the program to make decisions about the game's outcome.
