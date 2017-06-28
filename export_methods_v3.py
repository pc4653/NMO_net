import os
import scipy.misc
import dicom
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
group = 'NMO'

def category( desc ):
   if 'head'.lower() in desc.lower():
     result = 1;
   elif 'spine' in desc.lower():
     result = 1;
   else:
     result = 0;

   return result;

#def recognize(label_lines ):
#   position_lock = 1
#   orientation_lock = 1
#   mode_lock = 1
#   image_data = tf.gfile.FastGFile('temp.jpg', 'rb').read()

#   predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})
    
      # Sort to show labels of first prediction in order of confidence
#   top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
#   for node_id in top_k:
#      if (node_id in (0, 1)) and position_lock:
#          position = label_lines[node_id]
#          position_lock = 0
#      elif node_id in (2, 3, 4) and orientation_lock:
#          orientation = label_lines[node_id]
#          orientation_lock = 0
#      elif node_id in (5, 6, 7, 8, 9, 10, 11, 12, 13, 14) and mode_lock:
#          mode = label_lines[node_id]
#          mode_lock = 0
#   return position+'#'+orientation+'#'+mode 


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
	   desc = data.StudyDescription + '#' + data.SeriesDescription
	   if ' ' in desc:
	     desc = desc.replace(' ', '_')
	   if '&' in desc:
	     desc = desc.replace('&','and')
	   if '/' in desc:
	     desc = desc.replace('/','or')
   except AttributeError:
           print 'No Description'
	   print input_str
	   desc = 'missing'

   number = str(data.SeriesNumber) + '#' + str(data.InstanceNumber)
	   

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


   #name = group + '%' + desc + '%' + number + '%' + '[' + date + ']' + '%' + ID +'.jpg'
   result = category(desc)

   subpath = os.path.join(output_path, ID)
   if not os.path.isdir(subpath):
     os.mkdir(subpath)

   subpath = os.path.join(subpath, date)
   if not os.path.isdir(subpath):
     os.mkdir(subpath)

   subpath = os.path.join(subpath,str(data.SeriesNumber))
   if not os.path.isdir(subpath):
     os.mkdir(subpath)

   #output_string = os.path.join(subpath,name)
   if result == 1:
     #tagfile(name, tags)
       try:
         scipy.misc.toimage(data.pixel_array, cmin=0, cmax=255).save('temp.jpg')
       except ValueError:
         print 'ValueError'
         print input_str
       except TypeError:
         print 'TypeError'
         print input_str 
   




   return [str(data.InstanceNumber) + '%' + desc,subpath];
