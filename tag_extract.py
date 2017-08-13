import os

input_dir = '/home/chengp/Pictures/test/NMO_by_Patient/'
os.chdir(input_dir)
path = os.getcwd()
filenames = os.listdir(path)
for filename in filenames:
	input_dir1 = input_dir + filename + '/'
	os.chdir(input_dir1)
	filenames1 = os.listdir(input_dir1)
	for filename1 in filenames1:
		input_dir2 = input_dir1 + filename1 + '/'
		os.chdir(input_dir2)
		filenames2 = os.listdir(input_dir2)
		for filename2 in filenames2:			
			if (not 'T1' in filename2) and (not 'T2' in filename2):
				os.system('rm -r ' + filename2)
				
	os.chdir(input_dir)

