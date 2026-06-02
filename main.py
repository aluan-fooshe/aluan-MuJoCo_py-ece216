import mujoco
import mujoco.viewer
import numpy as np
import time

model = mujoco.MjModel.from_xml_path("gizmo.xml")
data  = mujoco.MjData(model)

# enable joint visualization option:
scene_option = mujoco.MjvOption()
scene_option.flags[mujoco.mjtVisFlag.mjVIS_JOINT] = True

# check geoms before launching viewer
try:
    model.geom('green_sphere')
    model.geom('red_box')
    print("both geoms found!")
except KeyError as e:
    print("geom not found:", e)

# Simulate and display video.
with mujoco.viewer.launch_passive(model, data) as viewer:
    start = time.time()
    while data.time < 10:
        mujoco.mj_step(model, data)
        viewer.sync()

        # keep in sync with real time
        elapsed = time.time() - start
        remaining = data.time - elapsed
        if remaining > 0:
            time.sleep(remaining)