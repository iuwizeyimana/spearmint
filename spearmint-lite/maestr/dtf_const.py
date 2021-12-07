def dtf_const(L2O, L1O, L2P, L1P, TILE_L2, array, letters):
	#for sub_accel_0
	l2o_0 = L2O[0] #will be a number between 0 and 6!-1
	l2p_0 = L2P[0] #will be a number between 0 and 5
	l1o_0 = L1O[0] #same as l2
	l1p_0 = L1P[0] #same as l2

	#assign the appropriate order given the number
	order_l2_0 = array[l2o_0]
	order_l1_0 = array[l1o_0]
	par_l2_0 = letters[l2p_0]
	par_l1_0 = letters[l1p_0]

	#for sub_accel_1
	l2o_1 = L2O[1] #will be a number between 0 and 6!-1
	l2p_1 = L2P[1] #will be a number between 0 and 6
	l1o_1 = L1O[1] #same as l2
	l1p_1 = L1P[1] #same as l2

	#assign the appropriate order given the number
	order_l2_1 = array[l2o_1]
	order_l1_1 = array[l1o_1]
	par_l2_1 = letters[l2p_1]
	par_l1_1 = letters[l1p_1]
	
	#build the default tile size and offset  dictionaries

	dict_tl_sz = {"K":"1", "C":"1", "Y":"Sz(R)", "X":"Sz(S)", "R":"Sz(R)", "S":"Sz(S)"}
	dict_ofst_sz = {"K":"1", "C":"1", "Y":"1", "X":"1", "R":"Sz(R)", "S":"Sz(S)"}

	#start building the dataflow for accel0
	dataflow_0 = "\t\tDataflow { \n"

	
	if(par_l2_0 != par_l1_0):
		#let us append the values for l2
		for dim in (order_l2_0):
			if (dim == "\n"): continue
			if (dim == par_l2_0):
				dataflow_0 += "\t\t\tSpatialMap(" + dict_tl_sz[dim] + "," + dict_ofst_sz[dim] + ")" + dim + "; \n"
			elif (dim == par_l1_0):
				dataflow_0 += "\t\t\tTemporalMap(" + str(TILE_L2[0]) + "," + str(TILE_L2[0]) + ")" + dim + "; \n"
			else:
				dataflow_0 += "\t\t\tTemporalMap(" + dict_tl_sz[dim] + "," + dict_ofst_sz[dim] + ")" + dim + "; \n"
		#add the cluster directive. Note that we use the tile size of the dimension parallelized in l1 
		dataflow_0 += "\t\t\tCluster("+ str(TILE_L2[0]) + ", P); \n"

		#if the parallel dimension is K  remove it from L1 order
		if(par_l2_0 == "K"):
			#create the new order without k
			placeholder = ""
			for spot in range(len(order_l1_0)):
				if(order_l1_0[spot]!="K"):
					placeholder += order_l1_0[spot]
			#replace order_l1
			order_l1_0 = placeholder 
	#now apprend the values for l1
	for dim_ in (order_l1_0):
		if (dim_ == "\n"): continue;
		if (dim_ == par_l1_0):
			dataflow_0 += "\t\t\tSpatialMap(" + dict_tl_sz[dim_] + "," + dict_ofst_sz[dim_] + ")" + dim_ + "; \n"
		else:
			dataflow_0 += "\t\t\tTemporalMap(" + dict_tl_sz[dim_] + "," + dict_ofst_sz[dim_] + ")" + dim_ + "; \n"
	dataflow_0 += "\t\t}\n"

	#now build the dataflow for accel1
	dataflow_1 = "\t\tDataflow { \n"

	if(par_l2_1 != par_l1_1):
		#let us append the values for l2
		for dim in (order_l2_1):
			if (dim == "\n"): continue;
			if (dim == par_l2_1):
				dataflow_1 += "\t\t\tSpatialMap(" + dict_tl_sz[dim] + "," + dict_ofst_sz[dim] + ")" + dim + "; \n"
			elif (dim == par_l1_1):
				dataflow_1 += "\t\t\tTemporalMap(" + str(TILE_L2[1]) + "," + str(TILE_L2[1]) + ")" + dim + "; \n"
			else:
				dataflow_1 += "\t\t\tTemporalMap(" + dict_tl_sz[dim] + "," + dict_ofst_sz[dim] + ")" + dim + "; \n"
		#add the cluster directive. Note that we use the tile size of the dimension parallelized in l1 
		dataflow_1 += "\t\t\tCluster("+ str(TILE_L2[1]) + ", P); \n"
		#if the parallel dimension is K  remove it from L1 order
		if(par_l2_1 == "K"):
			#create the new order without k
			placeholder = ""
			for spot in range(len(order_l1_1)):
				if(order_l1_1[spot]!="K"):
					placeholder += order_l1_1[spot]
			#replace order_l1
			order_l1_1 = placeholder 
	#now apprend the values for l1
	for dim_ in (order_l1_1):
		if (dim_ == "\n"): continue;
		if (dim_ == par_l1_1):
			dataflow_1 += "\t\t\tSpatialMap(" + dict_tl_sz[dim_] + "," + dict_ofst_sz[dim_] + ")" + dim_ + "; \n"
		else:
			dataflow_1 += "\t\t\tTemporalMap(" + dict_tl_sz[dim_] + "," + dict_ofst_sz[dim_]+ ")" + dim_ + "; \n"
	dataflow_1 += "\t\t}\n"

	return dataflow_0, dataflow_1
