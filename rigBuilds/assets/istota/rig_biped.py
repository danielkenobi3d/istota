from istota.rigBuilds.assets.istota.customRig import rigBiped
from RMPY.core import controls
from RMPY.rig import rigCorrectives
import importlib
importlib.reload(rigBiped)
from builder.pipeline import environment
from istota.rigBuilds.assets.istota.customRig import correctives_definition
import importlib
importlib.reload(correctives_definition)

def build_biped():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    env = environment.Environment()

    # rig_correctives = rigCorrectives.CorrectiveBlendShapes(definition=correctives_definition)
    # rig_correctives.build()
    controls.color_now_all_ctrls()
    # tongue.build()

