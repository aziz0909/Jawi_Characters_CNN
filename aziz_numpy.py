import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread, imsave, imresize
import h5py
import glob, cv2

f = h5py.File("jawi_dataset.hdf5", "a")  # create HDF5 file

try:
    dset1 = f.create_dataset("train_data", (2607, 784), dtype='float32')
    dset2 = f.create_dataset("train_label", (2607,), dtype='int32')
    dset3 = f.create_dataset("test_data", (311, 784), dtype='float32')
    dset4 = f.create_dataset("test_label", (311,), dtype='int32')
except:
    dset1 = f['/train_data']
    dset2 = f['/train_label']
    dset3 = f['/test_data']
    dset4 = f['/test_label']

def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])

filelist = glob.glob("train/36.Vi/*.bmp")
filelist2 = glob.glob("test/36.Vi/*.bmp")

# 1.Alif 2.Ba 3.Ta 4.Tsa 5.Jim 6.Hha 7.Kho 8.Dal 9.Thal 10.Ra 11.Zai 12.Seen
# 13.Sheen 14.Sad 15.Dhad 16.Tta 17.Dha 18.Ain 19.Ghain 20.Fa 21.Qaf 22.Kaf 23.Lam 24.Meem
# 25.Noon 26.Waw 27.Ha 28.Lamalif 29.Hamzah 30.Ya 31.Nga 32.Pa 33.Ga 34.Nya 35.Cha 36.Vi

x = 2539
y = 302
kelas = 36

for img2 in filelist:
    cvimg = cv2.imread(img2)

    try:
        cvimg = rgb2gray(cvimg)
        cvimg = np.array(cvimg, dtype='float32')
        cvimg = np.reshape(cvimg, 784)

    except:
        cvimg = np.array(cvimg, dtype='float32')
        cvimg = np.reshape(cvimg, 784)

    dset1[x] = cvimg
    dset2[x] = kelas
    # try:
    #     print(x)
    #     print(dset2[x])
    # except:
    #     print("Error Bodoh!")

    x +=1

print(x)

for img in filelist2:
    cvimg = cv2.imread(img)

    try:
        cvimg = rgb2gray(cvimg)
        cvimg = np.array(cvimg, dtype='float32')
        cvimg = np.reshape(cvimg, 784)

    except:
        cvimg = np.array(cvimg, dtype='float32')
        cvimg = np.reshape(cvimg, 784)

    dset3[y] = cvimg
    dset4[y] = kelas
    # try:
    #     print(y)
    #     print(dset4[y])
    # except:
    #     print("Error Bodoh!")

    y +=1

print(y)

f.close()
