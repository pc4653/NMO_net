import os
import dicom

def categorize( input_str):
	try: 
		data = dicom.read_file(input_str)
	except dicom.errors.InvalidDicomError:
		print 'InvalidDicomError'
		print input_str
		return;
	
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


input_dir = '/home/chengp/Pictures/NMO_Patient/'
os.chdir(input_dir)
path = os.getcwd()
filenames = os.listdir(path)
study_dic = {}
series_dic = {}
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
			series_dic.update({series_desc:1})



	os.chdir(input_dir)
	
for item in study_dic:
	print item + '  count:' + str(study_dic[item])
print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
for item in series_dic:
	print item + '  count:' + str(series_dic[item])
