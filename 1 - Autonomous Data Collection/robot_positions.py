# each function represents a routine for the robot to perform on the workflow
# yumi gives positions in terms of 7 coordinates
# https://berkeleyautomation.github.io/yumipy/api/robot.html

from yumipy import YuMiRobot, YuMiState
import time



def reset_robot_pos():
    global y
    y = YuMiRobot()
    y.left.set_speed(YuMiRobot.get_v(150))
    y.left.goto_state(YuMiState([-146.06,-122.78,30.53,200.91,126.87,-115.28,54.45]))
    return

def robot_routine():
    global y
    y = YuMiRobot()

    # left bringtoexchange
    y.left.set_speed(YuMiRobot.get_v(150))
    y.left.goto_state(YuMiState([-109.57,-94.07,55.51,159.66,119.65,-92.64,105.22]))

    # l2r exchange
    y.right.set_speed(YuMiRobot.get_v(150))
    y.right.goto_state(YuMiState([50.02,-125.72,17.08,-36.65,69.57,125.83,-86.33]))
    y.right.goto_state(YuMiState([56.01,-125.72,16.01,-44.6,60.94,125.92,-86.06]))
    y.right.close_gripper()
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.open_gripper()
    y.left.goto_state(YuMiState([-62.89,-83.1,75.63,148.78,73.69,-68.21,90.46]))

    y.left.goto_state(YuMiState([-99.14,-77.31,16.63,148.97,-32.33,-75.22,126.03]))
    y.left.close_gripper()
    y.right.open_gripper()
    y.right.set_speed(YuMiRobot.get_v(50))
    y.right.goto_state(YuMiState([50.15,-125.72,10.33,-42.78,75.2,124.36,-79.88]))
    y.right.goto_state(YuMiState([41.8,-125.72,28.3,-43.55,83.6,138.13,-79.14]))
    y.right.goto_state(YuMiState([50.93,-125.72,24.99,-46.83,66.86,132.88,-85.73]))
    y.right.close_gripper()
    y.left.open_gripper()
    y.left.goto_state(YuMiState([-93.43,-66.78,6.56,170.65,-45.14,-101.65,124.74]))

    # rotate
    y.right.set_speed(YuMiRobot.get_v(150))
    y.right.goto_state(YuMiState([40.25,-125.72,5.05,29.13,54.94,98.69,-83.91]))
    y.right.set_speed(YuMiRobot.get_v(700))
    y.right.goto_state(YuMiState([40.2,-125.72,1.56,28.06,56.78,8.73,-83.92]))
    y.right.set_speed(YuMiRobot.get_v(150))
    time.sleep(5)
    return
def robot_return():
    global y
    y = YuMiRobot()

    # right bringtoexchange
    y.right.set_speed(YuMiRobot.get_v(150))
    y.right.goto_state(YuMiState([40.2,-125.72,1.56,28.06,56.78,8.73,-83.92]))
    y.right.goto_state(YuMiState([62.94,-125.72,28.97,-53.41,52.46,139.75,-90.23]))

    # r2l exchange
    y.right.set_speed(YuMiRobot.get_v(50))
    y.left.set_speed(YuMiRobot.get_v(50))
    y.left.close_gripper()
    y.right.open_gripper()
    y.right.goto_state(YuMiState([66.89,-125.72,18.87,-48.45,53.9,133.87,-89.47]))
    y.right.goto_state(YuMiState([70.87,-125.72,15.08,-42.22,61.61,125.84,-88.16]))

    y.right.close_gripper()
    y.left.open_gripper()

    y.left.goto_state(YuMiState([-90.36,-66.75,-14.03,178.46,-64.3,-102.65,122.99]))
    y.left.goto_state(YuMiState([-40.55,-46.81,63.39,177.22,0.51,-115.83,84.29]))
    y.left.goto_state(YuMiState([-55.96,-54.09,71.86,162.38,3.12,-94.54,91.82]))
    y.left.goto_state(YuMiState([-96.38,-54.09,72.25,130.25,104.35,-106.67,93.11]))
    y.left.goto_state(YuMiState([-96.38,-54.09,64.62,146.14,96.75,-97.61,107.57]))
    y.left.close_gripper()
    y.right.open_gripper()
    y.right.goto_state(YuMiState([45.98,-125.72,12.36,-37.03,74.41,120.53,-88.5]))

    # left arm central closed
    y.left.set_speed(YuMiRobot.get_v(50))
    y.left.goto_state(YuMiState([-96.38, -54.09, 64.62, 146.14, 96.75, -97.61, 107.57]))
    y.left.goto_state(YuMiState([-131.55,-54.10,12.1,116.71,97.19,-77.68,95.3]))
    return
def pick_small_vial_1():
    global y
    y = YuMiRobot()

    y.left.set_speed(YuMiRobot.get_v(150))
    y.left.goto_state(YuMiState([-135.31,-125.95,25.11,192.85,113.64,-40.88,62.96]))
    y.left.goto_state(YuMiState([-135.28,-125.95,14.76,192.36,104.76,-37.37,60.46]))
    y.left.close_gripper()
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-135.47,-124.36,17.01,190.06,109.07,-34.65,60.87]))
    y.left.goto_state(YuMiState([-135.49,-124.36,19.04,191.52,110.72,-34.64,62.39]))
    y.left.goto_state(YuMiState([-135.62,-124.35,30.04,191.13,119.18,-34.64,63.66]))
    y.left.goto_state(YuMiState([-137.75,-93.78,37.06,153.87,137.68,-83.6,78.18]))
    return
def putback_small_vial_1():
    global y
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-131.55,-54.1,17.66,121.9,88.45,-83.84,106.4]))
    y.left.goto_state(YuMiState([-138.24,-54.1,7.33,125.61,75.5,-86.9,122.9]))
    y.left.goto_state(YuMiState([-142.37,-54.12,3.72,124.21,75.05,-86.17,127.88]))
    y.left.goto_state(YuMiState([-144.07,-54.33,1.56,123.36,74.27,-87.74,130.46]))
    y.left.open_gripper()
    y.left.goto_state(YuMiState([-144.06,-54.33,1.56,123.31,74.69,-106.84,130.51]))
    y.left.goto_state(YuMiState([-144.06,-54.32,5.72,121.86,87.55,-101.21,124.35]))
    return
def pick_small_vial_2():
    global y
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-134.21,-126.81,22.6,196.64,112.42,-38.59,61.87]))
    y.left.goto_state(YuMiState([-134.2,-126.81,20.81,198.23,111.55,-13.68,62.09]))
    y.left.goto_state(YuMiState([-134.13,-126.81,16.96,196.06,106.8,-7.16,60.11]))
    y.left.close_gripper()
    y.left.goto_state(YuMiState([-134.14,-126.81,18.89,196.14,108.97,-7.19,60.58]))
    y.left.goto_state(YuMiState([-134.14,-126.81,21.87,196.86,111.6,-7.16,61.36]))
    y.left.goto_state(YuMiState([-137.84,-129.56,35.4,201.57,124.1,-11.29,59.32]))
    return
def putback_small_vial_2():
    global y
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-131.55,-54.1,17.66,121.9,88.45,-83.84,106.4]))
    y.left.goto_state(YuMiState([-131.51,-54.1,17.09,121.84,93.51,-71.56,107.29]))
    y.left.goto_state(YuMiState([-129.06,-54.1,18.81,125.51,89.56,-82.85,108.4]))
    y.left.goto_state(YuMiState([-137.07,-54.13,7.99,125.96,80.55,-82.23,122.28]))
    y.left.goto_state(YuMiState([-137.06,-54.13,5.81,126.2,74.43,-82.11,124.98]))
    y.left.open_gripper()
    y.left.goto_state(YuMiState([-132.28,-54.06,15.14,126.68,84.99,-73.48,113.71]))
    return
def pick_small_vial_3():
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-138,-122.8,12.79,192.76,103.56,-132.3,61.95]))
    y.left.goto_state(YuMiState([-136.86,-119.74,8.4,190.6,100.27,-133.73,64.48]))
    y.left.close_gripper()
    y.left.goto_state(YuMiState([-136.86,-119.74,10.34,190.74,102.78,-133.72,64.89]))
    y.left.goto_state(YuMiState([-136.87,-119.74,13.07,191.09,104.96,-133.68,65.24]))
    y.left.goto_state(YuMiState([-138.17,-119.74,23.49,193.27,116.27,-133.21,67.56]))
    y.left.goto_state(YuMiState([-122.19,-103.96,57.49,174.32,115.2,-133.22,81.44]))
    return
def putback_small_vial_3():
    global y
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-134.3,-56.05,13.53,125.48,86.68,-186.27,107.56]))
    y.left.goto_state(YuMiState([-142.99,-56.24,0.12,125.42,76.03,-188.61,123.78]))
    y.left.goto_state(YuMiState([-148.05,-55.55,-3.66,127.02,70.5,-187.67,133.79]))
    y.left.open_gripper()
    y.left.goto_state(YuMiState([-138.06,-55.43,10.26,127.2,82.95,-182.51,114.09]))
    return
def pick_small_vial_4():
    global y
    y.left.set_speed(YuMiRobot.get_v(50))
    y.left.goto_state(YuMiState([-134.3,-56.05,13.53,125.48,86.68,-186.27,107.56]))
    y.left.goto_state(YuMiState([-129.64,-122.8,20.43,189.74,104.84,-130.13,61.65]))
    y.left.goto_state(YuMiState([-129.64,-122.79,18.48,186.81,103.99,-130.96,60.18]))
    y.left.close_gripper()
    y.left.set_speed(YuMiRobot.get_v(25))

    y.left.goto_state(YuMiState([-129.64,-122.78,21.43,187.88,107.01,-130.96,61.15]))
    y.left.goto_state(YuMiState([-129.64,-122.76,26.58,182.61,111.17,-130.97,57.63]))
    y.left.goto_state(YuMiState([-135.01,-122.66,37.39,183.84,127.37,-126.49,54.92]))
    return
def putback_small_vial_4():
    global y
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-131.55,-54.1,17.66,121.9,88.45,-83.84,106.4]))
    y.left.goto_state(YuMiState([-121.07,-54.11,22.95,119.64,90.34,-180.42,95.99]))
    y.left.goto_state(YuMiState([-128.07,-54.11,8.81,124.11,74.64,-180.43,113.2]))
    y.left.goto_state(YuMiState([-128.1,-57.01,6.52,127.79,73.93,-179.15,113.36]))

    y.left.open_gripper()
    y.left.goto_state(YuMiState([-122.27,-56.99,17.81,125.55,85.31,-178.97,101.32]))
    return
def pick_small_vial_5():
    global y
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-146.06,-122.78,30.53,200.91,126.87,-115.28,54.45]))
    y.left.goto_state(YuMiState([-140.82,-122.76,10.64,191.58,100.36,-127.39,55.31]))
    y.left.goto_state(YuMiState([-142.76,-119.33,3.81,188.47,102.73,-126.84,54.46]))
    y.left.close_gripper()
    y.left.goto_state(YuMiState([-142.76,-119.33,8.32,188.72,106.85,-126.86,55]))
    y.left.goto_state(YuMiState([-142.82,-119.33,25.44,187.78,120.94,-126.86,56.31]))
    return
def putback_small_vial_5():
    global y
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-134.86,-63.88,11.53,128.64,97.65,-167.81,97.98]))
    y.left.goto_state(YuMiState([-137.93,-63.88,0.8,128.62,90.09,-170.02,104.95]))
    y.left.goto_state(YuMiState([-142.1,-64.86,-9.57,128.24,81.1,-174.6,114.23]))
    y.left.open_gripper()
    y.left.goto_state(YuMiState([-138.25,-56.84,6.35,119.19,90.46,-177.73,104.96]))
    return
def pick_small_vial_6():
    global y
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-146.06,-122.78,30.53,200.91,126.87,-115.28,54.45]))
    y.left.goto_state(YuMiState([-133.92,-121.13,18.81,190.04,108.61,-124.62,57.11]))
    y.left.goto_state(YuMiState([-133.91,-121.11,13.89,186.22,104.34,-126.51,54.91]))
    y.left.close_gripper()
    y.left.goto_state(YuMiState([-133.92,-121.11,18.94,186.23,109,-126.49,55.1]))
    y.left.goto_state(YuMiState([-132.94,-116.21,29.04,178.88,119.94,-127.36,56.65]))
    return
def putback_small_vial_6():
    global y
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-131.55,-54.1,17.66,121.9,88.45,-83.84,106.4]))
    y.left.goto_state(YuMiState([-125.92,-54.17,12.07,117.86,88.19,-177.39,98.84]))
    y.left.goto_state(YuMiState([-131.49,-54.24,1.81,121,74.21,-177.77,114.43]))
    y.left.goto_state(YuMiState([-134.45,-54.24,-2.08,119.81,71.72,-177.77,119]))
    y.left.open_gripper()
    y.left.goto_state(YuMiState([-130.47,-33.88,17.38,105.69,69.99,-181.38,115.75]))
    return
def pick_small_vial_7():
    global y
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-146.06,-122.78,30.53,200.91,126.87,-115.28,54.45]))
    y.left.goto_state(YuMiState([-142.87,-116.17,6.03,186.94,104.73,-130.97,55.84]))
    y.left.goto_state(YuMiState([-141.03,-112.97,-0.08,182.61,99.2,-132.24,58.75]))
    y.left.close_gripper()
    y.left.goto_state(YuMiState([-141.04,-112.97,3.52,182.91,102.92,-132.23,59.03]))
    y.left.goto_state(YuMiState([-144.94,-112.97,20.58,182.85,122.8,-133.72,55.28]))
    return
def putback_small_vial_7():
    global y
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-131.55,-54.1,17.66,121.9,88.45,-83.84,106.4]))
    y.left.goto_state(YuMiState([-137.62,-50.8,9.1,117.81,88.74,-178.3,104.3]))
    y.left.goto_state(YuMiState([-143.17,-53.65,-2.28,121.81,79.34,-178.27,117.15]))
    y.left.goto_state(YuMiState([-146.48,-55.5,-12.51,116.49,69.31,-173.29,125.23]))
    y.left.goto_state(YuMiState([-146.5,-58.39,-15.63,118.14,68.82,-170.89,124.52]))
    y.left.open_gripper()
    y.left.goto_state(YuMiState([-138.82,-48.75,7.33,114.25,83.4,-173.44,107.27]))
    return
def pick_small_vial_8():
    global y
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-146.06,-122.78,30.53,200.91,126.87,-115.28,54.45]))
    y.left.goto_state(YuMiState([-144.18,-126.28,16.12,196.42,107,-109.7,41.33]))
    y.left.goto_state(YuMiState([-144.18,-126.26,11.04,195.41,101.2,-110.77,39.45]))
    y.left.close_gripper()
    y.left.goto_state(YuMiState([-144.18,-126.26,15.85,195.29,105.53,-109.72,40.15]))
    y.left.goto_state(YuMiState([-151.69,-126.16,27.42,204.21,121.03,-111.59,39.25]))
    return
def putback_small_vial_8():
    global y
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-131.55,-54.1,17.66,121.9,88.45,-83.84,106.4]))
    y.left.goto_state(YuMiState([-125.82,-54.1,10.31,118.7,88.35,-166.15,96.48]))
    y.left.goto_state(YuMiState([-130.02,-54.1,1.17,117.27,81.39,-170.79,104.9]))
    y.left.goto_state(YuMiState([-133.28,-57.49,-5.87,120.48,75.23,-170.96,111.96]))
    y.left.goto_state(YuMiState([-132.78,-59.25,-8,120.86,73.13,-163.69,111.28]))
    y.left.open_gripper()
    y.left.goto_state(YuMiState([-122.67,-59.23,17.93,126.45,97.01,-166.58,88.27]))
    return
def pick_small_vial_9():
    global y
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-146.06,-122.78,30.53,200.91,126.87,-115.28,54.45]))
    y.left.goto_state(YuMiState([-147.61,-117.23,1.84,191.01,102.08,-123.77,48.55]))
    y.left.goto_state(YuMiState([-149.16,-115.18,-5.68,190.01,100.8,-122.9,46.93]))
    y.left.close_gripper()
    y.left.goto_state(YuMiState([-149.16,-115.18,0.36,189.18,106.72,-125.98,46.95]))
    y.left.goto_state(YuMiState([-156.41,-115.12,12.19,195.13,123.79,-131.38,44.83]))
    return
def putback_small_vial_9():
    global y
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-131.55,-54.1,17.66,121.9,88.45,-83.84,106.4]))
    y.left.goto_state(YuMiState([-140.78,-54.09,-1.87,113.38,91.92,-167.04,101.61]))
    y.left.goto_state(YuMiState([-145.96,-54.12,-6.01,114.88,86.08,-164.7,110.78]))
    y.left.goto_state(YuMiState([-148.81,-56.36,-17.89,112.9,74.53,-159.23,122.25]))
    y.left.goto_state(YuMiState([-149.79,-58.44,-21.67,114.25,68.9,-158.85,126.19]))
    y.left.open_gripper()
    y.left.goto_state(YuMiState([-145.44,-49.42,-3.77,113.83,79.14,-170.49,116.75]))
    return
def pick_small_vial_10():
    global y
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-146.06,-122.78,30.53,200.91,126.87,-115.28,54.45]))
    y.left.goto_state(YuMiState([-146.06,-122.73,8.89,198.23,103.05,-115.35,40.57]))
    y.left.goto_state(YuMiState([-146.06,-122.75,5.87,196.89,100.51,-115.23,39.62]))
    y.left.close_gripper()
    y.left.goto_state(YuMiState([-146.04,-122.75,9.26,195.83,104.1,-115.23,39.58]))
    y.left.goto_state(YuMiState([-143.14,-117.5,24.91,189.77,122.33,-112.52,46.83]))
    return
def putback_small_vial_10(): 
    global y
    y.left.set_speed(YuMiRobot.get_v(25))
    y.left.goto_state(YuMiState([-131.55,-54.1,17.66,121.9,88.45,-83.84,106.4]))
    y.left.goto_state(YuMiState([-123.67,-54.1,18.31,119.93,95.06,-170.26,88.82]))
    y.left.goto_state(YuMiState([-129.81,-54.1,0.88,116.76,83.14,-166.2,101.33]))
    y.left.goto_state(YuMiState([-128.52,-54.1,1.57,116.09,82.54,-163.92,100]))
    y.left.goto_state(YuMiState([-132.36,-54.1,-5.07,117.06,73.71,-163.42,109.86]))
    y.left.goto_state(YuMiState([-136.19,-54.13,-10.12,114.47,72.42,-163.38,114.82]))
    y.left.goto_state(YuMiState([-136.18,-54.13,-10.5,115.18,69.23,-163.38,116.98]))
    y.left.open_gripper()
    y.left.goto_state(YuMiState([-125.27,-49.4,11.49,117.41,85.02,-173.66,98.14]))
    return

if __name__ == '__main__':
    global y
    y = YuMiRobot()
