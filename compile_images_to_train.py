import os
import shutil

training_classes = os.listdir('datasets')
destination = 'train'

for directory in training_classes:
	class_dir = 'datasets/{}'.format(directory)
	for image in os.listdir(class_dir):
		file_name = os.path.join(class_dir, image)
		if (os.path.isfile(file_name)):
			shutil.copy(file_name, destination)
		else:
			print("File doesn't exist: {}'.format(file_name))
