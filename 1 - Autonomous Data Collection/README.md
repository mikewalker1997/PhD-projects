This is the code for collecting videos of liquid samples to feed into the 3D-CNN models

The process: robot picks a sample, rotates in front of a camera for recording, returns sample to rack, then repeats.

robot_positions.py - Coordinates for the robotic arm movements (via Yumipy)
record_vids_classes.py - Camera classes for recording videos, each class corresponds to the size of vials in routine
run_routine.py - script for running the routine
