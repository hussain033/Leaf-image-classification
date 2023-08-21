# Leaf Image Classification

Welcome to the Leaf Image Classification repository! This project focuses on the development of a deep learning model for accurately identifying plant species through leaf images. The project utilizes the MobileNet_v2 architecture with transfer learning and data augmentation techniques. The model achieves an impressive accuracy of 92% on unseen data, making it a valuable resource for plant identification and learning.

## Introduction

### Background
Identifying plant species can be challenging due to the vast variety of plants. This project aims to simplify plant identification by creating a leaf image classification system using deep learning.

### Objective
The primary objective is to develop a system capable of accurately identifying plant species based on leaf images. This system provides an efficient solution for gathering information about plants for common users.

## Methodology

### Data Collection and Augmentation
A diverse dataset of plant leaves was collected for model training. To enhance the dataset and prevent overfitting, various data augmentation techniques were applied, including rotation, flipping, and scaling. This augmented dataset improves the model's performance and generalization.

### Model Development with MobileNet_v2 and Transfer Learning
The deep learning model is developed using transfer learning with the MobileNet_v2 architecture. MobileNet_v2 is renowned for its excellent performance in image classification tasks. Transfer learning allows us to adapt the pretrained MobileNet_v2 model to our specific classification task, leveraging its learned features and reducing training time.

## Usage

### Inference
To use the leaf image classification model for inference, follow these steps:

1. Cloning the repository: 
   ```
   git clone https://github.com/hussain033/Leaf-image-classification
   ```
3. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
4. Place your leaf image in the appropriate directory.
5. Run the inference script:
   ```
   python inference.py path/to/your/image.jpg
   ```

### Experimentation
You can experiment with the model training of the project by replacing the mobilenetv2 model with any other image classification such as resnet, alexnet to mention a few. 
We have provided the model training ipynb file, feel free to experiment with it by cloning the repo.

for Cloning the repo, use the following command:
``` 
git clone https://github.com/hussain033/Leaf-image-classification
```

The Dataset is divided into train, test and validation set and there are totally 12 classes.

## Results

The developed model achieves an accuracy rate of 92% on unseen data. This high accuracy demonstrates the model's proficiency in identifying plant species from leaf images. Transfer learning with MobileNet_v2 and the augmented dataset significantly contribute to the model's success.

## Conclusion

The Leaf Image Classification project provides an effective solution for plant species identification. By leveraging transfer learning with MobileNet_v2 and applying data augmentation, the model achieves an impressive accuracy rate. This system serves as a valuable tool for users seeking to identify and learn about plants.


