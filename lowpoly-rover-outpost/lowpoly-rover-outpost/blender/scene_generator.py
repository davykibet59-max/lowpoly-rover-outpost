"""
Blender 4.x scene generator for Low-Poly Rover Outpost
Run inside Blender's scripting tab.
"""
import bpy
import math

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Ground
bpy.ops.mesh.primitive_plane_add(size=20, location=(0,0,0))
ground = bpy.context.active_object
ground.name = "Ground"

# Sun light
bpy.ops.object.light_add(type='SUN', location=(4,-4,8))
sun = bpy.context.active_object
sun.data.energy = 3.0

# Camera
bpy.ops.object.camera_add(location=(8,-10,6), rotation=(math.radians(68),0,math.radians(40)))
cam = bpy.context.active_object
bpy.context.scene.camera = cam

# Rover body
bpy.ops.mesh.primitive_cube_add(location=(0,0,1))
rover = bpy.context.active_object
rover.scale = (1.4,0.9,0.5)
rover.name = "RoverBody"

# Wheels
wheel_positions = [(-1.6,-1.1,0.4),(1.6,-1.1,0.4),(-1.6,1.1,0.4),(1.6,1.1,0.4)]
for i, pos in enumerate(wheel_positions, start=1):
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=0.5, depth=0.45, location=pos, rotation=(math.radians(90),0,0))
    wheel = bpy.context.active_object
    wheel.name = f"Wheel_{i}"

# Mast
bpy.ops.mesh.primitive_cylinder_add(radius=0.08, depth=1.6, location=(0.2,0,2.0))
mast = bpy.context.active_object
mast.name = "SensorMast"

# Solar panels
for x in (-2.6, 2.6):
    bpy.ops.mesh.primitive_cube_add(location=(x,0,1.6))
    panel = bpy.context.active_object
    panel.scale = (1.0, 1.8, 0.05)
    panel.name = f"SolarPanel_{'L' if x < 0 else 'R'}"

# Outpost module
bpy.ops.mesh.primitive_cube_add(location=(5,2,1.0))
mod = bpy.context.active_object
mod.scale = (1.8, 1.8, 1.0)
mod.name = "HabModule"

print("Scene generated successfully.")
