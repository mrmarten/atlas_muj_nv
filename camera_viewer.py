import mujoco_py

model = mujoco_py.load_model_from_path("atlas_nv_sandia.xml")
sim = mujoco_py.MjSim(model)

## a is a tuple if depth is True and a numpy array if depth is False ##
a = sim.render(width=200, height=200, camera_name='head_camera', depth=True)
rgb_img = a[0]
depth_img = a[1]