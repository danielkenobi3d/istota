build_order = ['source', 'rig', 'load data',  'finalize']
build = {
    'source': [
        ('Import geometry', ['rig_build.import_geometry']),
        # ('Import guides', ['rig_build.import_guides']),
        ('Import reference points', ['rig_build.import_reference_points'])
        ],
    'rig': [
        ('build biped', ['rig_biped.build_biped']),
        ('custom rig', ['rig_build.custom_rig']),
        ('visibility switches', ['visibility_switches.build'])
        ],
    'load data': [
        ('load skinning', ['rig_build.load_skinning_data']),
        ('load shapes', ['rig_build.load_shapes_data'])

    ],
    'finalize': [
        ('cleanup', ['rig_build.cleanup']),
        ('custom finalize', ['rig_build.custom_finalize'])
    ],
}