class Map:
    def __init__(self):
        self.board = [["_" for _ in range(10)] for _ in range(10)]
        self.bleeehh = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.ships = []  # List to store the ships

    def print_board(self):
        print(" |1|2|3|4|5|6|7|8|9|10|")
        for i in range(10):
            print(f"{self.bleeehh[i]}|{self.board[i][0]}|{self.board[i][1]}|{self.board[i][2]}|{self.board[i][3]}|{self.board[i][4]}|{self.board[i][5]}|{self.board[i][6]}|{self.board[i][7]}|{self.board[i][8]}|{self.board[i][9]}|")

    def place_ship(self, start, end):
        # Add the ship to the list of ships
        self.ships.append((start, end))

        # Mark the ship on the board
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                self.board[i][j] = "S"

    def check_hit(self, coordinate):
        # Check if the coordinate hits any ship
        for ship in self.ships:
            if ship[0][0] <= coordinate[0] <= ship[1][0] and ship[0][1] <= coordinate[1] <= ship[1][1]:
                return True
        return False

if __name__ == "__main__":
    map = Map()
    map.place_ship((1, 1), (1, 3))  # Place a ship at coordinates (1,1) to (1,3)
    map.print_board()
    print(map.check_hit((1, 2)))  # Check if the coordinate (1,2) hits a ship