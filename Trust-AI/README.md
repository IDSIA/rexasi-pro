#  Balancing Accuracy and Interpretability in Multi-Sensor Fusion through Dynamic Bayesian Networks

This is the official repository for the paper "Balancing Accuracy and Interpretability in Multi-Sensor Fusion through Dynamic Bayesian Networks" submitted at the "European Workshop on Trustworthy AI" (TRUST-AI 2025 - https://sites.google.com/view/trust-ai/home) at the "28th European Conference on Artificial Intelligence" (ECAI)

The dataset can be find on HuggingFace:
- https://huggingface.co/datasets/carlogrigioni/safe-road-crossing-aw-dataset


## Paper
#### Explainable Multi-Sensor Fusion by Dynamic Bayesian Networks
Franca Corradini, Carlo Grigioni, Alessandro Antonucci, Jerome Guzzi and Francesco Flammini

## Code

### xgb_CASE1.ipynb

Performs 7 fold LOOCV by training 7 eXtreme Gradient Boosting models models with 100 extimators and random seed 0 on original data. Then tests for original and augmented rain weak, rain strong and fog filters. Evaluates RMSE for each data fold.

### NN_CASE1.ipynb

Specifies a Deep Neural Network architecture and performs 7 fold LOOCV by training 7 same structure neural networks for 20 epochs and random seed 0 on original data. Then tests for original and augmented rain weak, rain strong and fog filters. Evaluates RMSE for each data fold.

### winkler_to_csv.py
Calculates the Winkler score for all prediction intervals.
The Winkler score is a metric used to evaluate the quality of a prediction interval by penalizing both the width of the interval and whether the true value lies outside it.
