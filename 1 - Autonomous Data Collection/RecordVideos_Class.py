import cv2
import time
import threading

class SmallVialRecords():

    # Video class based on openCV
    def __init__(self, video_filename):

        self.open = True
        self.capture_duration = 5
        self.device_index, self.fps, self.fourcc, self.frameSize = 0, 27, "MJPG", (640, 480)
        self.video_filename = video_filename
        self.video_cap, self.video_writer = cv2.VideoCapture(self.device_index), cv2.VideoWriter_fourcc(*self.fourcc)
        self.video_out = cv2.VideoWriter(self.video_filename, self.video_writer, self.fps, self.frameSize)
        self.frame_counts = 1
        self.start_time = time.time()

    # Video starts being recorded
    def record(self):

        while int(time.time() - self.start_time) < self.capture_duration:
            ret, video_frame = self.video_cap.read()
            if ret:
                self.video_out.write(video_frame)
                self.frame_counts += 1
            else:
                break
        # Finishes the video recording therefore the thread too

    def stop(self):

        if self.open:

            self.open = False
            self.video_out.release()
            self.video_cap.release()
            cv2.destroyAllWindows()
        else:
            pass

    # Launches the video recording function using a thread
    def start(self):
        video_thread = threading.Thread(target=self.record)
        video_thread.start()


def start_small_vial_recording(video_filename):
    global video_thread

    video_thread = SmallVialRecords(video_filename)
    video_thread.start()

    return video_filename

def stop_small_vial_video(video_filename):
    global video_thread
    video_thread.stop()

#def record_videos_small():
#   for i in range(1,6):

#        start_small_vial_recording('video_position_tryBBNG_'+str(i)+'.avi')
#        time.sleep(5)
#        stop_small_vial_video('video_position_tryBBNG_'+str(i)+'.avi')

class BigVialRecords():

    # Video class based on openCV
    def __init__(self, video_filename):

        self.open = True
        self.capture_duration = 20
        self.device_index, self.fps, self.fourcc, self.frameSize = 0, 27, "MJPG", (640, 480)
        self.video_filename = video_filename
        self.video_cap, self.video_writer = cv2.VideoCapture(self.device_index), cv2.VideoWriter_fourcc(*self.fourcc)
        self.video_out = cv2.VideoWriter(self.video_filename, self.video_writer, self.fps, self.frameSize)
        self.frame_counts = 1
        self.start_time = time.time()

    # Video starts being recorded
    def record(self):

        while int(time.time() - self.start_time) < self.capture_duration:
            ret, video_frame = self.video_cap.read()
            if ret:
                self.video_out.write(video_frame)
                self.frame_counts += 1
            else:
                break
        # Finishes the video recording therefore the thread too

    def stop(self):

        if self.open:

            self.open = False
            self.video_out.release()
            self.video_cap.release()
            cv2.destroyAllWindows()
        else:
            pass

    # Launches the video recording function using a thread
    def start(self):
        video_thread = threading.Thread(target=self.record)
        video_thread.start()


def start_big_vial_recording(video_filename):
    global video_thread

    video_thread = BigVialRecords(video_filename)
    video_thread.start()

    return video_filename

def stop_big_vial_video(video_filename):
    global video_thread
    video_thread.stop()

#def record_videos_big():
#   for i in range(1,6):

#        start_big_vial_recording('video_position_tryBBNG_'+str(i)+'.avi')
#        time.sleep(20)
#       stop_big_vial_video('video_position_tryBBNG_'+str(i)+'.avi')