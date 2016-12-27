#no classes for now. this is an experiment with just methods.

def puzzle_dict(puzzle_str):
    global puzzle_master
    puzzle_str_arr = list(puzzle_str)
    puzzle_master = dict(enumerate(puzzle_str_arr))

    puzzle_master = {k:int(v) if v.isdigit() else v for k,v in puzzle_master.items()}


    print "Here is the dictionary"
    print puzzle_master


def row_ref(puzzle_str):
    global puzzle_rows
    #try and get this to be integers here
    puzzle_str = [ int(x) for x in puzzle_str ]
    puzzle_rows = [puzzle_str[x:x+9] for x in range(0, len(puzzle_str),9)]
    puzzle_rows = [list(cell) for cell in puzzle_rows]
    print "Here are the rows"
    print puzzle_rows

def column_ref(puzzle_str):
    global puzzle_columns
    puzzle_str = [ int(x) for x in puzzle_str ]
    puzzle_columns = map(list, zip(*([puzzle_str[x:x+9] for x in range(0, len(puzzle_str),9)])))
    print "here are the colums"
    print puzzle_columns

def box_ref(puzzle_str):
    global puzzle_boxes_final
    puzzle_str = [ int(x) for x in puzzle_str ]
    puzzle_box_rows = [puzzle_str[x:x+3] for x in range(0, len(puzzle_str),3)]
    puzzle_box_rows = [list(cell) for cell in puzzle_box_rows]

    puzzle_boxes = map(list, zip(*([puzzle_box_rows[x:x+3] for x in range(0, len(puzzle_box_rows),3)])))

    # print puzzle_boxes

    temp_flat = []
    for sublist in puzzle_boxes:
      for val in sublist:
        temp_flat.append(val)

    puzzle_boxes_temp = []

    puzzle_boxes_temp.append(temp_flat[0:3])
    puzzle_boxes_temp.append(temp_flat[9:12])
    puzzle_boxes_temp.append(temp_flat[18:21])
    puzzle_boxes_temp.append(temp_flat[3:6])
    puzzle_boxes_temp.append(temp_flat[12:15])
    puzzle_boxes_temp.append(temp_flat[21:24])
    puzzle_boxes_temp.append(temp_flat[6:9])
    puzzle_boxes_temp.append(temp_flat[15:18])
    puzzle_boxes_temp.append(temp_flat[24:27])

    temp_flat_2= []

    flattened_list = []

    for x in puzzle_boxes_temp:
      for y in x:
        flattened_list.append(y)

    puzzle_boxes_final = []

    box_0 = flattened_list[0] + flattened_list[1] + flattened_list[2]
    box_1 = flattened_list[3] + flattened_list[4] + flattened_list[5]
    box_2 = flattened_list[6] + flattened_list[7] + flattened_list[8]
    box_3 = flattened_list[9] + flattened_list[10] + flattened_list[11]
    box_4 = flattened_list[12] + flattened_list[13] + flattened_list[14]
    box_5 = flattened_list[15] + flattened_list[16] + flattened_list[17]
    box_6 = flattened_list[18] + flattened_list[19] + flattened_list[20]
    box_7 = flattened_list[21] + flattened_list[22] + flattened_list[23]
    box_8 = flattened_list[24] + flattened_list[25] + flattened_list[26]

    puzzle_boxes_final.append(box_0)
    puzzle_boxes_final.append(box_1)
    puzzle_boxes_final.append(box_2)
    puzzle_boxes_final.append(box_3)
    puzzle_boxes_final.append(box_4)
    puzzle_boxes_final.append(box_5)
    puzzle_boxes_final.append(box_6)
    puzzle_boxes_final.append(box_7)
    puzzle_boxes_final.append(box_8)

    print "here are the boxes"
    print puzzle_boxes_final

#NEXT STEP: make reference table so that you know the row, column, and box for a given cell

def cell_reference(dict, row, column):
  for key, value in puzzle_master.iteritems():
    if key <= 8:
        cell_row = row[0]
        print row[0]
    elif key in range(9,17):
        cell_row = row[1]
    elif key in range(18,26):
        cell_row = row[2]
    elif key in range(27,35):
        cell_row = row[3]
    elif key in range(36,44):
        cell_row = row[4]
    elif key in range(45,53):
        cell_row = row[5]
    elif key in range(54,62):
        cell_row = row[6]
    elif key in range(63,71):
        cell_row = row[7]
    elif key in range(63,71):
        cell_row = row[8]
    elif key in range(72,80):
        cell_row = row[9]
    else:
        print "Error. Row must be out of range"

    if key in range(0,80,9):
        cell_column = puzzle_rows[0]
    elif key in range(1,80,9):
        cell_column = puzzle_rows[1]
    elif key in range(2,80,9):
        cell_column = puzzle_rows[2]
    elif key in range(3,80,9):
        cell_column = puzzle_rows[3]
    elif key in range(4,80,9):
        cell_column = puzzle_rows[4]
    elif key in range(5,80,9):
        cell_column = puzzle_rows[5]
    elif key in range(6,80,9):
        cell_column = puzzle_rows[6]
    elif key in range(7,80,9):
        cell_column = puzzle_rows[7]
    elif key in range(8,81,9):
        cell_column = puzzle_rows[8]
    else:
        print "other column"




practice_puzzle = "105802000090076405200400819019007306762083090000061050007600030430020501600308900"
puzzle_dict(practice_puzzle)
row_ref(practice_puzzle)
column_ref(practice_puzzle)
box_ref(practice_puzzle)
cell_reference(puzzle_master, puzzle_rows, column_ref)
