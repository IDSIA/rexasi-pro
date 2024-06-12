# Experimental Evaluation of Road-Crossing Decisions by Autonomous Wheelchairs against Environmental Factors

This is the repository for Experimental Evaluation of Road-Crossing Decisions by Autonomous Wheelchairs against Environmental Factors

The dataset can be find on HuggingFace:
- https://huggingface.co/datasets/carlogrigioni/safe-road-crossing-aw-dataset


## Paper
#### Experimental Evaluation of Road-Crossing Decisions by Autonomous Wheelchairs against Environmental Factors
Franca Corradini, Carlo Grigioni, Alessandro Antonucci, Jerome Guzzi and Francesco Flammini

## Code
Scripts are set to be executed in the following order, after downloading the experiment files from HuggingFace:

### fine_tune.py
Performs fine-tuning of YOLO version 8 nano from Ultralytics, for 10 epochs. Data should be downloaded from https://universe.roboflow.com/godwyll-aikins/robomaster-i5ydd

### auto_augment.py
Applies environmental filters to frames. Filters are implemented in the Automold library, for code and documentation: https://github.com/UjjwalSaxena/Automold--Road-Augmentation-Library/tree/master. Filters used are: fog (3 levels), rain (3 levels), bright (4 levels), dark (4 levels)

### yolo_v5.py
Detects objects in frames with YOLO version 5 small with weights as trained on the COCO dataset. Widths of bounding boxes are saved in csv files.

### yolo_v8.py
Detects objects in frames with YOLO version 8 nano with weights as fine-tuned in fine_tune.py. Widths of bounding boxes are saved in csv files.

### unify_dataframe.ipynb
Collects dataframes of widths of bounding boxes, which were saved filter by filter in a unique dataframe for the camera, the model and the experiment.

### missingness_eval.ipynb
Computes, in a restricted time interval, how many bounding box detections are missing for each type of filter, and makes a summary table, also divided by scene A and scene B.

### precision_eval.ipynb
Computes, in a restricted time interval, and only for frames in which an obstacle was detected, the measurment error of distance for each model and filter.
