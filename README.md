# Gesture-detection-and-replication
## Table of contents
* [About the Project](https://github.com/Dhruv454000/Gesture-detection-and-replication/edit/develop/README.md#:~:text=Acknowledgements%20and%20Resources-,About%20the%20Project,-To%20detect%20and)
  * [Tech Stack](https://github.com/Dhruv454000/Gesture-detection-and-replication/edit/develop/README.md#:~:text=detecting%20different%20gestures.-,Tech%20Stack%3A-,-Technologies%20used%20for)
  * [File Structure](https://github.com/Dhruv454000/Gesture-detection-and-replication/edit/develop/README.md#:~:text=Google%20colab-,File%20Structure,-.%0A%E2%94%9C%E2%94%80%E2%94%80%20docs%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20Documentation%20files)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
* [Usage](#usage)
 * [Results and Demo](#results-and-demo) 
* [Future Work](#future-work)
* [Troubleshooting](#troubleshooting)
* [Contributors](#contributors)
* [Acknowledgements and Resources](#acknowledgements-and-resources)
 
## About the Project
To detect and recognise basic hand gestures and imitate them using a simulation of a robotic hand. Recognition of gestures can be done using various approaches like CNN (Convolutional Neural Network), feature engineering (such as binary thresholding, circle detection, etc.), and others. The simulation will be done using CoppeliaSim.In this project will be focusing on two methods. 1.CNN's(for more information see in project resources link below) 2.opencv(contours detection).


So as you can see in the image when **_4_** was detected then the arm that you see in right side window is oriented at some position.
similarly you can move the arm by detecting different gestures.

### Tech Stack:-
Technologies used for this project
* [Python](https://www.python.org/)
* [opencv](https://opencv.org/)
* [Numpy](https://numpy.org/doc/#)
* [Remote API python Coppeliasim](https://www.coppeliarobotics.com/helpFiles/en/remoteApiFunctionsPython.htm)
* [keras](https://keras.io/) (Optional)
* [Google colab](https://colab.research.google.com/)


### File Structure
    .
    ├── docs                    # Documentation files (alternatively `doc`)
    │   ├── report.pdf          # Project report
    │   └── results             # Folder containing screenshots, gifs, videos of results
    ├── MOODYLYSER2f.ipynb                  # Training program for the Model
    ├── Moodelld1_5de.h5                  # Pretrained Model with set weights
    ├── README.md
    ├── landmarks.py                  # Connects the model to a live videofeed via webcams

## _Getting started:-_
### Prerequisites
Install coppeliasim:   [https://coppeliarobotics.com/downloads](https://coppeliarobotics.com/downloads)

### Installation
_Clone the Repo_

Some project resources and links:-
All in one project resources
https://docs.google.com/document/d/1Ho3gW0fzOjTQDwivSkv8w53ms3cHyDvEvNnYnVq8qrg/edit

