from __future__ import print_function
import os
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

import time
import keras
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D


batch_size = 32

#change this
num_classes = 4
epochs = 20

data_augmentation = False
num_predictions = 20
size = 400,400
save_dir = os.path.join(os.getcwd(), 'Tangsancai/model_to_reformat/')
images = []
labels = []

#change this
classes = {
	'gf' : [0],
	'tydtz' : [1],
    'tzla' : [2],
    'tzm' : [3]
}
all_classes = []
dirr = []

for i in classes:
		all_classes.append(i)
		
direc = os.getcwd()

#change分隔符以及路径
#windows上"\\"，linux上"/"
#目前路径为linux上的
for i in all_classes:
		dirr.append(direc + "/Tangsancai/" + i + "/")
		#print(i)

model_name = ''
for i in classes:
		model_name += i + '_'

model_name += str(time.time()) + '.h5'
#model_name = 'trained_model_horse_man_fake_plate.h5'

def transform_pic(pic_dir):
	im = Image.open(pic_dir)
	if im:
		im.thumbnail(size)
		#此时图片长128，宽不确定
		background = Image.new('RGB', size, (105,105,105,105))
		background.paste(im)
		#长比宽多的部分用灰色添上了
		return np.array(background)

def show_pic(pic_dir):
	pic = transform_pic(pic_dir)
	plt.imshow(pic, cmap = plt.cm.binary)
	plt.show()
	#print('shape: '+ str(pic.shape))

def load_pics(each_dir):
	for n in os.listdir(each_dir):    
		pdir = each_dir + n
		p = transform_pic(pdir)
		images.append(p)

		for temp in classes:
			if temp in each_dir:
				labels.append(classes[temp])
				break
		'''
		if 'fake_horse' in each_dir:
			labels.append(classes['fake_horse'])
		else:
			labels.append(classes['horse'])
		'''

#change this
for i in dirr:
	print(i)
for i in dirr:
	load_pics(i)
'''
load_pics(horse_dir)
load_pics(man_dir)
load_pics(fake_dir)
load_pics(plate_dir)
'''
x = np.array(images)
y = np.array(labels)
print('x: ' + str(x.shape))
print('y: ' + str(y.shape))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state= 30)


#test section
print('x_train: ' + str(x_train.shape))
print('y_train: ' + str(y_train.shape))
print('x_test: ' + str(x_test.shape))
print('y_test: ' + str(y_test.shape))
print('train 43: ' + str(y_train[43]))
plt.imshow(x_train[43])
plt.show()
print('test 4: ' + str(y_test[4]))
plt.imshow(x_test[4])
plt.show()

#后面我直接把cifar10的示例程序拷贝过来了
# Convert class vectors to binary class matrices.
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same',
				 input_shape=x_train.shape[1:]))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes))
model.add(Activation('softmax'))

# initiate RMSprop optimizer
#opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)
opt = keras.optimizers.Adagrad(lr=0.001, epsilon=None, decay=0.0)

# Let's train the model using RMSprop
model.compile(loss='categorical_crossentropy',
				optimizer=opt,
				metrics=['accuracy'])

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

if not data_augmentation:
	print('Not using data augmentation.')
	model.fit(x_train, y_train,
				batch_size=batch_size,
				epochs=epochs,
				validation_data=(x_test, y_test),
				shuffle=True)
else:
	print('Using real-time data augmentation.')
	# This will do preprocessing and realtime data augmentation:
	datagen = ImageDataGenerator(
		featurewise_center=False,  # set input mean to 0 over the dataset
		samplewise_center=False,  # set each sample mean to 0
		featurewise_std_normalization=False,  # divide inputs by std of the dataset
		samplewise_std_normalization=False,  # divide each input by its std
		zca_whitening=False,  # apply ZCA whitening
		zca_epsilon=1e-06,  # epsilon for ZCA whitening
		rotation_range=0,  # randomly rotate images in the range (degrees, 0 to 180)
		# randomly shift images horizontally (fraction of total width)
		width_shift_range=0.1,
		# randomly shift images vertically (fraction of total height)
		height_shift_range=0.1,
		shear_range=0.,  # set range for random shear
		zoom_range=0.,  # set range for random zoom
		channel_shift_range=0.,  # set range for random channel shifts
		# set mode for filling points outside the input boundaries
		fill_mode='nearest',
		cval=0.,  # value used for fill_mode = "constant"
		horizontal_flip=True,  # randomly flip images
		vertical_flip=False,  # randomly flip images
		# set rescaling factor (applied before any other transformation)
		rescale=None,
		# set function that will be applied on each input
		preprocessing_function=None,
		# image data format, either "channels_first" or "channels_last"
		data_format=None,
		# fraction of images reserved for validation (strictly between 0 and 1)
		validation_split=0.0)

	# Compute quantities required for feature-wise normalization
	# (std, mean, and principal components if ZCA whitening is applied).
	datagen.fit(x_train)

	# Fit the model on the batches generated by datagen.flow().
	model.fit_generator(datagen.flow(x_train, y_train,
									 batch_size=batch_size),
						epochs=epochs,
						validation_data=(x_test, y_test),
						workers=4)

# Save model and weights
if not os.path.isdir(save_dir):
	os.makedirs(save_dir)
model_path = os.path.join(save_dir, model_name)
model.save(model_path)
print('Saved trained model at %s ' % model_path)

# Score trained model.
scores = model.evaluate(x_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])






