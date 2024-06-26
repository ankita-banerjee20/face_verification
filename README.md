# Face Verification App Using Siamese Model

## Overview:
The Face Verification App is a computer application that utilizes a custom deep learning Siamese model for verifying faces captured through the device's camera. The app compares the input face with a set of verification images and determines whether the input face matches with verified faces.

> [!IMPORTANT]
> This app is still in beta phase.

## Features:
- Face verification using a custom neural network model.
- Real-time face detection and capture through the device's camera.
- Support for comparing the input face with multiple verification images.
- User-friendly interface displaying verification results.

## Usage:
- Allow the app to access your device's camera.
- Position your face within the camera frame.
- The app will capture your face and compare it with the stored verification images.
- If the similarity between your face and any verification image exceeds a certain threshold, the app will display a "Verified" status. Otherwise, it will display an "Unverified" status.


## Getting Started:
To kickstart the face verification app follow the next section to ensure proper installation and configuration of dependencies.

## Prerequisites:
1. Python 3.12 must be installed in order to run.
2. Kivy must be installed to run the UI.

## How to Run Guide:
Follow these steps to run the face verification app successfully:
1. Install Dependencies: Ensure that you have all the required dependencies installed. Run the following commands in a notebook cell:
```
!pip install opencv-python
!pip install matplotlib
!pip install tensorflow
```

## Contribution:
Contributions to the Face Verification App project are welcome. To contribute:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them.
- Push your changes to your fork.
- Submit a pull request to the main repository.

Your input is valuable to us. Feel free to contribute to the project. Thank you for exploring our Project.

## Acknowledgement:
- I acknowledge the paper [Siamese Neural Networks for One-shot Image Recognition](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf) by Gregory Koch, Richard Zemel, and Ruslan Salakhutdinov, which served as the inspiration for the Siamese neural network architecture implemented in this project.