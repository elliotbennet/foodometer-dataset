import os
import shutil

current_dir = os.path.dirname(os.path.realpath(__file__))
training_classes = os.listdir('{}datasets'.format(current_dir))
destination = 'train'

for directory in training_classes:
	class_dir = '{0}datasets/{1}'.format(current_dir, directory)
	for image in os.listdir(class_dir):
		file_name = os.path.join(class_dir, image)
		if (os.path.isfile(file_name)):
			shutil.copy(file_name, destination)
		else:
			print('File doesn't exist: {}'.format(file_name))
