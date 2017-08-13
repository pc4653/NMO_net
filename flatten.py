import os
input_dir = '/home/chengp/Pictures/positive/'
os.chdir(input_dir)
path = os.getcwd()
count = 0
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
			os.chdir(final_path)
			files = os.listdir(final_path)
			for file in files:
				os.system('cp ' + file + ' ' + input_dir+str(count)+'.jpg')
				count += 1
print count