from pathlib import Path


def read_input(day: int, test: bool = False):

    path = Path(f"day{day:02d}/input.txt")

    if test is True:
        path = Path(f"day{day:02d}/test-input.txt")

    return path.read_text().strip()
