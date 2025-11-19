from RMPY.rig.biped.rig import finger

toe_points=['L_toeThumb01_reference_grp', 'L_toeThumb02_reference_grp', 'L_toeThumb03_reference_grp']
mid_thumb_points = ['L_midThumb01_reference_grp', 'L_midThumb02_reference_grp', 'L_midThumb03_reference_grp']
pinky_thumb_points = ['L_pinkyThumb01_reference_grp', 'L_pinkyThumb02_reference_grp', 'L_pinkyThumb03_reference_grp']
toe_finger = finger.Finger()
toe_finger.create_point_base(*toe_points)