import os
import timeit
import cv2
from skimage import io as io
import face_recognition as fr
import numpy as np
import pickle
from tqdm import tqdm
from sklearn import datasets, svm, metrics

def main():
    print('Read dataset..., image file name format: 25_f_uuid4.jpg, 25 is age, f is female')
    gender_data = list()
    for fn in tqdm(os.listdir('data')):
        try:
            if fn.split('.')[1] == 'jpg':
                # print('Processing {}'.format(fn))
                gender_label = fn.split('_')[1]
                img = io.imread(os.path.join('data', fn))
                face_embedding = fr.face_encodings(img)
                if len(face_embedding) != 1:
                    # print('Above one face in an image, skip..')
                    continue
                single_data = list()
                single_data.append(face_embedding[0])
                single_data.append(gender_label)
                gender_data.append(single_data)
            else:
                continue
        except:
            continue

    print('Saving as a pkl file')
    with open('gender_data.pkl','wb') as f:
        pickle.dump(gender_data, f)
    print('Finished')


if __name__ == '__main__':
    main()



