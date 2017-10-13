import h5py
import png
import numpy as np
import scipy.io
import sys
import os
from skimage.io import imsave

if len(sys.argv) < 4:
    print("usage: %s <h5_file> <train_test_split> <out_folder>" % sys.argv[0])
    sys.exit(0)

h5_file = h5py.File(sys.argv[1],"r")
split = scipy.io.loadmat(sys.argv[2])
out_folder = sys.argv[3]

def save_to_file(image, depth, train_index, test_index):
    idx = int(i) + 1
    if idx in train_index:
        phase = "training"
    else:
        assert idx in test_index, "index %d neither found in training set nor in test set" % idx
        phase = "testing"

    folder = "%s/%s" % (out_folder, phase)
    if not os.path.exists(folder):
        os.makedirs(folder)
    depth *= 5000.0
    depth = np.rint(depth)

    imsave("%s/%04d_colors.png" % (folder,idx), image)
    png.from_array(depth,'L;16').save('%s/%04d_depth.png' % (folder,idx))

train_index = set([int(x) for x in split["trainNdxs"]])
test_index  = set([int(x) for x in split["testNdxs"]])
print("%d training images" % len(train_index))
print("%d test images" % len(test_index))

images = h5_file['images']
depths = h5_file['depths']

for i, image in enumerate(images):
    save_to_file(image.T, depths[i,:,:].T, train_index, test_index)
