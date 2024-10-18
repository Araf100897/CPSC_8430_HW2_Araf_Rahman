# CPSC_8430_HW2_Araf_Rahman
 
To begin training, ensure that the ModelSaveLoc variable is set to "TrainedModels" and confirm that train=True, within the main_execution() function in the tr1.py file (this is the default setting). The models in this version are trained for 10 epochs.

Before running the bash script "hw2_seq2seq.sh", check the main function and confirm that train=False and test=True are correctly assigned.

For testing, set the ModelSaveLoc to "BestModel" in the testmodel() function of Videocaptioning_main.py (also the default setting), then execute the "hw2_seq2seq.sh" script using "testing_data" and "result3.txt" as input (during the testing phase).

The BLEU scores for the top two models can be found in the file titled "final_result.csv".

The best-performing model:

model_batchsize_32_hidsize_128_DP_0.4_worddim_2048.h5 (BLEU Score: 0.6759887467657024).
