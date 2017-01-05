#no classes for now. this is an experiment with just methods.
from random import randint
from collections import OrderedDict
import copy
import random


#refactor using a list instead of a dictionary

def puzzle_parser(puzzle_str):
    # print list(puzzle_str)
    global orig_board_list
    orig_board_list = map(int, list(puzzle_str))
    # print orig_board_list
    return orig_board_list

def row_ref(orig_board_list):
    orig_board_rows = [orig_board_list[i:i+9] for i in range(0, len(orig_board_list), 9)]
    # print orig_board_rows
    return orig_board_rows


def column_ref(orig_board_list):
    orig_board_columns = map(list, zip(*([orig_board_list[x:x+9] for x in range(0, len(orig_board_list),9)])))
    # print orig_board_columns
    return orig_board_columns

def box_ref(orig_board_list):
    # orig_board_boxes = [ int(x) for x in puzzle_str ]
    orig_board_boxes_temp = [orig_board_list[x:x+3] for x in range(0, len(orig_board_list),3)]
    orig_board_boxes_temp = [list(cell) for cell in orig_board_boxes_temp]

    # print orig_board_boxes_temp

    orig_board_boxes = []

    #perhaps make this a while loop
    orig_board_boxes.append(orig_board_boxes_temp[0] + orig_board_boxes_temp[3] + orig_board_boxes_temp[6])
    orig_board_boxes.append(orig_board_boxes_temp[1] + orig_board_boxes_temp[4] + orig_board_boxes_temp[7])
    orig_board_boxes.append(orig_board_boxes_temp[2] + orig_board_boxes_temp[5] + orig_board_boxes_temp[8])
    orig_board_boxes.append(orig_board_boxes_temp[9] + orig_board_boxes_temp[12] + orig_board_boxes_temp[15])
    orig_board_boxes.append(orig_board_boxes_temp[10] + orig_board_boxes_temp[13] + orig_board_boxes_temp[16])
    orig_board_boxes.append(orig_board_boxes_temp[11] + orig_board_boxes_temp[14] + orig_board_boxes_temp[17])
    orig_board_boxes.append(orig_board_boxes_temp[18] + orig_board_boxes_temp[21] + orig_board_boxes_temp[24])
    orig_board_boxes.append(orig_board_boxes_temp[19] + orig_board_boxes_temp[22] + orig_board_boxes_temp[25])
    orig_board_boxes.append(orig_board_boxes_temp[20] + orig_board_boxes_temp[23] + orig_board_boxes_temp[26])

    # print "here are the boxes"
    # print orig_board_boxes
    return orig_board_boxes

#
def cell_row(cell):
    return cell / 9

def cell_column(cell):
    return cell % 9

# this is wrong
def cell_box(cell):
    box_row = (cell / 9) / 3
    box_column = (cell % 9) / 3
    return (box_row * 3) + box_column

def complete_area_checker(area):
    if len(set(area)) == 1:
    #maybe detect if there are any zeros
        return True

def complete_board_checker(board):
    for sublist in row_ref(board):
        if 0 not in sublist:
            return True

    for sublist in column_ref(board):
        if 0 not in sublist:
            return True

    for sublist in box_ref(board):
        if 0 not in sublist:
            return True


def solution_collector(orig_board_list, cell_index):
  # print row_ref(orig_board_list)[cell_row(cell_index)]
  # print column_ref(orig_board_list)[cell_column(cell_index)]
  # print box_ref(orig_board_list)[cell_box(cell_index)]
  #
  # print row_ref(orig_board_list)[cell_row(cell_index)] + column_ref(orig_board_list)[cell_column(cell_index)] + box_ref(orig_board_list)[cell_box(cell_index)]


  for cell,num in enumerate(orig_board_list):
    #   print num
    #this is broken. need to fix it so
      if num != 0:
          cell=cell
      else:
          numbers_now = row_ref(orig_board_list)[cell_row(cell)] + column_ref(orig_board_list)[cell_column(cell)] + box_ref(orig_board_list)[cell_box(cell)]
        #   print numbers_now
          num_list = [1,2,3,4,5,6,7,8,9]
          possible_nums = [x for x in num_list if x not in numbers_now]
          orig_board_list[cell] = possible_nums
        #   print num
  print orig_board_list

def solver(orig_board_list):
     old_orig_board_list = orig_board_list
     going = True

     print old_orig_board_list
     while going:
         new_orig_board_list = copy.deepcopy(old_orig_board_list)
         for cell,num in enumerate(new_orig_board_list):
             if isinstance(num, list):
                 new_orig_board_list[cell] = random.choice(num)
         print new_orig_board_list
        #  print "hi"


#puzzle one:
practice_puzzle = "105802000090076405200400819019007306762083090000061050007600030430020501600308900"

#nearly solved puzzle:
# practice_puzzle = "246857913180000000000001486418329507637480000950170048764532891321968754895710000"

#puzzle two:
# practice_puzzle = "005030081902850060600004050007402830349760005008300490150087002090000600026049503"

#easy kids puzzle
# practice_puzzle = "639000024002904067070268090005603780701025400360040209510080940200419005043700610"

# practice_puzzle = "000000000089410000006700193200000700340600010000900005000020050650040020730100000"
# practice_puzzle = "173269584589413672426758193291584736345672819867931245914826357658347921732195468"

puzzle_parser(practice_puzzle)
# row_ref_index(11)
# column_ref_index(23)
row_ref(orig_board_list)
column_ref(orig_board_list)
box_ref(orig_board_list)
cell_row(80)
cell_column(80)
cell_box(80)
solution_collector(orig_board_list, 80)
solver(orig_board_list)
