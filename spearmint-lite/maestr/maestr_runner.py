
if __name__ == '__main__':
	resfile = open('results.dat', 'r')
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

	outfile = open('results.dat', 'w')
	for line_ in lines:
		outfile.write(line_)

	outfile.close() 
	
	
