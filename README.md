# gender_classifier_dlib_transfer_learning
A simple demo of gender classifier by using dlib face recognition model as a feature extractor

By using dlib face recognition model, we can do transfer learning to classify gender of face, using sklearn ML framwork.
The traning dataset is all asian face, due to the lack of public asian gender dataset.
However, there are many private picture from my own, so I am not going to share the dataset.

If you are intrested in trainig by yourself, you can use google photo crawler to download image and label my your self
https://github.com/hellock/icrawler

I also provided simple pretrained model if you want to use.


Here is the evaluation metric


                 precision    recall  f1-score   support

              f       0.90      0.99      0.94       159
              m       0.99      0.91      0.95       189

     avg / total       0.95      0.95      0.95       348
