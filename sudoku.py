#no classes for now. this is an experiment with just methods.

def puzzle_dict(puzzle_str):
    puzzle_str_arr = list(puzzle_str)
    puzzle_master = dict(enumerate(puzzle_str_arr))
    print puzzle_master

def row_ref(puzzle_str):
    puzzle_rows = [puzzle_str[x:x+9] for x in range(0, len(puzzle_str),9)]
    puzzle_rows = [list(cell) for cell in puzzle_rows]
    print(puzzle_rows)

def column_ref(puzzle_str):
    print map(list, zip(*([puzzle_str[x:x+9] for x in range(0, len(puzzle_str),9)])))

practice_puzzle = "1-58-2----9--764-52--4--819-19--73-6762-83-9-----61-5---76---3-43--2-5-16--3-89--"
puzzle_dict(practice_puzzle)
row_ref(practice_puzzle)
column_ref(practice_puzzle)
