from RMPY.rig.facial import rigJaw

jaw_points = ['C_jaw01_reference_pnt', 'C_jawTip01_reference_pnt']
jaw = rigJaw.RigJaw()
jaw.create_point_base(*jaw_points)
