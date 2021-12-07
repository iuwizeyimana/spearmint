from dtf_const import dtf_const

if __name__ == '__main__':

	#1. create the dataflow from results.dat 
	text_file = open("order.txt", "r")
	order_array = text_file.readlines()
	text_file.close()
	#make the letters array
	letters = "KCRSXY"
	resfile = open('results.dat','r')
	r = resfile.readlines()
	resfile.close()
	line = r[-1]
	values = line.split()
	#L2O = [int(values[2]), int(values[3])]
	#L1O = [int(values[4]), int(values[5])]
	#L2P = [int(values[6]), int(values[7])]
	#L1P = [int(values[8]), int(values[9])]
	#TILE_L2 = [int(values[10]), int(values[11])]


	L2O = [121, 121]
	L1O = [142, 142]
	L2P = [int(values[2]), int(values[3])]
	L1P = [int(values[4]), int(values[5])]
	TILE_L2 = [64, 64]
	dataflows = dtf_const(L2O, L1O, L2P, L1P,TILE_L2, order_array, letters)


	#special case for dimesion K, will make it smoother later
	dataflow_wo_k = "\t\t Dataflow { \n\t\t\tSpatialMap(1,1) C;\n\t\t\tTemporalMap(Sz(R),1) Y;\n\t\t\tTemporalMap(Sz(S),1) X;\n\t\t\tTemporalMap(Sz(R),Sz(R)) R;\n\t\t\tTemporalMap(Sz(S),Sz(S)) S;\n\t\t}\n"

	#2. now read the given models and write their mappings

	for i in range (3):
		#we are assuming 3 models will be run in parallel
		model_name = 'model_' + str(i) + '.m'
		model_file = open(model_name, 'r')
		model = model_file.readlines()
		model_file.close()
		model_dtf_0 = []
		model_dtf_1 = []
		for line_ in model:
			model_dtf_0.append(line_)
			model_dtf_1.append(line_)


			if (line_[2:20] == "Dimensions { K: 1,"):
				
				#check and remove extra k values where necessary
				#start with dtf 0	
				dtf_0 = dataflows[0].splitlines()
				k_idx = []
				idx = -1
				idx_l1 = 0
				k_spatial = 0
				k_spatial_l2 = 0
				k_spatial_l1 = 0
				in_l1 = 0
				cluster_idx = 0

				for dtf_lines in dtf_0:
					idx += 1
					if((dtf_lines[3:10] == "Cluster")):
						in_l1 = 1
						cluster_idx = idx
					if(dtf_lines[-3] == "K"):
						k_idx.append(idx)
						if((dtf_lines[3:13] == "SpatialMap") and (in_l1==0)):
							k_spatial = 1
							k_idx.remove(idx)
						if((dtf_lines[3:13] == "SpatialMap") and (in_l1 ==1)):
							k_spatial_l1 = 1
					if((dtf_lines[3:10] == "Cluster") and (k_spatial == 1)):
						k_spatial_l2 = 1
						idx_l1 = idx + 1
				if(k_spatial_l1 == 1):
					new_dtf = "\n".join(dtf_0[0:cluster_idx])
					new_dtf += "}\n"
					model_dtf_0.append(new_dtf)
				elif(k_spatial_l2 == 1):
					new_dtf = "\t\tDataflow {\n"
					new_dtf += "\n".join(dtf_0[idx_l1:])
					new_dtf += "\n"
					model_dtf_0.append(new_dtf)
				else:
					decrement = 0
					for w in range (len(k_idx)):
						k_idx[w] -= decrement
						dtf_0.remove(dtf_0[k_idx[w]])
						decrement += 1
					new_dtf = "\n".join(dtf_0)
					model_dtf_0.append(new_dtf)

				#do the same for dtf 1
				dtf_1 = dataflows[1].splitlines()
				k_idx = []
				idx = -1
				idx_l1 = 0
				k_spatial = 0
				k_spatial_l2 = 0
				k_spatial_l1 = 0
				in_l1 = 0 
				cluster_idx = 0
				
				for dtf_lines_ in dtf_1:
					idx += 1
					if((dtf_lines_[3:10] == "Cluster")):
						in_l1 = 1
						cluster_idx = idx
					if(dtf_lines_[-3] == "K"):
						k_idx.append(idx)
						if((dtf_lines_[3:13] == "SpatialMap") and (in_l1==0)):
							#print("here")
							k_spatial = 1
							k_idx.remove(idx)
						if((dtf_lines_[3:13] == "SpatialMap") and (in_l1 ==1)):
							k_spatial_l1 = 1
					if((dtf_lines_[3:10] == "Cluster") and (k_spatial == 1)):
						k_spatial_l2 = 1
						idx_l1 = idx + 1
				if(k_spatial_l1 == 1):
					new_dtf = "\n".join(dtf_1[0:cluster_idx])
					new_dtf += "}\n"
					model_dtf_1.append(new_dtf)
				elif(k_spatial_l2 == 1):
					new_dtf = "\t\tDataflow {\n"
					new_dtf += "\n".join(dtf_1[idx_l1:])
					new_dtf += "\n"
					model_dtf_1.append(new_dtf)
				else:
					decrement = 0
					for w in range (len(k_idx)):
						k_idx[w] -= decrement
						dtf_1.remove(dtf_1[k_idx[w]])
						decrement += 1
					new_dtf = "\n".join(dtf_1)
					model_dtf_1.append(new_dtf)

				#need to fix this and make it less hard-coded
				#model_dtf_0.append(dataflow_wo_k)
				#model_dtf_1.append(dataflow_wo_k)

			elif(line_[2:12]== "Dimensions"):
				model_dtf_0.append(dataflows[0])
				model_dtf_1.append(dataflows[1])

		#now put the models in their appropriate files
		#dtf 0
		model_map0_name = 'model_' + str(i) + '_dtf0.m'
		outfile_0 = open(model_map0_name, 'w')
		for dtf0 in model_dtf_0:
			outfile_0.write(dtf0)
		outfile_0.close()
		#dtf 1
		model_map1_name = 'model_' + str(i) + '_dtf1.m'
		outfile_1 = open(model_map1_name, 'w')
		for dtf1 in model_dtf_1:
			outfile_1.write(dtf1)
		outfile_1.close()

