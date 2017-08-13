import tensorflow as tf
import sys
import os

input_dir = '/home/chengp/Pictures/test/'
pos_output_dir = '/home/chengp/Pictures/test_positive/'
neg_output_dir = '/home/chengp/Pictures/test_negative/'
label_lines = [line.rstrip() for line in tf.gfile.GFile("labels.txt")]
count = 0
# Unpersists graph from file
with tf.gfile.FastGFile("/home/chengp/Pictures/scripts/Multi-label-Inception-net/retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
	softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
	IDs = os.listdir(input_dir)
	for ID in IDs:
		path = os.path.join(input_dir, ID)
		dates = os.listdir(path)
		for date in dates:
			path1 = os.path.join(path, date)
			series_numbers = os.listdir(path1)
			for series_number in series_numbers:
					path2 = os.path.join(path1, series_number)
					filenames = os.listdir(path2)
					for filename in filenames:
						absolute_path = os.path.join(path2, filename)
              			# Read in the image_data
						image_data = tf.gfile.FastGFile(absolute_path, 'rb').read()
						predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})
						# Sort to show labels of first prediction in order of confidence
						top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
						if top_k[0] == 0:
							os.system('cp ' + absolute_path + ' ' + neg_output_dir + str(count)+'.jpg')
							count += 1
						else: 
							os.system('cp ' + absolute_path + ' ' + pos_output_dir + str(count)+'.jpg')
							count += 1
						
