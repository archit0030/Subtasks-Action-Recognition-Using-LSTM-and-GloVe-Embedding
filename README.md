# Subtasks-Action-Recognition-Using-LSTM-and-GloVe-Embedding

# Task to Sub-Action Sequence Prediction using LSTM

This repository contains code for predicting sequences of sub-actions from natural language tasks using a neural network model. The goal is to convert high-level task descriptions into a sequence of low-level actions (sub-actions) that can be used to control a robotic system.

## Table of Contents
- [Introduction](#introduction)
- [Model Overview](#model-overview)
- [Dataset](#dataset)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Training](#training)
- [Prediction](#prediction)
- [Results](#results)
- [License](#license)

## Introduction
This project aims to convert natural language descriptions of tasks into sequences of sub-actions. The model uses pre-trained GloVe word embeddings to represent the tasks and an LSTM-based neural network to predict the sub-actions.

## Model Overview
- **Word Embeddings:** Pre-trained GloVe embeddings are used to convert words into numerical vectors.
- **LSTM Model:** A sequential neural network with an LSTM layer is used to process the task embeddings and predict sub-action sequences.
- **Output:** The model outputs a sequence of sub-actions corresponding to the given task.

## Dataset
The dataset consists of pairs of tasks and their corresponding sequences of sub-actions. Tasks are high-level descriptions of actions, and sub-actions are atomic steps needed to perform the task.

## Dependencies
- Python 3.9 or greater
- TensorFlow 2.15.0 or greater
- NumPy
- scikit-learn

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/task-subaction-prediction.git
    cd task-subaction-prediction
    ```

2. Download the GloVe embeddings and place the `glove.6B.100d.txt` file in the root directory.

3. Run the script:
    ```bash
    python task_to_subaction.py
    ```

## Training
The model is trained using the task embeddings as input and the sub-action sequences as output. The training process can be customized by modifying the parameters in the script.

## Prediction
After training, you can use the model to predict sub-actions for new tasks. Simply input a new task description, and the model will output the corresponding sequence of sub-actions.

## Results
The model can successfully predict sequences of sub-actions for tasks similar to those in the training set. The predictions can be used to guide robotic systems in performing complex tasks.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
