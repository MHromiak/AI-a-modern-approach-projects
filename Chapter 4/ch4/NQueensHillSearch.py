from NQueensProblem import NQueensProblem as NQP
from typing import Tuple
import random

from NQueensSearchAgent import NQueensSearchAgent

class NQueensHillSearch(NQueensSearchAgent):

    def __init__(self, number_of_queens, loop_limit):
        self.problem = NQP(number_of_queens)
        self.search_instance = NQP(number_of_queens)
        self.loop_limit = loop_limit
    
    def execute(self):
        progress_data = []
        solved = False
        for i in range(0, self.loop_limit):
            collisions, different_rows, is_solved = self.search()
            progress_data.append([collisions, different_rows])
            if is_solved:
                solved = True
                print("Solution has been found:")
                self.search_instance.visualize_board()
                print()
                print(self.search_instance.queen_positions)
                break
        if not solved:
            print("Could not find solution in given amount of loops")
        
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
        else:
            self.problem.update_queens(self.search_instance.queen_positions)

        return self.search_instance.get_number_of_colliding_queens(), self.search_instance.get_number_of_different_rows(), self.search_instance.is_solution()

