import os
import shutil
from torchvision.datasets.folder import is_image_file

p_folder = './tmp/'
out_folder = './tmp_out/'
sub_folders = os.listdir(p_folder)
for sub_folder in sub_folders:
    sub_path = './tmp/' + sub_folder
    for root, _, fnames in sorted(os.walk(sub_path)):
        for fname in fnames:
            if is_image_file(fname):
                if "rgb" in fname:
                    old_path = os.path.join(root,fname)
                    new_name = fname.replace("rgb","")
                    new_path = out_folder + "train/" + new_name
                    shutil.move(old_path,new_path)
                else:
                    old_path = os.path.join(root,fname)
                    new_name = fname.replace("depth","")
                    new_path = out_folder + "train_dep/" + new_name
                    shutil.move(old_path,new_path)
