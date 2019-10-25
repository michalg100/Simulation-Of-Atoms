'''
Analtsis_Species.py
Script that Goes through the species.out file and
analyzes how many time steps have been for each num_Moles&num_Specs (the atom types and their amount)
Usage:
python Analtsis_Species.py
The #'s are for exeute on the colleage computere
'''
import re
import os
f1 = 0.5
f2 = 0.25
f1_f2_list = []
f1_f2 = [] #[num_Moles, num_Specs, num_Timestep]
num_Moles = 0 
num_Specs = 0
num_Timestep = 0
inputFile = os.path.join(os.getcwd(),"species.out")
file = open(inputFile, 'r')
#inputFile_t = str('{}/nvt_BB_real/species.out'.format(run_dir))
#file = open(inputFile_t, 'r')
line = file.readline()
while line:
	# creating the reviews_list - an array of arrays that contains the full details required for each f1_f2	   
	if re.match(r"([0-9]+)", line):
		temp = re.match(r"([0-9])+[ ]+([0-9])+[ ]+([0-9])+", line)
		if temp:
			if num_Moles == 0 and num_Specs == 0 and num_Timestep == 0:
				num_Moles = int(temp.group(2))
				num_Specs = int(temp.group(3))
				num_Timestep = 1
				
				
			elif num_Moles == int(temp.group(2)) and num_Specs == int(temp.group(3)):
				num_Timestep = num_Timestep + 1
				
			elif num_Moles != int(temp.group(2)) or num_Specs != int(temp.group(3)):
				f1_f2.extend([num_Moles, num_Specs,num_Timestep])	
				f1_f2_list.append(f1_f2)
				f1_f2 = []
				num_Moles = int(temp.group(2))
				num_Specs = int(temp.group(3))
				num_Timestep = 1
	line = file.readline()
print(f1_f2_list)

file.close()

f1_f2_info_file = open(os.getcwd() + "\\result_f1=" + str(f1)+ "_f2=" + str(f2) + ".txt", 'w')
#f1_f2_info_file_t = str('{}/nvt_BB_real/all_results_for_f1_f2/result_f1='.format(run_dir)) + str(f1)+ "_f2=" + str(f2) +".txt"
#f1_f2_info_file = open(f1_f2_info_file_t, 'w')
str_forces = "f1 = " + str(f1) + " f2 = " + str(f2) + "\n"
f1_f2_info_file.write(str_forces + str(f1_f2_list))
f1_f2_info_file.close()
