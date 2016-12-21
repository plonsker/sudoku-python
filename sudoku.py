#no classes for now. this is an experiment with just methods.

def board_rows(puzzle_string):

        lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
        # http://stackoverflow.com/questions/4119070/how-to-divide-a-list-into-n-equal-parts-python
        # for space in puzzle_string:
            # if space != "-":
                # # puzzle_string = map(int, puzzle_string)
                # map(lambda puzzle_string: int(space) if space != "-", puzzle_string)
                # 'lower' if x < 3 else 'higher' for x in lst

        #Try to iterate through list and change anything that isn't a dash into an integer
        int(space) if space != "-" else "-" for space in puzzle_string

        board_array = list(puzzle_string)
        print lol(board_array, 9)



board_rows("1-58-2----9--764-52--4--819-19--73-6762-83-9-----61-5---76---3-43--2-5-16--3-89--")
