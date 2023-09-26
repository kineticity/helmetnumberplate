
Motorcycle Helmet and License plate detection - v6 DatasetV6
==============================

This dataset was exported via roboflow.com on March 28, 2023 at 5:50 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 3544 images.
Helmet are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise, upside-down
* Random rotation of between -5 and +5 degrees
* Random exposure adjustment of between -25 and +25 percent
* Random Gaussian blur of between 0 and 1 pixels
* Salt and pepper noise was applied to 1 percent of pixels

The following transformations were applied to the bounding boxes of each image:
* 50% probability of horizontal flip
* 50% probability of vertical flip
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise, upside-down
* Random brigthness adjustment of between -25 and +25 percent
* Random exposure adjustment of between -25 and +25 percent
* Random Gaussian blur of between 0 and 1 pixels
* Salt and pepper noise was applied to 1 percent of pixels


