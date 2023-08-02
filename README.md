# Intelligent Video Surveillance System

This project is an Intelligent Video Surveillance System that uses a custom database created from various videos downloaded from the internet. The system is trained on a dataset consisting of normal events captured in different locations, such as malls and streets. The trained model aims to detect abnormal events in real-time video streams.

## Table of Contents

1. [Project Name](#project-name)
2. [Table of Contents](#table-of-contents)
3. [Project Demo](#project-demo)
4. [Badges](#badges)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Configuration](#configuration)
8. [Contributing](#contributing)
9. [License](#license)
10. [Acknowledgments](#acknowledgments)
11. [Documentation](#documentation)

## Project Demo
### Result Demo
A demo video showcasing the Intelligent Video Surveillance System in action can be found at 
![Demo Video](result.mp4).
### FrontEnd 
![1](frontend1.png)
![1](frontend1.png)

## Badges

[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)

## Installation

To run this project, you need to have the following libraries installed:

- OpenCV (cv2)
- NumPy
- Keras
- Imutils

You can install the required libraries using pip:

```bash
pip install opencv-python
pip install numpy
pip install keras
pip install imutils
```

## Usage

The code uses a pre-trained neural network model (`saved_model.h5`) to detect abnormal events in video streams. The main logic of the code is as follows:

1. Load the pre-trained neural network model using Keras.
2. Read video frames from the specified video file.
3. Process each frame to extract features for anomaly detection.
4. Calculate the mean squared loss (MSE) between the original frame and the reconstructed frame obtained from the model.
5. Temporal smoothing: Apply a smoothing factor to the loss values to reduce noise.
6. Dynamically adjust the threshold for anomaly detection based on past scores.
7. If the smoothed loss exceeds the threshold, an abnormal event is detected.

The code continuously processes video frames and displays the video with detected abnormal events marked.
### frontend 
1. The frontend provides a simple user interface to upload a video file for analysis. Follow these steps to use the Intelligent Video Surveillance System frontend:
2. The frontend provides a simple user interface to upload a video file for analysis. Follow these steps to use the Intelligent Video Surveillance System frontend:
3. Click on the "Choose File" button to select a video file (supported formats: .mp4 and .avi).
4. Click on the "Choose File" button to select a video file (supported formats: .mp4 and .avi).
5. The video will be played in the video player, and the analysis result overlay will be displayed.
6. The result overlay will indicate whether the video contains an "Abnormal Event Detected" or "No Abnormal Event Detected."

   
## Configuration

1. Replace the `path` variable with the path to the video file you want to analyze.

2. Fine-tune the `threshold`, `alpha`, and any other parameters to optimize the system's performance based on your specific use case.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, feel free to open a pull request or create an issue on the GitHub repository.

## License

This project is open-source and licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code, but please provide proper attribution to the original creator, Harsh Gupta (Desparete Enuf).

## Acknowledgments

The Intelligent Video Surveillance System is a project created by Harsh Gupta (Desparete Enuf) to demonstrate anomaly detection in video streams using neural networks and computer vision techniques. The project utilizes a custom database of normal events in various locations to train the model.

## Documentation

To use the Intelligent Video Surveillance System, follow these steps:

1. Install the required libraries as mentioned in the [Installation](#installation) section.

2. Prepare your video file to be analyzed and update the `path` variable in the code with the correct file path.

3. Fine-tune the threshold and other parameters based on your specific use case in the `threshold` and `alpha` variables.

4. Run the script in a Python environment.

The script will process the video frames, detect abnormal events, and display the video stream with any detected abnormal events marked. You can adjust the threshold and other parameters to achieve optimal anomaly detection performance for different scenarios.


