if __name__ == "__main__":
	parser = argparse.ArgumentParser(description = "pop file parser")
	parser.add_argument('pop_file', metavar = 'input', type=str, nargs = 1)
	args = parser.parse_args()
	var = args.pop_file[0]
	infile = open(var, 'r')
	lines = infile.readlines()
	infile.close()
	parent_pop = np.fromstring(lines[0][-1], dtype = int, sep = ' ')
	child1_pop = np.fromstring(lines[1][-1], dtype = int, sep = ' ')
	child2_pop = np.fromstring(lines[2][-1], dtype = int, sep = ' ')

	#1. write parent edp
	res_file = open('best_res_par.txt', 'r')
	parent_pop[-1] = int(res_file.readlines()[0])
	res_file.close()

	#2. write child1 edp
	res_file = open('best_res_child1.txt', 'r')
	child1_pop[-1] = int(res_file.readlines()[0])
	res_file.close()

	#3. write child2 edp
	res_file = open('best_res_child2.txt', 'r')
	child2_pop[-1] = int(res_file.readlines()[0])
	res_file.close()

	#4. save it to the pop_file
	np.savetxt(var, (parent_pop, child1_pop, child2_pop), fmt = "%d")

	
