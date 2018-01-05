# Jawi Characters CNN
In this project, I show how TensorFlow can be used to implement convolutional neural networks on Jawi characters.

## Description
* The main objective of this study is to investigate the effect of changing different parameters towards recognition accuracy.
* Jawi characters is training using convolutional neural network. 
* For first convolutional layer, 5x5 filter is used and max pooling is 2x2. And Second layer, Convolutional layer 64 – 5x5 Filter and same pooling layer 2x2. 
* This experiment apply a ReLU activation function to the output to introduce nonlinearities into the model on convolutional layers and Softmax function to generate value.  

## Result
Learning Rate | Accuracy
------------- | --------
η = 0.001 | 68.2%
η = 0.01 | 65.7%
η = 0.1 | 69%

## Credits
@Prof KO - ko@ukm.edu.my for provide image dataset
