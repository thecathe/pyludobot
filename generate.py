import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

length, width, height = [1, 2, 3]
x, y, z = [0, 0, 0.5 + height]

pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

pyrosim.End()
