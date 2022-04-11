

EMPTY_SYMBOL = "-"
SIZE_FIELD = 3
FIRST_PLAYER = "X"
SECOND_PLAYER = "0"


def main():
    field = init_field()
    print(field)

def init_field(size: int = SIZE_FIELD) -> list[list]:

     return  [
        [EMPTY_SYMBOL for _ in  range(SIZE_FIELD)]
        for _ in  range(SIZE_FIELD)
]
print(init_field())

def is_empti_cell(field: list[list],
                  row_index: int,
                  col_index: int) -> bool: ...

def get_cell(field: list[list],
                  row_index: int,
                  col_index: int) -> None:
    ...
win_combinations = [
    [(0,0),(0,1),(0,2)]

]



if __name__ == "__main__":
    main
