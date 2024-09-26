class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    def play(self, game_board, position):
        game_board[position] = self.symbol
class GameBoard:
    def __init__(self, size):  
        self.size = size
        self.grid = [' ' for _ in range(size * size)]
    def show(self):
        for i in range(self.size):
            row = " | ".join(self.grid[i * self.size:(i + 1) * self.size])
            print(row)
            if i < self.size - 1:
                print("-" * (self.size * 5 - 3))  # Adjust dashes based on the size
    def check_winner(self, player):
        winning_combinations = []
        # rows
        for i in range(self.size):
            winning_combinations.append([i * self.size + j for j in range(self.size)])
        # columns
        for j in range(self.size):
            winning_combinations.append([i * self.size + j for i in range(self.size)])
        # diagonals
        winning_combinations.append([i * (self.size + 1) for i in range(self.size)])  # \
        winning_combinations.append([(i + 1) * (self.size - 1) for i in range(1, self.size + 1)])
        for combo in winning_combinations:
            if all(self.grid[i] == player.symbol for i in combo):
                return True
        return False

    def is_filled(self):
        return ' ' not in self.grid

class TicTacToeGame:
    def __init__(self, player1, player2, size): 
        self.game_board = GameBoard(size)
        self.players = [player1, player2]
        self.active_player = player1

    def switch_player(self):
        self.active_player = self.players[1] if self.active_player == self.players[0] else self.players[0]

    def start(self):
        board_size = self.game_board.size * self.game_board.size
        while not self.game_board.is_filled():
            self.game_board.show()
            try:
                move = int(input(f"{self.active_player.name}, choose your box (1-{board_size}).")) - 1
                if move < 0 or move >= board_size:
                    raise IndexError("Out of range")
                if self.game_board.grid[move] == ' ':
                    self.active_player.play(self.game_board.grid, move)
                    if self.game_board.check_winner(self.active_player):
                        self.game_board.show()
                        print(f"Congratulations, {self.active_player.name} wins the game!")
                        break
                    self.switch_player()
                else:
                    print("The spot is already taken. Choose another one.")
            except (ValueError, IndexError): 
                print("Invalid input. Please enter the correct number")
                
        if self.game_board.is_filled():
            self.game_board.show()
            print("It's a draw!")
            print("Game Over....")

def main():

    print("................Welcome to Tic Tac Toe Game!...................")
    board_size = int(input("Enter the board size (select any number): "))
    player1_name = input("Enter name for Player 1: ")
    player2_name = input("Enter name for Player 2: ")

    player1 = Player(player1_name, 'X')
    player2 = Player(player2_name, 'O')
    game = TicTacToeGame(player1, player2, size=board_size) 
    game.start()

if __name__ == '__main__':
    main()     