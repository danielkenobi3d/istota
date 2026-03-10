prefix_geometry_list = []

definition = dict(
    brow=dict(
        type='blend_shape_definition',
        isSymetrical=True,
        baseMesh='character',
        control='L_facial00_brow_ctr',
        blendShapes=dict(LOutBrowUp={'connection': 'browOut', 'value': 10},
                         LOutBrowDwn={'connection': 'browOut', 'value': -10},
                         LInBrowUp={'connection': 'browIn', 'value': 10},
                         LInBrowDwn={'connection': 'browIn', 'value': -10},
                         LeyesCls={'connection': 'eyeCls', 'value': 10},
                         LeyesCls50={'connection': 'eyeCls', 'value': 5},
                         LeyesOpen={'connection': 'eyeCls', 'value': -10},
                         LeyeFlat = {'connection': 'eyeFlat', 'value': 10},
                         ),
        attributes=dict(browOut={'type': 'float', 'min': -10, 'max': 10},
                        browIn={'type': 'float', 'min': -10, 'max': 10},
                        eyeCls={'type': 'float', 'min': -10, 'max': 10},
                        eyeFlat={'type': 'float', 'min': 0, 'max': 10},
                        ),
        order=['browOut', 'browIn', 'eyeCls', 'eyeFlat']
        ),
    cheeks=dict(
        type='blend_shape_definition',
        isSymetrical=True,
        baseMesh='character',
        control='L_facial00_cheek_ctr',
        blendShapes=dict(Lsquint={'connection': 'squint', 'value': 10},
                         LnoseCorrugator={'connection': 'noseCorrugator', 'value': 10},
                         ),
        attributes=dict(squint={'type': 'float', 'min': 0, 'max': 10},
                        noseCorrugator={'type': 'float', 'min': 0, 'max': 10},),
        order=['squint', 'noseCorrugator']
        ),
    browCorrugator=dict(
        type='blend_shape_definition',
        isSymetrical=False,
        baseMesh='character',
        control='C_facial00_foreHead_ctr',
        blendShapes=dict(
                         browCorrugator={'connection': 'corrugator', 'value': 10},
                         ),
        attributes=dict(
                        corrugator={'type': 'float', 'min': 0, 'max': 10},
        ),
        order=['corrugator' ]


    )
)
eyes_dict = dict(
    eyes=dict(
        type='blend_shape_definition',
        isSymetrical=True,
        baseMesh='character',
        control='L_aim00_eye_grp',
        blendShapes=dict(LlookLeft={'connection': 'rotateY', 'value': 18},
                         LlookRight={'connection': 'rotateY', 'value': -18},
                         LlookUp={'connection': 'rotateZ', 'value': 18},
                         LlookDwn={'connection': 'rotateZ', 'value': -18},
                         ),
        attributes=dict(rotateY={'type': 'float', 'min': -18, 'max': 18},
                        rotateZ={'type': 'float', 'min': -18, 'max': 18},),
        order=['rotateY', 'rotateZ']
    ))

correctives_dict = dict(
        jawCorrectives=dict(
            type='blend_shape_definition',
            isSymetrical=False,
            baseMesh='character',
            control='C_joint00_jaw_ctr',
            blendShapes=dict(jawOpen={'connection': 'rotateZ', 'value': 12}),
            attributes=dict(rotateZ={'type': 'float', 'min': 0, 'max': 10}),
            order=['rotateZ']
            ),
)

direct_blendshape = {
    'character': 'C_BODY_001_HIGH'
}

jaw_layer = [u'character']


if __name__ == '__main__':
    import pymel.core as pm
    selection_list=[]
    for each_dictionary in [definition, eyes_dict]:
        for each_setup in each_dictionary.keys():
            for each_blendshape in each_dictionary[each_setup]['blendShapes'].keys():
                if not pm.objExists(each_blendshape):
                    print ('{} not found'.format(each_blendshape))
                if not pm.ls(each_blendshape)[0].getParent().name() == 'blendshapes':
                    selection_list.append(each_blendshape)
    pm.select(selection_list)


