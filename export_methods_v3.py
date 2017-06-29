import os
import scipy.misc
import dicom

def category( desc ):
	if 'head'.lower() in desc.lower():
		result = 1;
	elif 'spine' in desc.lower():
		result = 1;
	else:
		result = 0;

	return result;


#def tagfile( name, tags ):
#   f = open('/home/chengp/Pictures/NMO_tags/'+name+'.txt' , 'w')
#   for tag in tags:
#      if tag.lower() in name.lower():
#          f.write(tag)
#   f.close()

def read_export(input_str, output_path):
	try: 
		data = dicom.read_file(input_str)
	except dicom.errors.InvalidDicomError:
		print 'InvalidDicomError'
		print input_str
		return;
	ID = str(data.PatientID)
	try:
		study_desc = data.StudyDescription
		if ' ' in study_desc:
			study_desc = study_desc.replace(' ', '_')
		if '&' in study_desc:
			study_desc = study_desc.replace('&','and')
		if '/' in study_desc:
			study_desc = study_desc.replace('/','or')
	except AttributeError:
		print 'No Study Description'
		print input_str
		study_desc = 'missing'
		
		
	try:
		series_desc = data.SeriesDescription
		if ' ' in series_desc:
			series_desc = series_desc.replace(' ', '_')
		if '&' in series_desc:
			series_desc = series_desc.replace('&','and')
		if '/' in series_desc:
			series_desc = series_desc.replace('/','or')
	except AttributeError:
		print 'No Series Description'
		print input_str
		series_desc = 'missing'
	   

	try:
		date = str(data.AcquisitionDate)
	except AttributeError:
		print 'NO AcquisitionDate'
		print input_str
		try: 
			date = str(data.StudyDate)
		except AttributeError:
			print 'NO StudyDate'
			date = 'missing'

	study_date = study_desc + '[' + date + ']'
	name = '%' + str(data.InstanceNumber) + '.jpg'
	#result = category(desc)

	subpath = os.path.join(output_path, ID)
	if not os.path.isdir(subpath):
		os.mkdir(subpath)

	subpath = os.path.join(subpath, study_date)
	if not os.path.isdir(subpath):
		os.mkdir(subpath)

	subpath = os.path.join(subpath,str(data.SeriesNumber) + '%%' + series_desc)
	if not os.path.isdir(subpath):
		os.mkdir(subpath)

	output_string = os.path.join(subpath,name)
	if not os.path.isfile(output_string):
		try:
			scipy.misc.toimage(data.pixel_array, cmin=0, cmax=255).save(output_string)
		except ValueError:
			print 'ValueError'
			print input_str
		except TypeError:
			print 'TypeError'
			print input_str 
   




	return;
