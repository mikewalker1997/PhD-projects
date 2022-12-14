Scripts for robotic workflow which collects videos of liquids in motion. These videos are used for training a 3D-CNN model to estimate their properties.

The process: robot picks a sample, rotates in front of a camera for recording, returns sample to rack, then repeats.

robot_positions.py - Coordinates for the robotic arm movements (via Yumipy)
record_vids_classes.py - Camera classes for recording videos, each class corresponds to the size of vials in routine
run_routine.py - script for running the routine
