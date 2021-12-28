from ch4.NQueensProblem import NQueensProblem as NQP
import pytest

def test_NQP_init_works():
    nqp = NQP(4)
    queensList = nqp.queen_positions
    assert queensList[0] == [0,0]
    assert queensList[1] == [0,1]
    assert queensList[2] == [0,2]
    assert queensList[3] == [0,3]

    assert nqp.board == [[1,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    assert nqp.number_queens == 4

def test_NQP_init_less_than_4_queens():
    with pytest.raises(Exception):
        nqp = NQP(3)

def test_number_of_collisions():
    nqp = NQP(4)
    collisions = nqp.get_number_of_colliding_queens()
    assert collisions == 6

    nqp = NQP(5)
    collisions = nqp.get_number_of_colliding_queens()
    assert collisions == 10

def test_is_solution_pass():
    nqp = NQP(4)
    queens = nqp.queen_positions
    queens[0] = [1,0]
    queens[1] = [3,1]
    queens[2] = [0,2]
    queens[3] = [2,3]
    nqp.update_queens(queens)
    assert nqp.get_number_of_colliding_queens() == 0
    assert nqp.is_solution() == True

def test_is_solution_fail():
    nqp = NQP(4)
    assert nqp.is_solution() == False

def test_visualize_board_manually():
    nqp = NQP(4)
    nqp.visualize_board()
    print()
    queens = nqp.queen_positions
    queens[0] = [1,0]
    queens[1] = [3,1]
    queens[2] = [0,2]
    queens[3] = [2,3]
    nqp.update_queens(queens)
    nqp.visualize_board()
    assert True #TODO: Turn to false if you want to visually check

def test_board_size():
    nqp = NQP(8)
    assert len(nqp.board) == 8


