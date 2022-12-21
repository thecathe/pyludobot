import datetime
from typing import Tuple
import pybullet as p
import time

physicsClient = p.connect(p.GUI)

frame_rate = 60
frame_len = 1.0/frame_rate

ns_ratio = 1000000000
ms_ratio = 1000


def frame_throttling(prev: int, start: int) -> int:
    global frame_rate
    global frame_len
    global ns_ratio
    global ms_ratio

    now = time.time_ns()
    time_diff = (now - prev)/ns_ratio
    sleep_val = max(frame_len-time_diff, 0)
    print(
        f"{i:04d} :: {datetime.timedelta(seconds=round((now-start)/ns_ratio))} @ {round(sleep_val*frame_rate*frame_rate):02d}sps | ")
    time.sleep(sleep_val)
    return time.time_ns()


p.loadSDF("box.sdf")

start_time = time.time_ns()
prev_time = start_time
for i in range(0, 1000):

    prev_time = frame_throttling(prev_time, start_time)

    p.stepSimulation()

p.disconnect()
