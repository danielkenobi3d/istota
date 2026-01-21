from istota.rigBuilds.assets.istota.customRig import rigBiped
from RMPY.core import controls
from RMPY.rig import rigCorrectives
import importlib
importlib.reload(rigBiped)
from builder.pipeline import environment

def build_biped():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    env = environment.Environment()
    geo_definition = env.get_variables_from_path(environment.pipe_config.geo_definition)

    rig_correctives = rigCorrectives.CorrectiveBlendShapes(definition=geo_definition.correctives_definition)
    rig_correctives.build()
    controls.color_now_all_ctrls()
    # tongue.build()

