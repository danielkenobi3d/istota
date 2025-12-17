from RMPY.rig import rigStaticLayer
from RMPY.rig import rigSingleJoint
from RMPY.core import data_save_load
import pymel.core as pm
def build():
    geometries=['istota']
    static_layer = rigStaticLayer.StaticLayer(*geometries, name='breath')
    breath_points = pm.ls('C_breath00_reference_grp')[0]
    breath_rig = rigSingleJoint.RigSingleJoint()
    breath_rig.create_point_base(*breath_points.getChildren(), static=True, scaleXZ=True)
    print(breath_rig.zero_joint)
    data_save_load.load_skin_cluster('C_istota00_breath_msh')


if __name__=='__main__':
    build()

