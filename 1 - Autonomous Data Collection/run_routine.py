from class_camera import *
from robot_positions import *
from yumipy import YuMiRobot, YuMiState
import time

if __name__ == "__main__":
    global y
    
    vial_size_input = int(input("Vial size = "))

    if vial_size_input == int(8):
        for i in range(1,11):
            reset_robot_pos()
            pick_small_vial_function = str("pick_small_vial_"+str(i)+"()")
            eval(pick_small_vial_function)
            robot_routine()
            start_small_vial_recording('video_position_trySL_'+str(i)+'.avi')
            time.sleep(5)
            stop_small_vial_video('video_position_trySL_'+str(i)+'.avi')
            robot_return()
            putback_small_vial_function = str("putback_small_vial_"+str(i)+"()")
            eval(putback_small_vial_function)
    
    elif vial_size_input == int(20):
        for i in range(1,9):
            reset_robot_pos_big()
            pick_big_vial_function = str("pick_big_vial_"+str(i)+"()")
            eval(pick_big_vial_function)
            robot_routine_big()
            start_big_vial_recording('video_position_trySL_'+str(i)+'.avi')
            time.sleep(5)
            stop_big_vial_video('video_position_trySL_'+str(i)+'.avi')
            robot_return_big()
            putback_big_vial_function = str("putback_big_vial_"+str(i)+"()")
            eval(putback_big_vial_function)


    else:
        print('Please use samples in vial size 8 or 20ml')
