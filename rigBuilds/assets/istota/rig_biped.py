from istota.rigBuilds.assets.istota.customRig import rigBiped
from RMPY.core import controls


def build_biped():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    controls.color_now_all_ctrls()
    # tongue.build()

