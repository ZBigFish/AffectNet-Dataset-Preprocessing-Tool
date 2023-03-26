
import csv
import os

import cv2
from tqdm import tqdm

data_folder = 'Manually_Annotated_Images/'
done = 'AffectNet_class/'
train_file = 'training.csv'
test_file = 'validation.csv'


def align_img(img, x, y, width, height):
    W, H, C = img.shape
    x = 0 if x < 0 else x
    y = 0 if y < 0 else y
    aw = W if x + width > W else x + width
    ah = H if y + height > H else y + height
    return img[x:aw, y:ah]


fname = []
face_x = []
face_y = []
face_width = []
face_height = []
expression = []
num = 0
with open(train_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    print('load file complete!')
    for row in tqdm(reader, unit="pic"):
        if int(row['expression']) > 7:
            continue
        # there is a god damn wrong in row 315313 of training.csv. where the face_x and face_y is NULL for string!
        if row['face_x']=='NULL' or row['face_y']=='NULL' or int(row['face_width'])<0 or int(row['face_height'])<0:
            continue
        num += 1
        fname = row['subDirectory_filePath']
        x = int(row['face_x'])
        y = int(row['face_y'])
        width = int(row['face_width'])
        height = int(row['face_height'])
        expression = int(row['expression'])
        floder_dir = fname.split('/')[0]
        img = fname.split('/')[1]
        image = cv2.imread(os.path.join(data_folder, fname))

        # process img
        imgROI = align_img(image, x, y, width, height)
        imgROI = cv2.resize(imgROI, (224, 224), interpolation=cv2.INTER_AREA)

        cv2.imwrite(done + 'train/' + str(expression) + '/' + str(num) + '.jpg', imgROI)

    print(num)

num1 = 0
with open(test_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    print('load file complete!')
    for row in tqdm(reader, unit="pic"):
        if int(row['expression']) > 7:
            continue
        num1 += 1
        fname = row['subDirectory_filePath']
        x = int(row['face_x'])
        y = int(row['face_y'])
        width = int(row['face_width'])
        height = int(row['face_height'])
        expression = int(row['expression'])
        floder_dir = fname.split('/')[0]
        img = fname.split('/')[1]

        image = cv2.imread(os.path.join(data_folder, fname))

        # process img

        imgROI = align_img(image, x, y, width, height)
        imgROI = cv2.resize(imgROI, (224, 224), interpolation=cv2.INTER_AREA)

        cv2.imwrite(done + 'test/' + str(expression) + '/' + str(num1) + '.jpg', imgROI)

print('There are {} facial image of 8 expressions'.format(str(num + num1)))
print('Train set: {} images'.format(str(num)))
print('Test set: {} images'.format(str(num1)))
