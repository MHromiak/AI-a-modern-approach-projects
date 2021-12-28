

class NQueensProblem:

    def __init__(self, number_queens : int):
        if number_queens <= 3:
            raise Exception("Cannot have less than four queens")
        self.number_queens = number_queens
        self.queen_positions = {}
        self.board = self.init_board()
        self.init_location_dictionary(self.queen_positions, self.number_queens)
        self.update_board()

    def init_board(self):
        self.board = [[0 for x in range(0, self.number_queens)] for y in range(0, self.number_queens)]
    
    def init_location_dictionary(self, queen_positions : dict, number_queens : int):
        for i in range(0, number_queens):
            queen_positions[i] = [0, i] #Varying the column
    
    def update_board(self):
        self.init_board()
        for queen in self.queen_positions.keys():
            coordinates = self.queen_positions[queen]
            self.board[coordinates[0]][coordinates[1]] = 1
    
    def get_number_of_colliding_queens(self) -> int:
        number_of_collisions = 0
        visited_a = []
        for queen_a in self.queen_positions.values():
            for queen_b in self.queen_positions.values():
                if queen_a != queen_b and queen_b not in visited_a: #Removes double counting
                    if queen_a[0] == queen_b[0] or queen_a[1] == queen_b[1] or abs(queen_a[0] - queen_b[0]) == abs(queen_a[1] - queen_b[1]):
                        number_of_collisions += 1
            visited_a.append(queen_a)
        return number_of_collisions
    
    def get_number_of_different_rows(self):
        return len(set([queen[0] for queen in self.queen_positions.values()]))
    
    def update_queens(self, queens : list):
        self.queen_positions = queens
        self.update_board()
    
    def is_solution(self) -> bool:
        if self.get_number_of_colliding_queens() == 0:
            return True
        return False

    def visualize_board(self):
        for line in self.board:
            print(line)


                    