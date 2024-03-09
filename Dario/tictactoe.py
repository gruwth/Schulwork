import random

class tictactoe:
    def __init__(self):
        self.board = [' ']*9
        self.player = 'X'
        self.computer = 'O'
        self.winner = None
        self.ongoing = True
    
    def print_board(self):
        print("     |     |     ")
        print(f"  {self.board[0]}  |  {self.board[1]}  |  {self.board[2]}  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print(f"  {self.board[3]}  |  {self.board[4]}  |  {self.board[5]}  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print(f"  {self.board[6]}  |  {self.board[7]}  |  {self.board[8]}  ")
        print("     |     |     ")

    def player_move(self):
        while True:
            move = int(input("Wähle ein Feld (1-9): "))
            if move < 1 or move > 9:
                print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 9 eingeben.")
                continue
            if self.board[move-1] == ' ':
                self.board[move-1] = self.player
                break
            else:
                print("Feld ist bereits belegt. Bitte ein anderes Feld wählen.")

    def computer_move(self):
        possible_moves = [i for i, x in enumerate(self.board) if x == ' ']
        move = random.choice(possible_moves)
        self.board[move] = self.computer
    

    def bleeh_computer_move(self):
        winning_combinations = [[(i, j), i*3 + 2] for i in range(3) for j in range(2)]
        winning_combinations += [[(i, i+3), i+6] for i in range(3)]
        winning_combinations += [[(0, 4), 8], [(2, 4), 6]]

        for combination in winning_combinations:
            if self.board[combination[0][0]] == self.board[combination[0][1]] and self.board[combination[0][0]] != ' ' and self.board[combination[1]] == ' ':
                self.board[combination[1]] = self.computer
                return
        self.computer_move()


    def check_winner(self):
        winning_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for i in winning_combinations:
            if self.board[i[0]] == self.board[i[1]] == self.board[i[2]] != ' ':
                self.winner = self.board[i[0]]
                return True
        return False
    
    def check_draw(self):
        return ' ' not in self.board
    
    def play(self):
        self.print_board()
        while self.ongoing:
            self.player_move()
            self.print_board()
            if self.check_winner():
                print(f"{self.winner} hat gewonnen!")
                self.ongoing = False
                break
            if self.check_draw():
                print("Unentschieden!")
                self.ongoing = False
                break
            self.bleeh_computer_move()
            print("Computer hat gezogen:")
            self.print_board()
            if self.check_winner():
                print(f"{self.winner} hat gewonnen!")
                self.ongoing = False
                break
            if self.check_draw():
                print("Unentschieden!")
                self.ongoing = False
                break
    
    def reset(self):
        self.board = [' ']*9
        self.winner = None
        self.ongoing = True

if __name__ == "__main__":
    game = tictactoe()
    keep_playing = "y"
    while keep_playing.lower() == "y":
        game.reset()
        game.play()
        keep_playing = input("Nochmal spielen? (y/n): ")
    print("Spiel beendet.")
    
