# maze.py

from dataclasses import dataclass
from functools import cached_property
from typing import Iterator

from .role import Role
from .square import Square


class InvalidMazeException(Exception):
    """Exception for when a maze is initialised with improper squares"""


@dataclass(frozen=True)
class Maze:
    squares: tuple[Square, ...]

    def __post_init__(self) -> None:
        validate_indices(self)
        validate_rows_columns(self)
        validate_entrance(self)
        validate_exit(self)

    def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)

    def __getitem__(self, index: int) -> Square:
        return self.squares[index]

    @cached_property
    def width(self):
        return max(square.column for square in self) + 1

    @cached_property
    def height(self):
        return max(square.row for square in self) + 1

    @cached_property
    def entrance(self):
        return next(square for square in self if square.role is Role.ENTRANCE)

    @cached_property
    def exit(self):
        return next(square for square in self if square.role is Role.EXIT)


def validate_indices(maze: Maze) -> None:
    if not [square.index for square in maze] == list(range(len(maze.squares))):
        raise InvalidMazeException("Square indices are incorrectly mapped")


def validate_rows_columns(maze: Maze) -> None:
    for y in range(maze.height):
        for x in range(maze.width):
            square = maze[y * maze.width + x]
            if not square.row == y:
                raise InvalidMazeException("Square's row is not correct")
            if not square.column == x:
                raise InvalidMazeException("Square's column is incorrect")


def validate_entrance(maze: Maze) -> None:
    if not 1 == sum(1 for square in maze.squares if square.role is Role.ENTRANCE):
        raise InvalidMazeException("Maze does not have exactly one entrance")


def validate_exit(maze: Maze) -> None:
    if not 1 == sum(1 for square in maze.squares if square.role is Role.EXIT):
        raise InvalidMazeException("Maze does not have exactly one exit")
