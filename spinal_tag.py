import os
input_dir = '/home/chengp/Pictures/image/'
os.chdir(input_dir)
filenames = os.listdir(input_dir)
for filename in filenames:
	f = open('/home/chengp/Pictures/spinal_tagss/'+filename+'.txt' , 'w')
	f.write('yes_spinal_inside')
	f.close()
	
	