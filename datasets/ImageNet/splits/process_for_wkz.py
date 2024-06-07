import pickle as pk
import numpy as np
import os

# train doesn't need to be processed, but we need to extract the folder-classname mapping 
train_split = '/mnt/nasv2/hhz/LaBo/datasets/ImageNet/splits/class2images_train.p'

train = pk.load(open(train_split, 'rb'))
classname2folder_m = {}
for k, v in train.items():
    classname = k
    folder = v[0].split('/')[1]
    if k not in classname2folder_m.keys():
        classname2folder_m[classname] = folder
    else:
        raise ValueError('Duplicate class name')
        
val_split = '/mnt/nasv2/hhz/LaBo/datasets/ImageNet/splits/class2images_val.p'
new_val_split = '/mnt/nasv2/hhz/LaBo/datasets/ImageNet/splits/wkz_class2images_val.p'
val = pk.load(open(val_split, 'rb'))
for k, v in val.items():
    folder = classname2folder_m[k]
    for i in range(len(v)):
        assert 'val' in v[i], ValueError(f'Not a val image, {v[i]}')
        v[i] = os.path.join('val', folder, v[i].split('/')[-1])
with open(new_val_split, 'wb') as f:
    pk.dump(val, f)

test_split = '/mnt/nasv2/hhz/LaBo/datasets/ImageNet/splits/class2images_test.p'
new_test_split = '/mnt/nasv2/hhz/LaBo/datasets/ImageNet/splits/wkz_class2images_test.p'
test = pk.load(open(test_split, 'rb'))
for k, v in test.items():
    folder = classname2folder_m[k]
    for i in range(len(v)):
        assert 'val' in v[i], ValueError(f'Not a test image, {v[i]}')
        v[i] = os.path.join('val', folder, v[i].split('/')[-1])
with open(new_test_split, 'wb') as f:
    pk.dump(test, f)