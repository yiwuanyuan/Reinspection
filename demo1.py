#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : demo1.py
# Author: Wangyuan
# Date  : 2019/8/23

Z2CN18_10 = {
    'standard':'M3307',
    'chemical':{
        'ele':{
        'C':0.030,
        'Si':1.00,
        'Mn':2.00,
        'P':0.035,
        'S':0.020,
        'Cr':{'min':17.00,'max':20.00},
        'Ni':{'min':17.00,'max':20.00},
        'Cu':1.0,
        'B':0.0018,
        'Co':'依据技术规格书',
        },
        'test_stand':'试验依据MC1000进行'},
    'pyhsical':{
        'Tensile_test':{
            'room_temp':{
                'temp':{'min':18.00,'max':28.00},
                'rp0.2':{'min':175},
                'rm':{'min':490},
                'A':{'more3':{'min':45},'less3':{'min':40}},
                'Z':'记录数据',
                'sample_stand':"试样尺寸应符合MC1000 的规定",
                'test_stand':'拉伸试验应按MC1000的规定进行',
            },
            'high_temp':{
                'temp':350,
                'rp0.2':{'min':125},
                'rm':{'min':350},
                'A':'记录数据',
                'Z':'记录数据',
                'sample_stand':"试样尺寸应符合MC1000 的规定",
                'test_stand':'拉伸试验应按MC1000的规定进行',
            },
        },

    },
    'IC':{
        'temp':{'min':690.00,'max':710.00},
        'test_stand': '晶间腐蚀试验必须按B2300、C2300 和D2300 的规定进行',
        'result':'腐蚀试验后，如果试样在锤击检查中发出清脆的金属声，且在弯曲试验中无裂纹和开裂现象，则该腐蚀试验结果合格。若有疑问，可用显微检测判定是否存在晶间腐蚀。'
    },
}