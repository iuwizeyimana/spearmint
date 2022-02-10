import numpy as np

def generate_pop (sub_accel_num, num_pes):
  dtf = np.arange(sub_accel_num)
  #do random number generator btwn 1 and and num_pes
  pop_generated = 0
  while(pop_generated != 1):
        for i in range(sub_accel_num):
          dtf[i] = np.random.randint(1, (num_pes-1))
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

