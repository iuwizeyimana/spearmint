import argparse
import numpy as np

def generate_pop (sub_accel_num, num_pes):
  dtf = np.arange(sub_accel_num)
  #do random number generator btwn 1 and and num_pes
  pop_generated = 0
  while(pop_generated != 1):
        for i in range(sub_accel_num):
          dtf[i] = np.random.randint(1024, (num_pes-1024)) #To-Do change the hard coded 1024
        if(np.sum(dtf) == num_pes):
          pop_generated = 1
        #else:
         # print("generating population failed by: ", np.sum(dtf) )

  return dtf
  
def gen_new_pop (last_pop, delta, sub_accel_num):
  #delta is the maximum distance one can subtract 

  #first sort the last population 
  #ascending order
  sorted_last = np.sort(last_pop)
  new_pop_1 = np.array(sorted_last)
  new_pop_2 = np.array(sorted_last)
  #get the middle number
  #something to be improved on
  #when the accel_num are odd the middle one is not touched
  mid_pt = int(sub_accel_num /2)

  for k in range(mid_pt):
    #get a random number within a range of delta
    rand_num = np.random.randint(-delta, delta)
    #rand_num = delta
    x1 = sorted_last[k] + rand_num
    y1 = sorted_last[-(k+1)] - rand_num
    x2 = sorted_last[k] - rand_num
    y2 = sorted_last[-(k+1)] + rand_num
    if (x1>0 and y1>0):
      new_pop_1[k] = x1
      new_pop_1[-(k+1)] = y1

    if (x2>0 and y2>0):
      new_pop_2[k] = x2
      new_pop_2[-(k+1)] = y2


  return new_pop_1, new_pop_2

def greedy_random(sub_accel_num, num_pes, delta, num_pop, ctr=0):
  mid = int(sub_accel_num/2)
  #check to see if we must generate a new pop, if so generate them and put them in separate files
  if(ctr == 0):
    #1. Generate the populations' parent 
    pop_array = np.zeros((num_pop, 3, (sub_accel_num+1))) #the 3 is for 1 parent a 2 children
    # last number will hold the cost 
    for l in range(num_pop):
      pop_ = np.zeros(sub_accel_num)
      is_not_in_range = 0
      while(is_not_in_range != 1):
        is_not_in_range = 1
        if(l==0):
          pop_ = np.sort(generate_pop(sub_accel_num, num_pes))
        else:
          pop_ = np.sort(generate_pop(sub_accel_num, num_pes))
          for n in range(l):
            for o in range(mid):
              if(np.abs(pop_array[n][0][o] - pop_[o]) < (delta*2)):
                is_not_in_range = 0
                break
      pop_array[l][0][:-1] = np.array(pop_)

    #2. Generate the children
    for m in range(num_pop):
      pop_array[m][1][:-1], pop_array[m][2][:-1] = gen_new_pop(pop_array[m][0][:-1], delta, sub_accel_num)

    #3. write the populations to their respective files
    for k in range(num_pop):
      file_name = "pop_" + str(k) + ".dat"
      np.savetxt(file_name, (pop_array[k][0], pop_array[k][1], pop_array[k][2]), fmt= "%d")

  elif(ctr == 1): 
    #do greedy across every population
    for k in range(num_pop):
      file_name = "pop_" + str(k) + ".dat"
      infile = open(file_name, 'r')
      lines = infile.readlines()
      infile.close()
      #should have an error check that ensure the line in the files aren't greater than 3
      parent = np.fromstring(lines[0][:-1], dtype = int, sep = ' ')
      child1 = np.fromstring(lines[1][:-1], dtype = int, sep = ' ')
      child2 = np.fromstring(lines[2][:-1], dtype = int, sep = ' ')

      #print("parent cost: ", parent[-1], " child1: ", child1[-1], " child2: ", child2[-1])
      #make the population with the lowest cost the new parent
      new_pop = np.zeros((3, (sub_accel_num+1)))
      if(parent[-1] > child1[-1]):
        if(child1[-1]>child2[-1]):
          new_pop[0] = child2
        else: 
          new_pop[0] = child1
      elif(parent[-1]>child2[-1]):
        new_pop[0] = child2
      else:
        new_pop[0] = parent
      #then get its children
      new_pop[1][:-1], new_pop[2][:-1] = gen_new_pop(new_pop[0][:-1], delta, sub_accel_num)
      #write the new pop on the files 
      np.savetxt(file_name, (new_pop[0], new_pop[1], new_pop[2]), fmt = "%d")

  elif(ctr == 2):
    #get the best population and output it 
    file_name = "pop_0.dat"
    infile = open(file_name, 'r')
    lines = infile.readlines()
    infile.close()
    to_ret = np.array(lines[0][:-1], dtype = int, sep = ' ')
    for p in range(1, num_pop):
      file_name = "pop_" + str(p) + ".dat"
      infile = open(file_name, 'r')
      lines = infile.readlines()
      infile.close()
      this_pop = np.array(lines[0][:-1], dtype = int, sep = ' ')
      if(to_ret[-1] > this_pop[-1]):
        to_ret = this_pop
    #write toret to a file
    np.savetxt("output.txt", to_ret, newline= " ")
 # return 1	 

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Program input')
  parser.add_argument('integers', metavar = 'input', type=int, nargs='+')
  args = parser.parse_args()
  var = vars(args).get('integers')
  if(len(var)!=5):
    print("must have 5 arguments")
  else:
    greedy_random(var[0], var[1], var[2], var[3], var[4])
