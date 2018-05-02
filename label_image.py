import tensorflow as tf
import sys
import os

# change this as you see fit
capture = sys.argv[2]
capture = int(capture)
if capture == 1:
	if os.path.exists('/home/pi/image.jpg'):
		os.remove('/home/pi/image.jpg')
		# print('Previous Image Removed')
	# else:
		# print('Image not present')

	# print('Capturing Image')
	os.system('python /home/pi/picamera-test.py')


	# if os.path.exists('/home/pi/image.jpg'):
		# print('Image found')
# else:
	# print('Not using captured image')

image_path = sys.argv[1]

# Read in the image_data
image_data = tf.gfile.FastGFile(image_path, 'rb').read()

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line 
				   in tf.gfile.GFile('/home/pi/tf_files/retrained_labels.txt')]

# Unpersists graph from file
with tf.gfile.FastGFile("/home/pi/tf_files/retrained_graph.pb", 'rb') as f:
	graph_def = tf.GraphDef()
	graph_def.ParseFromString(f.read())
	_ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
	# Feed the image_data as input to the graph and get first prediction
	softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
	
	predictions = sess.run(softmax_tensor, \
			 {'DecodeJpeg/contents:0': image_data})
	
	# Sort to show labels of first prediction in order of confidence
	top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
	
	for node_id in top_k:
		human_string = label_lines[node_id]
		score = predictions[0][node_id]
		print('%s (score = %.5f)' % (human_string, score))
