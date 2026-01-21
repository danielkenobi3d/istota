corrective_order: ['knee']

config_correctives: {'knee': {'targets': [-130],
                                'drivers': ['L_intermediate00_leg_jnt', 'L_intermediate01_leg_jnt'],
                                'rotationOrder': 'zyx', 'RFlip': True},
                       },

'base_mesh': {'istota': {  # 'arm': ['L_armZ60_corrective_msh'],
    # 'elbow': ['L_elbowYn90_corrective_msh'],
    # 'elbow': ['L_elbowYn90_corrective_msh'],
    'knee': ['L_kneeZn130_corrective_msh'],
    # 'leg': ['L_legZ90_corrective_msh'],
    # 'legn': ['L_legZn90_corrective_msh'],
    # 'legSide': ['L_legY90_corrective_msh'],
    # 'ankle': ['L_ankleFeet40_corrective_msh'],
    # 'anklen': ['L_ankleFeetn40_corrective_msh'],
}
}