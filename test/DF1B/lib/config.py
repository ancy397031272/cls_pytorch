#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-


class DF1BConfig:
    # 检测小图的尺寸
    img_shape = (256, 256)
    # 对整图裁剪时的overlap大小
    overlap_piexl = 200
    # 权重的路径
    model_path = 'lib/model_cls.pth'

    # ng图片输出值
    ng_label = 1
    # 对整张图片划窗裁剪，以下是需要检测的小图的索引
    imgs_index_dict = {
        'EU12': [321, 322, 408, 451, 494, 537, 580, 623, 666, 709, 752, 795, 838, 881, 924, 967, 1010, 1053, 1096, 1139,
                 1182], 'EU11': [756, 799, 842, 885, 928, 971], 'EU2': [712, 754, 755], 'UL15': [674, 717, 760, 803],
        'UL10': [460, 503, 504, 547, 590, 633, 676, 719, 762, 805, 848, 891, 934],
        'EU8': [193, 236, 322, 365, 408, 451, 494, 537, 580, 623, 666, 709, 752, 795, 838, 881, 924, 1010, 1011, 1053,
                1054],
        'UL14': [458, 459, 544, 545, 587, 588, 630, 631, 673, 674, 716, 717, 759, 760, 802, 803, 888, 889, 931, 932],
        'EU6': [709, 710, 752, 795], 'EU9': [326, 369, 412, 455, 456, 498, 499],
        'EU4': [448, 491, 534, 577, 620, 663, 706, 749, 792, 793, 835, 836, 878, 879, 922, 965, 1008, 1051],
        'EU5': [364, 493, 579], 'UL6': [458, 459, 501, 502, 545, 802, 803, 845, 846, 888],
        'EU10': [456, 499, 542, 585, 628, 671, 714, 757, 800, 843, 886, 929],
        'UL8': [241, 284, 327, 370, 413, 456, 499, 542, 585, 628, 629, 671, 672, 714, 715, 757, 758, 800, 801, 844, 887,
                930, 973, 1016, 1059], 'UL1': [374, 417, 461, 504, 547], 'UL5': [501, 544, 545, 588],
        'EU0': [276, 277, 319, 320, 406, 449, 492, 535, 578, 621, 664, 707, 750, 793, 836, 922, 965],
        'UL9': [374, 417, 460, 503, 504, 546], 'UL13': [458, 501, 544, 545, 588],
        'UL12': [326, 327, 369, 370, 413, 456, 499, 542, 585, 628, 671, 714, 757, 800, 843, 886, 929, 972, 1015, 1016,
                 1058, 1059, 1102, 1145],
        'UL0': [241, 327, 370, 413, 456, 457, 499, 500, 542, 543, 585, 586, 628, 629, 672, 715, 758, 801, 844, 887, 930,
                1016, 1059],
        'UL4': [370, 413, 456, 499, 542, 585, 628, 671, 714, 757, 800, 843, 886, 929, 972, 1015, 1058, 1059, 1101, 1102,
                1144, 1145, 1187, 1188], 'EU1': [280, 323, 366, 452, 495], 'EU15': [712, 755, 798],
        'UL3': [805, 848, 891, 933, 934, 976, 1019], 'EU3': [839, 882, 925, 968, 1011], 'UL7': [],
        'EU13': [453, 582, 625], 'UL11': [761, 933, 934, 976, 977], 'EU7': [752, 795, 838, 881, 924, 967],
        'EU14': [410, 453, 496, 539, 582, 625, 668, 711, 754, 797, 883, 926],
        'UL2': [417, 418, 461, 504, 547, 590, 633, 762, 805, 848, 891, 934]}

    # 由于视角更改，以下是映射列表
    imgs_index_map_dict = {
        12: 0,
        13: 1,
        14: 2,
        15: 3,
        16: 4,
        17: 5,
        18: 6,
        19: 7,
        50: 8,
        51: 9,
        52: 10,
        53: 11,
        54: 12,
        55: 13,
        56: 14,
        57: 15
    }
