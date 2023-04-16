# test_maze.py

import pytest

from maze_solver.models.border import Border
from maze_solver.models.maze import InvalidMazeException, Maze
from maze_solver.models.square import Square


def test_maze_validation_improper_squares_given():
    improper_squares = (
        Square(1, 0, 0, Border.EMPTY),
        Square(0, 0, 1, Border.EMPTY),
    )

    with pytest.raises(InvalidMazeException):
        wrong_maze = Maze(squares=improper_squares)
