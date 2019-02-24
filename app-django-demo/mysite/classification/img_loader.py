from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

def transform_original_pic(pic_dir):
    im = Image.open(pic_dir)
    return np.array(im)

def most_frequent_colour(pic_dir):
    image = Image.open(pic_dir)
    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)

    return most_frequent_pixel


def transform_pic(pic_dir, size):
    im = Image.open(pic_dir)
    im.thumbnail(size)
    #此时图片长128，宽不确定
    background = Image.new('RGB', size, (105,105,105,105))
    background.paste(im)
    #长比宽多的部分用灰色添上了
    return np.array(background)

def show_pic(pic_dir, size):
    pic = transform_pic(pic_dir, size)
    plt.imshow(pic, cmap = plt.cm.binary)
    #plt.show()
    #print('shape: '+ str(pic.shape))

def get_clean_pic(pic_dir):

    # load image
    img = cv2.imread(pic_dir)
    #rsz_img = cv2.resize(img, fx=0.25, fy=0.25)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # threshold to get just the signature
    ret, thresh_gray = cv2.threshold(gray, thresh=100, maxval=255, type=cv2.THRESH_BINARY)
    #cv2.imshow("Cropped and thresholded gray image", thresh_gray)
    #cv2.waitKey(4000)

    # find where the signature is and make a cropped region
    points = np.argwhere(thresh_gray == 0)  # find where the black pixels are
    points = np.fliplr(points)  # store them in x,y coordinates instead of row,col indices
    x, y, w, h = cv2.boundingRect(points)  # create a rectangle around those points
    x, y, w, h = x - 10, y - 10, w + 20, h + 20  # make the box a little bigger
    crop = gray[y:y + h, x:x + w]  # create a cropped region of the gray image

    # get the thresholded crop
    ret, thresh_crop = cv2.threshold(crop, thresh=200, maxval=255, type=cv2.THRESH_BINARY)

    # display
    cv2.imshow("Cropped and thresholded image", thresh_crop)
    cv2.waitKey(0)

def contourtest(pic_dir):

    im = cv2.imread(pic_dir)
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("window title", imgray)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    im2 = cv2.drawContours(im2, contours, -1, (0,255,0), 3)
    cv2.imshow("window title", im2)
    cv2.waitKey()

#plt.imshow(transform_original_pic(pic_dir))
#plt.show()
#get_clean_pic(pic_dir)
#contourtest(pic_dir)