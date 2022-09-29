#!/usr/bin/python3
import mujoco_py

model = mujoco_py.load_model_from_path("atlas_nv_sandia.xml")
sim = mujoco_py.MjSim(model)

a = sim.render(width=200, height=200, camera_name='lidar', depth=True)
rgb_img = a[0]
depth_img = a[1]
