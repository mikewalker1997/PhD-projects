import cv2
import time
import threading

class SmallVialRecords():

    def __init__(self, video_filename):

        self.open = True
        self.capture_duration = 5
        self.device_index, self.fps, self.fourcc, self.frameSize = 0, 27, "MJPG", (640, 480)
        self.video_filename = video_filename
        self.video_cap, self.video_writer = cv2.VideoCapture(self.device_index), cv2.VideoWriter_fourcc(*self.fourcc)
        self.video_out = cv2.VideoWriter(self.video_filename, self.video_writer, self.fps, self.frameSize)
        self.frame_counts = 1
        self.start_time = time.time()

    def record(self):

        while int(time.time() - self.start_time) < self.capture_duration:
            ret, video_frame = self.video_cap.read()
            if ret:
                self.video_out.write(video_frame)
                self.frame_counts += 1
            else:
                break
  
    def stop(self):

        if self.open:

            self.open = False
            self.video_out.release()
            self.video_cap.release()
            cv2.destroyAllWindows()
        else:
            pass

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


class BigVialRecords():

    def __init__(self, video_filename):

        self.open = True
        self.capture_duration = 20
        self.device_index, self.fps, self.fourcc, self.frameSize = 0, 27, "MJPG", (640, 480)
        self.video_filename = video_filename
        self.video_cap, self.video_writer = cv2.VideoCapture(self.device_index), cv2.VideoWriter_fourcc(*self.fourcc)
        self.video_out = cv2.VideoWriter(self.video_filename, self.video_writer, self.fps, self.frameSize)
        self.frame_counts = 1
        self.start_time = time.time()

    def record(self):

        while int(time.time() - self.start_time) < self.capture_duration:
            ret, video_frame = self.video_cap.read()
            if ret:
                self.video_out.write(video_frame)
                self.frame_counts += 1
            else:
                break
       
    def stop(self):

        if self.open:

            self.open = False
            self.video_out.release()
            self.video_cap.release()
            cv2.destroyAllWindows()
        else:
            pass

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
