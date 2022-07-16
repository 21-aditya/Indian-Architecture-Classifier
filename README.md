# Indian-Architecture-Classifier
Each and every state in India has its own magnificent architecture and to be able to classify each style would be of great significance to architectural and historic studies. Convolutional Neural Networks (CNN) have a track record of exhibiting promising results for architecture type classification due to their feature extraction capability.

In this project the main focus initially lies in collecting the dataset. Data collection and initial pre-processing was done manually, amounting to roughly 1700 images. Images in this dataset consist of various Architectural Styles pertaining to 9 classes, namely Cave-Architecture, Chola, Hoysala, Kalinga, Kerala, MaruGurjara, Mughal, Rajput and Tibetan.

The next part of the project focuses on using this dataset and feeding it as input to various Machine Learning techniques and analysing which one is better at classifying the different architectural styles correctly. First off we work on using CNN with a combination of Support Vector Machine (SVM) algorithm for better classification of architectures. Then we check out Keras InceptionV3 architecture and analyse how it performs with the data.

Fast-AI is a deep learning library which has high level components that give very good results. This is due to its layered architecture which has common underlying patterns of various deep learning techniques in terms of decoupled abstractions. We try the Fastai ResNet and VGG models to analyse how it classifies the architectural images accurately.

# Data-Set
Images of various types of Indian architecture were collected from the internet through web scraping. The types are, Cave architecture, Chola, Hoysala, Kalinga, Kerala, Maru-Gurjara, Mughal, Rajput, Tibetan. After this, manual refinement was done for duplicates and watermarks.
These images were then further refined by removing the pictures with humans and other objects taking up space in the frame. Data augmentation was also done in an attempt to increase the accuracy of our models.
The dataset used contains 1700 images which was used for 3 models (Fast- AI VGG, Fast-AI ResNet, CNN-SVM) and another version of the same which was augmented and preprocessed again to about 5500 images that was used for 1 model (InceptionV3).

# Sample Images
<table>
 <tr>
   <td>
    <img src="https://github.com/21-aditya/Indian-Architecture-Classifier/blob/Computer_Science/SampleImages/Screenshot%202022-07-16%20at%2010.55.31%20PM.png" width="450" height="450" align="left">
   </td>
   <td>
<img src="https://github.com/21-aditya/Indian-Architecture-Classifier/blob/Computer_Science/SampleImages/Screenshot%202022-07-16%20at%2010.57.19%20PM.png" width="450" height="450" align="left">
   </td>
 </tr>
</table>
