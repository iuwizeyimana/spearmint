#!/bin/sh

getedp()
{
for k in {1..2}
do 
	cd .. 
	python3 spearmint-lite.py --method=SequentialChooser --method-args=mcmc_iters=25,noiseless=1 --results $1
	cd maestr
	python model_maker.py $1 
	cp model_0_dtf0.m model_0_dtf1.m model_1_dtf0.m model_1_dtf1.m model_2_dtf0.m model_2_dtf1.m ~/maestro/
	cp $2 $3 ~/maestro/
	cd ~/maestro
	rm edp_result.txt
	./het_mae 6  model_0_dtf0.m model_0_dtf1.m model_1_dtf0.m model_1_dtf1.m model_2_dtf0.m model_2_dtf1.m $2 $3 
	cp edp_result.txt ~/spearmint/spearmint-lite/maestr
	
	cd ~/spearmint/spearmint-lite/maestr
	python maestr_runner.py $1

done

}

echo "creating resource dist"

python3 resource_dist.py $1 $2 $3 $4 0

for i in $(seq 1 $5); do #this is for the amount of times you go through the greedysearch 
	for j in $(seq 1 $6); do #for all the populations get and store their current edp
	        pop_file = "pop_"$i.dat
		python make_hw.py $pop_file
		#empty files to hold best edp -- to do: find a better way to do this
		cp empty.txt best_res_par.txt
		cp empty.txt best_res_child1.txt
		cp empty.txt best_res_child2.txt
		#get the edps
		getedp parent_results.dat parent_accel1.m parent_accel2.m
		getedp child1_results.dat child1_accel1.m child1_accel2.m
		getedp child2_results.dat child2_accel1.m child2_accel2.m
		python store_to_file.py $pop_file
	done 
	python3 resource_dist.py $1 $2 $3 $4 1
done

python3 resource_dist.py $1 $2 $3 $4 2
