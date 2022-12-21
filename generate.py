import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

start_length, start_width, start_height = [1, 1, 1]
length, width, height = [start_length, start_width, start_height]

z_sep = 0.1
origin_x, origin_y, origin_z = [0, 0, start_height + z_sep]

for xi in range(0, 2):
    for yi in range(0, 2):
        z_offset = 0.1
        length, width, height = [1, 1, 1]
        x, y, z = [0+(xi*width)+((start_width/2)-(width/2)),
                   0 + (yi*length)+((start_length/2)-(length/2)),
                   origin_z + height]
        for i in range(0, 10):
            pyrosim.Send_Cube(name=f"Box{i}",
                              pos=[x, y, z+z_offset],
                              size=[length, width, height]
                              )
            z_offset += z_sep+height
            length *= 0.9
            width *= 0.9
            height *= 0.9


pyrosim.End()
