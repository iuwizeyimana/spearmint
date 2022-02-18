if __name__ == "__main__":
	# open the pop file
	parser = argparse.ArgumentParser(description = "pop file parser")	
	parser.add_argument('pop_file', metavar = 'input', type=str, nargs=1, help="file with hw distr")
	args = parser.parse_args()
	var = args.pop_file[0]
	infile = open(var, 'r')	
	lines = infile.readlines()
	infile.close()
	#make a string with L1 and L2 sizes and NoC and all that jazz
	#To-Do make this less hard coded lol
	#find a way to distribute the l1 l2 and noc_bw based on the num pes we have
	end_lines = "\nL1Size: 10240\nL2Size: 1049000\nNoC_BW: 8192\nNoC_NumHops: 1"
	pes = "NumPEs: "
	
	#1. make the parent sub-accels
	parent_pop = np.fromstring(lines[0][:-1], dtype = int, sep = ' ')
	parent_pes_1, parent_pes_2 = parent_pop[0], parent_pop[1]
	parent_accel1 = pes + parent_pes_1 + end_lines
	parent_accel2 = pes + parent_pes_2 + end_lines
	outfile_par_1 = open('parent_accel1.m', 'w')
	outfile_par_1.write(parent_accel1)
	outfile_par_1.close()
	outfile_par_2 = open('parent_accel2.m', 'w')
	outfile_par_2.write(parent_accel2)
	outfile_par_2.close()
	

	#2. make the child1 sub_accels
	child1_pop = np.fromstring(lines[1][:-1], dtype = int, sep = ' ')
	child1_pes_1, child1_pes_2 = child1_pop[0], child1_pop[1]
	child1_accel1 = pes + child1_pes_1 + end_lines
	child1_accel2 = pes + child1_pes_2 + end_lines
	outfile_child1_1 = open('child1_accel1.m', 'w')
	outfile_child1_1.write(child1_accel1)
	outfile_child1_1.close()
	outfile_child1_2 = open('child1_accel2.m', 'w')
	outfile_child1_2.write(pchild1_accel2)
	outfile_child1_2.close()


	#3. make the child2 sub_accels
	child2_pop = np.fromstring(lines[2][:-1], dtype = int, sep = ' ')
	child2_pes_1, child1_pes_2 = child2_pop[0], child2_pop[1]
	child2_accel1 = pes + child2_pes_1 + end_lines
	child2_accel2 = pes + child2_pes_2 + end_lines
	outfile_child2_1 = open('child2_accel1.m', 'w')
	outfile_child2_1.write(child2_accel1)
	outfile_child2_1.close()
	outfile_child2_2 = open('child2_accel2.m', 'w')
	outfile_child2_2.write(pchild2_accel2)
	outfile_child2_2.close()
