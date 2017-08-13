import os
input_dir = '/home/chengp/Pictures/positive/'
compare_dir = '/home/chengp/Pictures/T12_NMO_by_Patient_1/'
output_dir = '/home/chengp/Pictures/Sag_Spine_not_spinal/'
os.chdir(input_dir)
path = os.getcwd()
count = 1311
filenames = os.listdir(path)
for filename in filenames:
	new_path = input_dir + filename + '/'
	#os.chdir(new_path)
	folders = os.listdir(new_path)
	for folder in folders:
		newer_path = new_path + folder + '/'
		more_folders = os.listdir(newer_path)
		for more_folder in more_folders:
			final_path = newer_path + more_folder + '/'
			comp_path = compare_dir + filename + '/' + folder + '/' + more_folder + '/'
			os.chdir(comp_path)
			files = os.listdir(final_path)
			comp_files = os.listdir(comp_path)
			for comp_file in comp_files:
				if not comp_file in files:
					os.system('cp ' + comp_file + ' ' + input_dir+str(count)+'.jpg')
					count += 1
print count