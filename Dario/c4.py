import random


class ConnectFour:
    def __init__(self):
        self.board = [['_' for _ in range(7)] for _ in range(6)]
        self.player = 'X'
        self.computer = 'O'
        self.winner = None
        self.ongoing = True
        self.move = None

    def print_board(self):
        print("|1|2|3|4|5|6|7|")
        for i in range(6):
            print(f"|{self.board[i][0]}|{self.board[i][1]}|{self.board[i][2]}|{self.board[i][3]}|{self.board[i][4]}|{self.board[i][5]}|{self.board[i][6]}|")
        print("---------------")


    def validate_input(self):
        try:
            self.move = int(self.move)
            return self.move >= 1 and self.move <= 7
        except Exception:
            return False
        
    def validate_move(self, move):
        row = 5
        while row >= 0:
            if self.board[row][move-1] == '_':
                return True, row
            row -= 1
        return False, None


    def player_move(self):
        while True:
            self.move = input("Wähle eine Spalte (1-7): ")
            if not self.validate_input():
                print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 7 eingeben.")
                continue
            valid, row = self.validate_move(self.move)
            if valid:
                self.board[row][self.move-1] = self.player
            else:
                print("Spalte ist voll. Bitte eine andere Spalte wählen.")
                continue
            break

    def computer_move(self):
        valid = False
        while not valid:
            self.move = random.randint(1, 7)
            valid, row = self.validate_move(self.move)
            print("Computer pick: ", self.move)
            if valid:
                self.board[row][self.move-1] = self.computer
    

    def check_winner(self):
        for i in range(6):
            for j in range(7):
                if self.board[i][j] != '_':
                    if j < 4 and self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]:
                        return True
                    if i < 3 and self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]:
                        return True
                    if i < 3 and j < 4 and self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]:
                        return True
                    if i < 3 and j > 2 and self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3]:
                        return True
        return False

        


if __name__ == "__main__":
    connect4 = ConnectFour()
    connect4.print_board()
    while True:
        connect4.player_move()
        connect4.print_board()
        if connect4.check_winner():
            print(f"{connect4.player} hat gewonnen!")
            break
        connect4.computer_move()
        connect4.print_board()
        if connect4.check_winner():
            print(f"{connect4.computer} hat gewonnen!")
            break
