# gender_classifier_dlib_transfer_learning
[![codebeat badge](https://codebeat.co/badges/1ef6ec71-05e5-4b11-8d14-af0eb96a067b)](https://codebeat.co/projects/github-com-cftang0827-face_gender-master)

A simple demo of gender classifier by using dlib face recognition model as a feature extractor

By using dlib face recognition model, we can do transfer learning to classify gender of face, using sklearn ML framwork.
The traning dataset is all asian face, due to the lack of public asian gender dataset.
However, there are many private picture from my own, so I am not going to share the dataset.

If you are intrested in trainig by yourself, you can use google photo crawler to download image and label my your self
https://github.com/hellock/icrawler

I also provided simple pretrained model if you want to use.


Here is the evaluation metric


                   precision    recall  f1-score   support

              f        0.90      0.99      0.94       159
              m        0.99      0.91      0.95       189

     avg / total       0.95      0.95      0.95       348

## Environment 
* MacOS or Ubuntu
* face_recognition 1.2.2
* dlib 19.10.0
* Python 3.6.4
* sklearn 0.19.1
* skimage 0.13.1

## How to run the code and set prerequisite ?
First, you need to set up the environment of dlib, sklearn and face_recognition, however, you cannot simply use ```pip install ``` to install dlib, you should build it from source or use ```conda install -c menpo dlib``` to install it. It is a tricky step, so I prepare the whole installation script for opencv, dlib, face_recognition and the other useful library for computer vision and machine learning in Python 3.6, here is the link

https://github.com/cftang0827/python-computer-vision-env_install

Or if you don't want to use whole script, you could follow the installation step from face_recognition API
https://github.com/ageitgey/face_recognition#installation-options

It's quite simple and useful
