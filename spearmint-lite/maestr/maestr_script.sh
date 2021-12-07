

for i in {1..2}
do 
	cd ..
	#python spearmint-lite.py --method=GPEIOptChooser --method-args=mcmc_iters=25,noiseless=1 maestr
	python3 spearmint-lite.py --method=SequentialChooser --method-args=mcmc_iters=25,noiseless=1 maestr

	cd maestr
	
	python model_maker.py
	cp model_0_dtf0.m model_0_dtf1.m model_1_dtf0.m model_1_dtf1.m model_2_dtf0.m model_2_dtf1.m ~/maestro_rsch_stff/maestro/
	cd ~/maestro_rsch_stff/maestro
	rm edp_result.txt
	./het_mae 6 model_0_dtf0.m model_0_dtf1.m  model_1_dtf0.m model_1_dtf1.m model_2_dtf0.m model_2_dtf1.m data/hw/accelerator_4.m data/hw/accelerator_5.m

	cp edp_result.txt ~/spearmint/spearmint-lite/maestr  #|| cp ~/spearmint/spearmint-lite/maestr/big_num.txt ~/spearmint/spearmint-lite/maestr/edp_result.txt

	cd ~/spearmint/spearmint-lite/maestr
	python maestr_runner.py

done
