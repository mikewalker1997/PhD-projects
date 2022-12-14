from class_camera import *
from robot_positions import *
from yumipy import YuMiRobot, YuMiState
import time

if __name__ == "__main__":
    global y
    
    # asks user to set vial size for routine
    vial_size_input = int(input("Vial size = "))

    # for 8ml vial routine, the robot picks a small vial from designated position (1 to 10) and records video as the samples are rotated
    if vial_size_input == int(8):
        for i in range(1,11):
            reset_robot_pos() # from robot_positions.py
            pick_small_vial_function = str("pick_small_vial_"+str(i)+"()")
            eval(pick_small_vial_function)
            robot_routine()
            start_small_vial_recording('small_vial_'+str(i)+'.avi') # records and saves video (from records_vids_classes.py)
            time.sleep(5)
            stop_small_vial_video('small_vial_'+str(i)+'.avi')
            robot_return()                                                    # robot returns sample to rack
            putback_small_vial_function = str("putback_small_vial_"+str(i)+"()")
            eval(putback_small_vial_function)
    
    elif vial_size_input == int(20):
        for i in range(1,9):
            reset_robot_pos_big()
            pick_big_vial_function = str("pick_big_vial_"+str(i)+"()")
            eval(pick_big_vial_function)
            robot_routine_big()
            start_big_vial_recording('big_vial_'+str(i)+'.avi')
            time.sleep(5)
            stop_big_vial_video('big_vial_trySL_'+str(i)+'.avi')
            robot_return_big()
            putback_big_vial_function = str("putback_big_vial_"+str(i)+"()")
            eval(putback_big_vial_function)


    else:
        print('Please use samples in vial size 8 or 20ml')
