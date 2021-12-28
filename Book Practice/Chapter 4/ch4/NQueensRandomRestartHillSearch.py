from NQueensProblem import NQueensProblem as NQP
from typing import Tuple
import random

from NQueensSearchAgent import NQueensSearchAgent

class NQueensRandomRestartHillSearch(NQueensSearchAgent):

    def __init__(self, number_of_queens, loop_limit, number_restarts, plateau_limit):
        super().__init__(number_of_queens, loop_limit)
        self.restarts_remaining = number_restarts
        self.plateau_limit = plateau_limit
        self.consecutive_plateaus = 0
    
    def execute(self):
        progress_data = []
        solved = False
        while True:
            collisions, different_rows, is_solved = self.search()
            progress_data.append([collisions, different_rows])
            if is_solved:
                self.restarts_remaining = 0
                solved = True
                print("Solution has been found:")
                self.search_instance.visualize_board()
                print()
                print(self.search_instance.queen_positions)
                return
            if self.consecutive_plateaus >= self.plateau_limit:
                break
        print("Restarting due to plateau limit")
        self.restarts_remaining -= 1
        
        # self.graph_data()
    
    def search(self) -> Tuple[int, int, bool]:
        #Values to see if move has improved standing
        # print(self.search_instance.queen_positions)
        # print(len(set([queen[0] for queen in self.queen_positions.values()])))
        
        current_collisions, current_different_rows = self.search_instance.get_number_of_colliding_queens(), self.search_instance.get_number_of_different_rows()
        
        #Current positions
        queen_positions = self.search_instance.queen_positions
        queen_to_move = random.choice(list(queen_positions.keys()))

        #Make move
        coordinates = queen_positions[queen_to_move]
        coordinates[0] = random.randint(0, self.search_instance.number_queens - 1)
        
        #Tentatively update positions
        queen_positions[queen_to_move] = coordinates
        self.search_instance.update_queens(queen_positions)

        #Get new values
        new_collisions, new_different_rows = self.search_instance.get_number_of_colliding_queens(), self.search_instance.get_number_of_different_rows()
        
        #If we are worse, revert
        if new_collisions > current_collisions:
            self.search_instance.update_queens(self.problem.queen_positions)
            self.consecutive_plateaus = 0
        else:
            self.problem.update_queens(self.search_instance.queen_positions)
            self.consecutive_plateaus += 1

        return self.search_instance.get_number_of_colliding_queens(), self.search_instance.get_number_of_different_rows(), self.search_instance.is_solution()

