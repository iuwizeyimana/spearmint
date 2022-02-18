import os
import numpy as np

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = "results file")
	parser.add_argument('res_file', metavar='input', type=str, nargs=1)
	args = parser.parse_args()
	var = args.res_file[0]

	resfile = open(var, 'r')
	lines = resfile.readlines()
	resfile.close()

	edpresfile = open('edp_result.txt', 'r')
	edp_lines = edpresfile.readlines()
	edpresfile.close()

	edp_line = edp_lines[-1]
	edps = edp_line.split()

	line2chng = lines[-1]
	value = line2chng.split()

	#shrink the edp number for the optimization algo
	edp = float(edps[0])/(1e+17)
	edp = abs(edp)

	newline = str(edp) + " 0 " + line2chng[4:]
	lines[-1] = newline

	outfile = open(var, 'w')
	for line_ in lines:
		outfile.write(line_)

	outfile.close() 
	

	#hold current best edp in a file
	if(var == 'parent_results.dat'):
		filesize = os.path.getsize("best_res_par.txt")
		if (filesize == 0):
			res_file = open('best_res_par.txt', 'w')
			res_file.write(edp)
			res_file.close()
		else:
			res_file = open('best_res_par.txt', 'r+')
			cur_best = int(res_file.readlines()[0])
			if(cur_best > edp): res_file.write(edp)
			res_file.close()
	elif(var == 'child1_results.dat'):
		filesize = os.path.getsize("best_res_child1.txt")
		if (filesize == 0):
			res_file = open('best_res_child1.txt', 'w')
			res_file.write(edp)
			res_file.close()
		else:
			res_file = open('best_res_child1.txt', 'r+')
			cur_best = int(res_file.readlines()[0])
			if(cur_best > edp): res_file.write(edp)
			res_file.close()
	elif(var == 'child2_results.dat'):
		filesize = os.path.getsize("best_res_child2.txt")
		if (filesize == 0):
			res_file = open('best_res_child2.txt', 'w')
			res_file.write(edp)
			res_file.close()
		else:
			res_file = open('best_res_child2.txt', 'r+')
			cur_best = int(res_file.readlines()[0])
			if(cur_best > edp): res_file.write(edp)
			res_file.close()
	else:
		print("could find what results file it was")

#to-do 1-> change results.dat to input file --done 
#      2-> hold the current best edp in an input file as well -- done
#      3-> find a non-hardcoded way to have varying numbers of sub_accels	
