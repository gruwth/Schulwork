class Map:
    def __init__(self):
        self.board = [["_" for _ in range(10)] for _ in range(10)]
        self.bleeehh = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

        
    def print_board(self):
        print(" |1|2|3|4|5|6|7|8|9|10|")
        for i in range(10):
            print(f"{self.bleeehh[i]}|{self.board[i][0]}|{self.board[i][1]}|{self.board[i][2]}|{self.board[i][3]}|{self.board[i][4]}|{self.board[i][5]}|{self.board[i][6]}|{self.board[i][7]}|{self.board[i][8]}|{self.board[i][9]}|")





if __name__ == "__main__":
    map = Map()
    map.print_board()