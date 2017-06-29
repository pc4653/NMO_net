import os
import dicom
import operator
def categorize( input_str):
	try: 
		data = dicom.read_file(input_str)
	except dicom.errors.InvalidDicomError:
		print 'InvalidDicomError'
		print input_str
		return ['N/A','N/A'];
	
	try:
		study_desc = data.StudyDescription
	except AttributeError:
		print 'No Description'
		print input_str
		study_desc = 'missing'
	try:
		series_desc = data.SeriesDescription
	except AttributeError:
		print 'No Description'
		print input_str
		series_desc = 'missing'
	
	
	return [study_desc, series_desc];

tags = open('/home/chengp/Pictures/labels.txt').readlines()
label_lines = map(str.strip, tags)
input_dir = '/home/chengp/Pictures/Other_Patient/'
count = {'Head' : 0 , 'Spine' : 0 , 'Ax' : 0 , 'Cor' : 0 , 'Sag' : 0 , 'ce_MRV' : 0, 'Tensor' : 0, 'Diffusion':0, 'ASSET':0, 'MRA':0, 'T1':0, 'T2':0, 'DTI':0, 'PROBE-SI':0, 'DWI':0}
os.chdir(input_dir)
path = os.getcwd()
filenames = os.listdir(path)
study_dic = {}
series_dic = {}
study_total = 0
for filename in filenames:

	os.chdir(filename)
	path1 = os.getcwd()
	input_data = input_dir + filename + '/'
	filenames1 = os.listdir(path1)
	for filename1 in filenames1:
		input_path = input_data + filename1
		[study_desc, series_desc] = categorize(input_path)
		if study_dic.has_key(study_desc):
			study_dic[study_desc] = study_dic[study_desc] + 1
		else:
			study_dic.update({study_desc:1})
		if series_dic.has_key(series_desc):
			series_dic[series_desc] = series_dic[series_desc] + 1
		else:
			series_dic.update({series_desc:1})



	os.chdir(input_dir)
for item in study_dic:
	study_total = study_total + study_dic[item]
	for label in label_lines:
		if label.lower() in item.lower():
			count[label] = count[label] + study_dic[item]
			
			
			
sorted_study = sorted(study_dic.items(),key=operator.itemgetter(1),reverse=True)
for x in sorted_study:
	print x
print study_total
print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
series_total = 0
for item in series_dic:
	series_total = series_total + series_dic[item]
	for label in label_lines:
		if label.lower() in item.lower():
			count[label] = count[label] + series_dic[item]
			
			
sorted_series = sorted(series_dic.items(),key=operator.itemgetter(1),reverse=True)
for x in sorted_series:
	print x
print series_total
print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
print count