from NQueensProblem import NQueensProblem as NQP


class NQueensSearchAgent:

    def __init__(self, number_of_queens, loop_limit):
        self.problem = NQP(number_of_queens)
        self.search_instance = NQP(number_of_queens)
        self.loop_limit = loop_limit
    
    def execute(self):
        pass

    def search(self):
        pass

    def graph_data(self):
        pass