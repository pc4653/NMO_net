import dicom
import os
import scipy.misc
from export_methods_v3 import *

tags = open('/home/chengp/Pictures/labels.txt').readlines()
label_lines = map(str.strip, tags)

output_path = '/home/chengp/Pictures/NMO_by_Patient/'

#create_dir(output_path)

input_dir = '/home/chengp/Pictures/NMO_Patient/'

os.chdir(input_dir)
path = os.getcwd()
filenames = os.listdir(path)
for filename in filenames:

   os.chdir(filename)
   path1 = os.getcwd()
   input_data = input_dir + filename + '/'
   filenames1 = os.listdir(path1)
   for filename1 in filenames1:
     input_path = input_data + filename1
     read_export(input_path, output_path)



   os.chdir(input_dir)





