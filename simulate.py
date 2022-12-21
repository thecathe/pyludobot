import sys
import datetime
import time

import pybullet_data
import pybullet as p

g_flags = {
    "-ft": True,  # frame throttle
    "-log": False
}

g_vars = {
    "loopuntil": 1000
}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg[0] == "-":
                if arg in g_flags.keys():
                    g_flags[arg] = not g_flags[arg]
                    print(f"successful {arg}")
                else:
                    print(f"unknown flag: {arg}")
            else:
                key, val = arg.split("=", 1)
                if key in g_vars.keys():
                    g_vars[key] = val
                    print(f"var {key} = {val}")
                else:
                    print(f"unknown var: {key}")
    else:
        print("no args given\n")

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

frame_rate = 120
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
    if g_flags["-log"]:
        print(
            f"{i:04d}"
            f" : {datetime.timedelta(seconds=round((now-start)/ns_ratio))}"
            f" @ {round(sleep_val*frame_rate*frame_rate):03d}sps | ")
    time.sleep(sleep_val)
    return time.time_ns()


def main_loop():
    p.stepSimulation()


p.setGravity(0, 0, -9.8)

planeID = p.loadURDF("plane.urdf")

p.loadSDF("boxes.sdf")

if g_flags["-ft"]:
    start_time = time.time_ns()
    prev_time = start_time
    # frame throttling
    for i in range(0, g_vars["loopuntil"]):
        prev_time = frame_throttling(prev_time, start_time)
        main_loop()
else:
    print("no throttling")
    # without throttling
    for i in range(0, g_vars["loopuntil"]):
        if g_flags["-log"]:
            print(f"{i:04d}")
        time.sleep(frame_len)
        main_loop()


p.disconnect()
