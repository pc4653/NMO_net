import dicom
import os
import scipy.misc
from export_methods_v3 import *

tags = open('/home/chengp/Pictures/labels.txt').readlines()
label_lines = map(str.strip, tags)

output_path = '/home/chengp/Pictures/NMO_by_Patient/'

#create_dir(output_path)

input_dir = '/home/chengp/Pictures/NMO_Patient/'

with tf.gfile.FastGFile("/home/chengp/Pictures/scripts/Multi-label-Inception-net/retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

sess = tf.Session()
softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

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
     [desc, subpath] = read_export(input_path, output_path)
     position_lock = 1
     orientation_lock = 1
     mode_lock = 1
     image_data = tf.gfile.FastGFile('temp.jpg', 'rb').read()

     predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})
    
      # Sort to show labels of first prediction in order of confidence
     top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
     for node_id in top_k:
      if (node_id in (0, 1)) and position_lock:
          position = label_lines[node_id]
          position_lock = 0
      elif node_id in (2, 3, 4) and orientation_lock:
          orientation = label_lines[node_id]
          orientation_lock = 0
      elif node_id in (5, 6, 7, 8, 9, 10, 11, 12, 13, 14) and mode_lock:
          mode = label_lines[node_id]
          mode_lock = 0
     net_result = position+'#'+orientation+'#'+mode 
     name = net_result + '%' + desc + '.jpg'
     output_string = os.path.join(subpath,name)
     os.system('mv temp.jpg ' + output_string)



   os.chdir(input_dir)





