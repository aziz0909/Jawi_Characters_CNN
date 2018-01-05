from PIL import Image
import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.misc import imread, imsave, imresize

def rgb2gray(rgb):
    return cv2.resize(255-rgb, (28, 28))

x = 1
# filelist = glob.glob("train/4.Tsa/*.bmp")
filelist = glob.glob("train/5.Jim/*.bmp")
# filelist = glob.glob("test/6.Hha/*.bmp")
# filelist = glob.glob("test/7.Kho/*.bmp")
# filelist = glob.glob("test/8.Dal/*.bmp")
# filelist = glob.glob("test/9.Thal/*.bmp")
# filelist = glob.glob("test/10.Ra/*.bmp")
# filelist = glob.glob("test/11.Zai/*.bmp")
# filelist = glob.glob("test/12.Seen/*.bmp")
# filelist = glob.glob("test/13.Sheen/*.bmp")
# filelist = glob.glob("test/14.Sad/*.bmp")
# filelist = glob.glob("test/15.Dhad/*.bmp")
# filelist = glob.glob("test/16.Tta/*.bmp")
# filelist = glob.glob("test/17.Dha/*.bmp")
# filelist = glob.glob("test/18.Ain/*.bmp")
# filelist = glob.glob("test/19.Ghain/*.bmp")
# filelist = glob.glob("test/20.Fa/*.bmp")
# filelist = glob.glob("test/21.Qaf/*.bmp")
# filelist = glob.glob("test/22.Kaf/*.bmp")
# filelist = glob.glob("test/23.Lam/*.bmp")
# filelist = glob.glob("test/24.Meem/*.bmp")
# filelist = glob.glob("test/25.Noon/*.bmp")
# filelist = glob.glob("test/26.Waw/*.bmp")
# filelist = glob.glob("test/27.Ha/*.bmp")
# filelist = glob.glob("test/28.Lamalif/*.bmp")
# filelist = glob.glob("test/29.Hamzah/*.bmp")
# filelist = glob.glob("test/30.Ya/*.bmp")
# filelist = glob.glob("test/31.Nga/*.bmp")
# filelist = glob.glob("test/32.Pa/*.bmp")
# filelist = glob.glob("test/33.Ga/*.bmp")
# filelist = glob.glob("test/34.Nya/*.bmp")
# filelist = glob.glob("test/35.Cha/*.bmp")
# filelist = glob.glob("test/36.Vi/*.bmp")

for img in filelist:
    cvimg = imread(img)
    # try:
    #     gray = rgb2gray(cvimg)
    #     # newimg = imresize(gray, (20, 20))
    #
    # except:
    #     newimg = imresize(cvimg, (20, 20))

    # plt.imshow(newimg, cmap=plt.get_cmap('gray'))
    # plt.show()

    gray = rgb2gray(cvimg)
    x = str(x)
    a = ('new/' + x + '.bmp')
    imsave(a, gray)
    x = int(x)
    x += 1
