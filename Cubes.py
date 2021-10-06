import bpy
import requests

# Set initial values
xpos = 0
ypos = 0
zpos = 0
zpos_base = 0
ypos_base = 0

# Draw Depth (Y)
for depth in range(5):
    
    
    #Draw Height loop (Z)
    for row in range(5):
        
        #Draw row loop (x)
        for x in range(0,10):
            xpos = xpos + 1.5
            
            if (x % 2) == 0:
                zpos = zpos_base + 0.5
                ypos = ypos_base + 0.5
            else:
               zpos = zpos_base
               ypos = ypos_base
            
            # Draw cube or sphere - uncomment as required. (or not)
            bpy.ops.mesh.primitive_cube_add(size=0.5, enter_editmode=False, location=(xpos, ypos, zpos))
            bpy.ops.mesh.primitive_uv_sphere_add(radius=0.3, enter_editmode=False, location=(xpos, ypos, zpos +0.0))

        # Increment Z access after for next row    
        zpos_base = zpos_base + 2
        xpos = 0
    
    # Increment Y access for next depth layer
    ypos_base = ypos_base + 2
    ypos = ypos_base

    # Reset X and Z        
    xpos = 0
    zpos_base = 0
