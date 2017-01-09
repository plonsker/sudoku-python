#no classes for now. this is an experiment with just methods.
from random import randint
from collections import OrderedDict
import copy
import random


#refactor using a list instead of a dictionary

def puzzle_parser(puzzle_str):
    global orig_puzzle_list
    orig_puzzle_list = map(int, list(puzzle_str))
    return orig_puzzle_list

def row_ref(orig_puzzle_list):
    orig_puzzle_rows = [orig_puzzle_list[i:i+9] for i in range(0, len(orig_puzzle_list), 9)]
    print orig_puzzle_rows
    return orig_puzzle_rows


def column_ref(orig_puzzle_list):
    orig_puzzle_columns = map(list, zip(*([orig_puzzle_list[i:i+9] for i in range(0, len(orig_puzzle_list),9)])))
    print orig_puzzle_columns
    return orig_puzzle_columns

def box_ref(orig_puzzle_list):
    orig_puzzle_boxes_temp = [orig_puzzle_list[i:i+3] for i in range(0, len(orig_puzzle_list),3)]
    orig_puzzle_boxes_temp = [list(cell) for cell in orig_puzzle_boxes_temp]

    # print orig_puzzle_boxes_temp

    orig_puzzle_boxes = []

    #perhaps make this a loop?
    orig_puzzle_boxes.append(orig_puzzle_boxes_temp[0] + orig_puzzle_boxes_temp[3] + orig_puzzle_boxes_temp[6])
    orig_puzzle_boxes.append(orig_puzzle_boxes_temp[1] + orig_puzzle_boxes_temp[4] + orig_puzzle_boxes_temp[7])
    orig_puzzle_boxes.append(orig_puzzle_boxes_temp[2] + orig_puzzle_boxes_temp[5] + orig_puzzle_boxes_temp[8])
    orig_puzzle_boxes.append(orig_puzzle_boxes_temp[9] + orig_puzzle_boxes_temp[12] + orig_puzzle_boxes_temp[15])
    orig_puzzle_boxes.append(orig_puzzle_boxes_temp[10] + orig_puzzle_boxes_temp[13] + orig_puzzle_boxes_temp[16])
    orig_puzzle_boxes.append(orig_puzzle_boxes_temp[11] + orig_puzzle_boxes_temp[14] + orig_puzzle_boxes_temp[17])
    orig_puzzle_boxes.append(orig_puzzle_boxes_temp[18] + orig_puzzle_boxes_temp[21] + orig_puzzle_boxes_temp[24])
    orig_puzzle_boxes.append(orig_puzzle_boxes_temp[19] + orig_puzzle_boxes_temp[22] + orig_puzzle_boxes_temp[25])
    orig_puzzle_boxes.append(orig_puzzle_boxes_temp[20] + orig_puzzle_boxes_temp[23] + orig_puzzle_boxes_temp[26])

    # print "here are the boxes"
    # print orig_puzzle_boxes
    return orig_puzzle_boxes

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

#the following method is not in use
def complete_area_checker(area):
    if len(set(area)) == 1:
    #maybe detect if there are any zeros
        return True

def complete_puzzle_checker(puzzle):
    if all(len(set(sublist)) == 9 for sublist in row_ref(puzzle)) and all(len(set(sublist)) == 9 for sublist in column_ref(puzzle)) and all(len(set(sublist)) == 9 for sublist in box_ref(puzzle)):
            return True


def solution_collector(orig_puzzle_list, cell_index):

  for cell,num in enumerate(orig_puzzle_list):
    #   print num
    #this is broken. need to fix it so
      if num != 0:
          cell=cell
      else:
          numbers_now = row_ref(orig_puzzle_list)[cell_row(cell)] + column_ref(orig_puzzle_list)[cell_column(cell)] + box_ref(orig_puzzle_list)[cell_box(cell)]
          num_list = list(range(1,10))
          possible_nums = [i for i in num_list if i not in numbers_now]
          orig_puzzle_list[cell] = possible_nums
  print orig_puzzle_list

def solver(orig_puzzle_list):
     old_orig_puzzle_list = orig_puzzle_list
     going = True
     #the already_seen list was created in order to keep previous iterations of puzzles from being repeated, but has not done much
     already_seen = []

    #  print old_orig_puzzle_list
     i = 0
     while going:
        #  new_orig_puzzle_list = ""
         new_orig_puzzle_list = copy.deepcopy(old_orig_puzzle_list)
         for cell,num in enumerate(new_orig_puzzle_list):
             if isinstance(num, list):
                 new_orig_puzzle_list[cell] = random.choice(num)
                 print new_orig_puzzle_list
                 print "Calculation: %s" % i
         if complete_puzzle_checker(new_orig_puzzle_list):
             print "solved"
             print new_orig_puzzle_list
            #  print already_seen
             break

         i+=1


#first sample puzzle:
# practice_puzzle = "105802000090076405200400819019007306762083090000061050007600030430020501600308900"

#nearly solved puzzle for testing purposes:
practice_puzzle = "246857913180000000000001486418329507637480000950170048764532891321968754895710000"

#entirely solved puzzle for testing sake
# practice_puzzle = "173269584589410072426758193291584700005672819867931245914826357658347921732195468"

puzzle_parser(practice_puzzle)
row_ref(orig_puzzle_list)
column_ref(orig_puzzle_list)
box_ref(orig_puzzle_list)
cell_row(80)
cell_column(80)
cell_box(80)
solution_collector(orig_puzzle_list, 80)
solver(orig_puzzle_list)
