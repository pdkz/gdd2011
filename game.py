#!/usr/bin/env python

class OnePersonGame(object) :
  def __init__(self, lists) : 
    self.list = lists
    self.result = list()

  def calc(self) :
    for idx, elem in enumerate(self.list) : 
      step = 1
      is_found = False
      elem = [int(n) for n in elem]
      queue = [elem]
      new_state = list() 

      while (len(queue) > 0) :
        for state in queue :
          fives = [n for n in state if (n % 5) == 0]
          if (len(fives) > 0) :
            if (len(state) == len(fives)) :
              is_found = True
              break
            else :
              next_state = [n for n in state if (n % 5) != 0]
              new_state.append(next_state)
          next_state = [n / 2 for n in state]
          new_state.append(next_state)
          
        if (is_found) : 
          self.result.append(str(step) + '\n')
          break
        queue = new_state[:]
        new_state = []    
        step += 1
    
  def export(self) :
    f = open("output.dat", "w")
    f.writelines(self.result)
    f.close()

def get_list() :
  data = import_data()
  all_list = [row.split() for row in data[1:]]
  num_list = [all_list[i] for i in range(1, len(all_list), 2)]

  return num_list

def import_data() :
  f = open("input.dat", "r")
  data = f.readlines()
  f.close()

  return data

if __name__ == '__main__' :
  lists = list()
  lists = get_list()

  opg = OnePersonGame(lists)
  opg.calc()
  opg.export()
