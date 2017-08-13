import shutil
import os

path = '/home/chengp/Pictures/T12_NMO_by_Patient_1/'
output_path = '/home/chengp/Pictures/Spines/'
patientID = os.listdir(path)
for patient in patientID:
	content_path = path+patient+'/'
	content = os.listdir(content_path)
	for series in content:
		if 'spine' in series.lower() or 'neck' in series.lower():
			shutil.copytree(content_path+series, output_path+patient+'/'+series)