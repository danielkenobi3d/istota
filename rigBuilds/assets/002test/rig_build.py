from pymel.core.system import reference

from RMPY.rig import rigSingleJoint
from RMPY.rig import rigWorld
import pymel.core as pm

def custom_rig():
    rig_world = rigWorld.RigWorld()
    rig_main = rigSingleJoint.RigSingleJoint()
    reference_points = pm.ls('reference_points')[0]
    rig_main.create_point_base(*reference_points.getChildren(),
                               size=.2,
                               centered = True)
    rig_main.rename_as_skinned_joints()
    rig_main.set_parent(rig_world)
    geo = pm.group(empty=True, name='geo')
    geo.setParent('rig')
    pm.parent('pCube1',geo)