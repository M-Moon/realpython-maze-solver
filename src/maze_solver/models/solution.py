# solution.py

from dataclasses import dataclass
from functools import reduce
from typing import Iterator

from .role import Role
from .square import Square


class InvalidSolutionException(Exception):
    """Exception for when a solution is not properly formatted/invalid"""


@dataclass(frozen=True)
class Solution:
    squares: tuple[Square, ...]

    def __post_init__(self) -> None:
        ...

    def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)

    def __getitem__(self, index: int) -> Square:
        return self.squares[index]

    def __len__(self) -> int:
        return len(self.squares)


def validate_solution(solution: Solution) -> None:
    if not all(
        (
            solution.squares[0].role is Role.ENTRANCE,
            solution.squares[-1].role is Role.EXIT,
            reduce(validate_corridor, solution.squares),
        )
    ):
        raise InvalidSolutionException("Solution contains invalid data")


def validate_corridor(current: Square, following: Square) -> Square:
    if not any((current.row == following.row, current.column == following.column)):
        raise InvalidSolutionException(
            "Two squares next to each other are not a valid corridor"
        )
