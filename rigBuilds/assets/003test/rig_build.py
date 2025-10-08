from RMPY.rig import rigSingleJoint
from RMPY.rig import rigWorld
import pymel.core as pm

def custom_rig():
    rig_world = rigWorld.RigWorld()
    rig_main = rigSingleJoint.RigSingleJoint()
    reference_points = pm.ls('reference_points')[0]
    rig_main.create_point_base(*reference_points.getChildren())
    rig_main.set_parent(rig_world)