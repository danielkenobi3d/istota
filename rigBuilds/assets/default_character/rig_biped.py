from RMPY.rig.biped import rigBiped
from RMPY.rig import rigHierarchy
from RMPY.core import controls
from RMPY.core import data_save_load
import pymel.core as pm
from RMPY.core import search_hierarchy
from RMPY.rig.switches import rigBoolSwitch

# from RMPY.rig.customRig import tongue

def build_biped():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    controls.color_now_all_ctrls()
    # tongue.build()


def hide_rigs():
    settings_rig_sistems = pm.ls('*_settings*_pnt')
    for each in settings_rig_sistems:
        each.visibility.set(False)


def hierarchy():
    rig_hierarchy = rigHierarchy.RigHierarchy()
    pm.parent('Model', rig_hierarchy.geometry)


def load_data():
    controls_list = pm.ls('*ctr')
    data_save_load.load_curves(*controls_list)
    geometry = search_hierarchy.shape_type_in_hierarchy(pm.ls('geometry')[0], mesh_list=[], object_type='mesh')
    data_save_load.load_skin_cluster(*geometry)


def finalize():
    hide_rigs()
    pm.delete('reference_points')
    # pm.delete('measures_ref_grp')


if __name__ == '__main__':
    build_rig()
    # data_save_load.save_curve()