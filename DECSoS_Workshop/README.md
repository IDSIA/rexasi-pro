# safe_roadcrossing_aw
This is the repository for Safe Road Crossing Decision for Autonomous Wheelchairs

The dataset can be find on HuggingFace:
- https://huggingface.co/datasets/carlogrigioni/safe-road-crossing-aw-dataset

## Demo
![gif](animation.gif)

## Paper
#### Safe Road-Crossing by Autonomous Wheelchairs: a Novel Dataset and its Experimental Evaluation
Carlo Grigioni, Franca Corradini, Alessandro Antonucci, Jerome Guzzi and Francesco Flammini

ArXiv: https://arxiv.org/abs/2403.08984

## Code
Scripts are set to be executed in the following order, after downloading the experiment files from HuggingFace:
### `bbox_pipeline.ipynb`
Extracts frames from mp4 videos, applies adverse weather filters and uses YOLO to detect robomaters. Then computes bounding boxes appering width in pixels and distance between camera and approaching robomaster.
### `focal_length_tuning.ipynb`
Finds the best focal length parameter to use for distance calculation from traingle similarity by comparing distances with ground truth distance from the motion tracker.
### `exp1-distance-fusion.ipynb`
Takes as input raw `.csv` files of experiment 1 for motion tracker, range sensors, object detection bounding boxes. Performs preprocessing by removing outliers, applies smoothing. Computes speed and acceleration for all sensors. Defines danger function. Merges data and resamples them at 100 Hz. Information fusion is done at the level of distances, then calculates speeds and accelerations. Then compares danger function from fusion with danger function evaluated on motion tracker data.
### `exp1-weighted-fusion.ipynb`
Takes as input raw `.csv` files of experiment 1 for motion tracker, range sensors, object detection bounding boxes. Performs the same steps of `exp1-distance-fusion.ipynb`. Evaluates the same danger function for for motion tracker, range sensors, object detection from wheelchair camera frames, and object detection from drone camera frames. Fusion is then performed by applying weighted average of individual sensors danger function. The Weighted average of danger function is compared with danger function evaluated on motion tracker data.
### `exp1-voting.ipynb`
Takes as input raw `.csv` files of experiment 1 for motion tracker, range sensors, object detection bounding boxes. Performs the same steps of `exp1-distance-fusion.ipynb`. Evaluates the same danger function for for motion tracker, range sensors, object detection from wheelchair camera frames, and object detection from drone camera frames. Applies the same decision threshold on danger functions. Fusion is then performed by averaging individual binary decisions from sensors. It is then compared by binary metrics to with decisions evaluated on motion tracker data.
### `fusion.ipynb`
Takes as input preprocessed and sincronized data for experiment 1 from `pre_fusion_data.csv`. Defines the danger function.
Applies distance fusion as in `exp1-distance-fusion.ipynb`. Defines an additional `decision` loop to make binary decisions that account for the last $n$ evaluations and make binary decisions more robust.
Applies danger function fusion as in `exp1-weighted-fusion.ipynb`.
Applies voting fusion as in `exp1-voting.ipynb`. Produces metrics as RMSE, accuracy, precision and recall.
## Additional data
### `pre_fusion_data.csv`
| timestamp | distance_wheelchair | speed_wheelchair | acceleration_wheelchair | distance_tracker | speed_tracker | acceleration_tracker | danger_tracker | distance_drone | speed_drone | acceleration_drone | distance_range | speed_range | acceleration_range | wheelchair_data |drone_data | tracker_data | range_data |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| timestamp | distance_wheelchair | speed_wheelchair | acceleration_wheelchair | distance_tracker | speed_tracker | acceleration_tracker | danger_tracker | distance_drone | speed_drone | acceleration_drone | distance_range | speed_range | acceleration_range | wheelchair_data |drone_data | tracker_data | range_data |

## Acknowledgments
This work was supported by the Swiss State Secretariat for Education,
Research and lnnovation (SERI). The project has been selected within the
European Union’s Horizon Europe research and innovation programme under grant
agreement: HORIZON-CL4-2021-HUMAN-01-01. Views and opinions expressed are
however those of the authors only and do not necessarily reflect those of the funding
agencies, which cannot be held responsible for them.