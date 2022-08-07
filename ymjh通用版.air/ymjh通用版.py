# -*- encoding=utf8 -*-
__author__ = "86133"

from airtest.core.api import *

auto_setup(__file__)
# 课业
# if exists(Template(r"tpl1629784944266.png", record_pos=(0.225, -0.263), resolution=(890, 522))):
#     touch(Template(r"tpl1629784944266.png", record_pos=(0.225, -0.263), resolution=(890, 522)))
# if exists(Template(r"tpl1658551968269.png", record_pos=(-0.341, -0.074), resolution=(1350, 797))):
#     touch(Template(r"tpl1658551968269.png", record_pos=(-0.341, -0.074), resolution=(1350, 797)))
#     touch(Template(r"tpl1658552042674.png", record_pos=(-0.283, 0.108), resolution=(1350, 797)))
#     touch(wait(Template(r"tpl1658552263499.png", record_pos=(0.358, 0.094), resolution=(1350, 797))))
#     touch(Template(r"tpl1658552288305.png", record_pos=(0.358, 0.094), resolution=(1350, 797)))
#     if exists(Template(r"tpl1658552570310.png", record_pos=(0.001, 0.075), resolution=(1350, 797))):
#         touch(Template(r"tpl1658552570310.png", record_pos=(0.001, 0.075), resolution=(1350, 797)))
#     if exists(Template(r"tpl1658552603100.png", record_pos=(-0.221, 0.075), resolution=(1350, 797))):
#         touch(Template(r"tpl1658552603100.png", record_pos=(-0.221, 0.075), resolution=(1350, 797)))
#     wait(Template(r"tpl1658552981188.png", record_pos=(0.0, 0.123), resolution=(1350, 797)))
#     if exists(Template(r"tpl1658552981188.png", record_pos=(0.0, 0.123), resolution=(1350, 797))):
#         touch(Template(r"tpl1658552981188.png", record_pos=(0.0, 0.123), resolution=(1350, 797)))
#         touch(Template(r"tpl1658554206346.png", record_pos=(0.17, 0.116), resolution=(1350, 797)))
#     if exists(Template(r"tpl1658554813590.png", record_pos=(-0.441, -0.167), resolution=(1350, 797))):
#         touch(Template(r"tpl1658554000768.png", record_pos=(-0.482, -0.169), resolution=(1350, 797)))
#         touch(Template(r"tpl1658554023416.png", record_pos=(-0.305, -0.143), resolution=(1350, 797)))
#         touch(Template(r"tpl1658554042058.png", record_pos=(-0.302, -0.08), resolution=(1350, 797)))
#         touch(Template(r"tpl1658554191265.png", record_pos=(0.237, 0.174), resolution=(1350, 797)))
#         touch(Template(r"tpl1658554200658.png", record_pos=(0.001, 0.123), resolution=(1350, 797)))
#         touch(Template(r"tpl1658554206346.png", record_pos=(0.17, 0.116), resolution=(1350, 797)))
#     if exists(Template(r"tpl1658554813590.png", record_pos=(-0.441, -0.167), resolution=(1350, 797))):
#         touch(Template(r"tpl1658554000768.png", record_pos=(-0.482, -0.169), resolution=(1350, 797)))
#         touch(Template(r"tpl1658554023416.png", record_pos=(-0.305, -0.143), resolution=(1350, 797)))
#         touch(Template(r"tpl1658554042058.png", record_pos=(-0.302, -0.08), resolution=(1350, 797)))
#         touch(Template(r"tpl1658554191265.png", record_pos=(0.237, 0.174), resolution=(1350, 797)))
#         touch(Template(r"tpl1658554200658.png", record_pos=(0.001, 0.123), resolution=(1350, 797)))
#         touch(Template(r"tpl1658554206346.png", record_pos=(0.17, 0.116), resolution=(1350, 797)))
#     if exists(Template(r"tpl1658554813590.png", record_pos=(-0.441, -0.167), resolution=(1350, 797))):
#         touch(Template(r"tpl1658554000768.png", record_pos=(-0.482, -0.169), resolution=(1350, 797)))
#         touch(Template(r"tpl1658554023416.png", record_pos=(-0.305, -0.143), resolution=(1350, 797)))
#         touch(Template(r"tpl1658554042058.png", record_pos=(-0.302, -0.08), resolution=(1350, 797)))
#         touch(Template(r"tpl1658554191265.png", record_pos=(0.237, 0.174), resolution=(1350, 797)))
#         touch(Template(r"tpl1658554200658.png", record_pos=(0.001, 0.123), resolution=(1350, 797)))
#         touch(Template(r"tpl1658554206346.png", record_pos=(0.17, 0.116), resolution=(1350, 797)))
#     touch(Template(r"tpl1658554904139.png", record_pos=(0.342, 0.047), resolution=(1350, 797)))
#     touch(Template(r"tpl1658554910606.png", record_pos=(0.17, 0.114), resolution=(1350, 797)))
#     touch(Template(r"tpl1658554918941.png", record_pos=(0.299, 0.026), resolution=(1350, 797)))









#华山论剑
if exists(Template(r"tpl1629784944266.png", record_pos=(0.225, -0.263), resolution=(890, 522))):
    touch(Template(r"tpl1629784944266.png", record_pos=(0.225, -0.263), resolution=(890, 522)))
pos = exists(Template(r"tpl1629566720355.png", record_pos=(-0.128, 0.266), resolution=(627, 369)))
if pos:touch(pos)
touch(Template(r"tpl1629566569580.png", record_pos=(-0.325, -0.028), resolution=(627, 369)))

touch(wait(Template(r"tpl1629567592054.png", record_pos=(0.28, -0.143), resolution=(627, 369)),timeout=5000))
touch(Template(r"tpl1629567604081.png", record_pos=(0.162, 0.114), resolution=(627, 369)))
sleep(10)
if exists(Template(r"tpl1659788527233.png", record_pos=(0.225, -0.266), resolution=(1352, 797))):
    touch(Template(r"tpl1659788527233.png", record_pos=(0.225, -0.266), resolution=(1352, 797)))
touch(Template(r"tpl1658551541821.png", record_pos=(-0.331, -0.089), resolution=(1350, 797)))
touch(Template(r"tpl1658551577582.png", record_pos=(0.151, 0.117), resolution=(1350, 797)))
sleep(1)
if exists(Template(r"tpl1629568389927.png", record_pos=(0.251, 0.106), resolution=(627, 369))):
    touch(Template(r"tpl1629568389927.png", record_pos=(0.251, 0.106), resolution=(627, 369)))
touch(Template(r"tpl1658556505616.png", record_pos=(0.376, -0.225), resolution=(1352, 797)))
touch(Template(r"tpl1658556524146.png", record_pos=(0.454, -0.258), resolution=(1352, 797)))


#江湖英雄榜
if exists(Template(r"tpl1629784944266.png", record_pos=(0.225, -0.263), resolution=(890, 522))):
    touch(Template(r"tpl1629784944266.png", record_pos=(0.225, -0.263), resolution=(890, 522)))
if exists(Template(r"tpl1629776346107.png", record_pos=(-0.13, 0.257), resolution=(890, 522))):
    touch(Template(r"tpl1629776360801.png", record_pos=(-0.131, 0.265), resolution=(890, 522)))
if exists(Template(r"tpl1629776393551.png", record_pos=(0.139, 0.156), resolution=(890, 522))):
    touch(Template(r"tpl1629776583038.png", record_pos=(0.134, 0.164), resolution=(890, 522)))

if exists(Template(r"tpl1629776209662.png", record_pos=(0.34, 0.175), resolution=(890, 522))):
    touch(Template(r"tpl1629776209662.png", record_pos=(0.34, 0.175), resolution=(890, 522)))
    touch(wait(Template(r"tpl1629776227082.png", record_pos=(0.394, -0.133), resolution=(890, 522)),timeout=5000))
    touch(Template(r"tpl1629776260346.png", record_pos=(0.169, 0.115), resolution=(890, 522)))
    touch(Template(r"tpl1629776434292.png", record_pos=(-0.022, 0.236), resolution=(890, 522)))
    sleep(10)


if exists(Template(r"tpl1658551101202.png", record_pos=(-0.153, 0.176), resolution=(1350, 797))):
    touch(Template(r"tpl1658551101202.png", record_pos=(-0.153, 0.176), resolution=(1350, 797)))



if exists(Template(r"tpl1629779373304.png", record_pos=(0.297, 0.028), resolution=(890, 522))):
    touch(Template(r"tpl1629779373304.png", record_pos=(0.297, 0.028), resolution=(890, 522)))
    if exists(Template(r"tpl1658550442640.png", record_pos=(-0.001, 0.111), resolution=(1352, 797))):
        touch(Template(r"tpl1658550442640.png", record_pos=(-0.001, 0.111), resolution=(1352, 797)))
if exists(Template(r"tpl1629779418762.png", record_pos=(-0.004, 0.194), resolution=(890, 522))):
        touch(Template(r"tpl1629779418762.png", record_pos=(-0.004, 0.194), resolution=(890, 522)))
if exists(Template(r"tpl1629779373304.png", record_pos=(0.297, 0.028), resolution=(890, 522))):
    touch(Template(r"tpl1629779373304.png", record_pos=(0.297, 0.028), resolution=(890, 522)))
    if exists(Template(r"tpl1658550442640.png", record_pos=(-0.001, 0.111), resolution=(1352, 797))):
        touch(Template(r"tpl1658550442640.png", record_pos=(-0.001, 0.111), resolution=(1352, 797)))
if exists(Template(r"tpl1629779418762.png", record_pos=(-0.004, 0.194), resolution=(890, 522))):
        touch(Template(r"tpl1629779418762.png", record_pos=(-0.004, 0.194), resolution=(890, 522)))
if exists(Template(r"tpl1629779373304.png", record_pos=(0.297, 0.028), resolution=(890, 522))):
    touch(Template(r"tpl1629779373304.png", record_pos=(0.297, 0.028), resolution=(890, 522)))
    if exists(Template(r"tpl1658550442640.png", record_pos=(-0.001, 0.111), resolution=(1352, 797))):
        touch(Template(r"tpl1658550442640.png", record_pos=(-0.001, 0.111), resolution=(1352, 797)))
if exists(Template(r"tpl1629779418762.png", record_pos=(-0.004, 0.194), resolution=(890, 522))):
        touch(Template(r"tpl1629779418762.png", record_pos=(-0.004, 0.194), resolution=(890, 522)))
if exists(Template(r"tpl1629779373304.png", record_pos=(0.297, 0.028), resolution=(890, 522))):
    touch(Template(r"tpl1629779373304.png", record_pos=(0.297, 0.028), resolution=(890, 522)))
    if exists(Template(r"tpl1658550442640.png", record_pos=(-0.001, 0.111), resolution=(1352, 797))):
        touch(Template(r"tpl1658550442640.png", record_pos=(-0.001, 0.111), resolution=(1352, 797)))
if exists(Template(r"tpl1629779418762.png", record_pos=(-0.004, 0.194), resolution=(890, 522))):
        touch(Template(r"tpl1629779418762.png", record_pos=(-0.004, 0.194), resolution=(890, 522)))
touch(Template(r"tpl1629876896946.png", record_pos=(0.374, -0.224), resolution=(1039, 609)))
#银票和神器碎片
# touch([1051,39])
# if exists(Template(r"tpl1629876216494.png", record_pos=(0.454, -0.021), resolution=(1340, 785))):
#     touch(Template(r"tpl1629876233137.png", record_pos=(0.456, -0.021), resolution=(1340, 785)))
#     if exists(Template(r"tpl1629876294130.png", record_pos=(-0.1, -0.091), resolution=(1340, 785))):
#         touch(Template(r"tpl1629876313974.png", record_pos=(-0.134, -0.079), resolution=(1292, 785)))
#         if exists(Template(r"tpl1629876355499.png", record_pos=(0.436, 0.19), resolution=(1226, 785))):
#             touch(Template(r"tpl1629876369610.png", record_pos=(0.437, 0.191), resolution=(1226, 785)),duration=4)
#             if exists(Template(r"tpl1629876444662.png", record_pos=(0.342, 0.263), resolution=(1226, 785))):
#                 touch(Template(r"tpl1629876460536.png", record_pos=(0.36, 0.269), resolution=(1182, 785)))
# else:
#     if exists(Template(r"tpl1629876294130.png", record_pos=(-0.1, -0.091), resolution=(1340, 785))):
#         touch(Template(r"tpl1629876313974.png", record_pos=(-0.134, -0.079), resolution=(1292, 785)))
#         if exists(Template(r"tpl1629876355499.png", record_pos=(0.436, 0.19), resolution=(1226, 785))):
#             touch(Template(r"tpl1629876369610.png", record_pos=(0.437, 0.191), resolution=(1226, 785)),duration=4)
#             if exists(Template(r"tpl1629876444662.png", record_pos=(0.342, 0.263), resolution=(1226, 785))):
#                 touch(Template(r"tpl1629876460536.png", record_pos=(0.36, 0.269), resolution=(1182, 785)))
#                 touch(Template(r"tpl1629876752984.png", record_pos=(0.297, 0.027), resolution=(1039, 609)))
#                 touch(Template(r"tpl1629876766023.png", record_pos=(-0.0, 0.111), resolution=(1039, 609)))
# touch(Template(r"tpl1629876910870.png", record_pos=(0.455, -0.26), resolution=(1039, 609)))                
# if exists(Template(r"tpl1629975712355.png", record_pos=(0.299, 0.029), resolution=(1340, 785))):
#     touch(Template(r"tpl1629975712355.png", record_pos=(0.299, 0.029), resolution=(1340, 785)))
#     if exists(Template(r"tpl1629975712355.png", record_pos=(0.299, 0.029), resolution=(1340, 785))):
#         touch(Template(r"tpl1629975712355.png", record_pos=(0.299, 0.029), resolution=(1340, 785)))





touch(wait(Template(r"tpl1629713584157.png", record_pos=(0.456, -0.142), resolution=(1340, 785))),timeout=1000)

if exists(Template(r"tpl1629713659612.png", record_pos=(0.334, -0.012), resolution=(1340, 785))):
    touch(Template(r"tpl1629713659612.png", record_pos=(0.334, -0.012), resolution=(1340, 785)))
    touch(Template(r"tpl1629716891963.png", record_pos=(-0.361, 0.195), resolution=(1022, 598)))
    touch(Template(r"tpl1629716909219.png", record_pos=(-0.092, 0.154), resolution=(1022, 598)))
    touch(Template(r"tpl1629716937979.png", record_pos=(0.297, 0.027), resolution=(1022, 598)))
    touch(Template(r"tpl1629716944927.png", record_pos=(0.258, -0.142), resolution=(1022, 598)))
    touch(Template(r"tpl1629716952541.png", record_pos=(0.452, -0.262), resolution=(1022, 598)))

#星阵
touch(wait(Template(r"tpl1629713584157.png", record_pos=(0.456, -0.142), resolution=(1340, 785)))

,timeout=1000)
touch(Template(r"tpl1629713637617.png", record_pos=(0.45, -0.01), resolution=(1340, 785)))
touch(Template(r"tpl1629713848365.png", record_pos=(0.419, -0.203), resolution=(1340, 785)))

touch(Template(r"tpl1629713856241.png", record_pos=(-0.142, 0.062), resolution=(1340, 785)))
touch(Template(r"tpl1629713865083.png", record_pos=(0.11, 0.262), resolution=(1340, 785)))
touch(Template(r"tpl1629714517475.png", record_pos=(-0.289, 0.086), resolution=(1022, 598)))
wait(Template(r"tpl1629714579443.png", record_pos=(0.406, 0.259), resolution=(1022, 598)),timeout=10000)
if exists(Template(r"tpl1629714579443.png", record_pos=(0.406, 0.259), resolution=(1022, 598))):

    wait(Template(r"tpl1659680895415.png", record_pos=(-0.254, 0.232), resolution=(1352, 797)),timeout=10000)
    if exists(Template(r"tpl1659680895415.png", record_pos=(-0.254, 0.232), resolution=(1352, 797))):
        touch(Template(r"tpl1629714579443.png", record_pos=(0.406, 0.259), resolution=(1022, 598)))
        sleep(1)
        touch(Template(r"tpl1629716603641.png", record_pos=(0.444, -0.265), resolution=(1022, 598)))
        touch(Template(r"tpl1629716712191.png", record_pos=(0.167, 0.114), resolution=(1022, 598)))

        touch(Template(r"tpl1629716532036.png", record_pos=(-0.027, 0.254), resolution=(1022, 598)))
if exists(Template(r"tpl1659795034284.png", record_pos=(0.3, 0.028), resolution=(1352, 797))):
    touch(Template(r"tpl1659795034284.png", record_pos=(0.3, 0.028), resolution=(1352, 797)))
    if exists(Template(r"tpl1659795074218.png", record_pos=(0.0, 0.111), resolution=(1352, 797))):
        touch(Template(r"tpl1659795084501.png", record_pos=(0.0, 0.111), resolution=(1352, 797)))
        touch(Template(r"tpl1629779418762.png", record_pos=(-0.004, 0.194), resolution=(890, 522)))


#开始帮派按任务
touch(Template(r"tpl1629784944266.png", record_pos=(0.225, -0.263), resolution=(890, 522)))
pos1 = exists(Template(r"tpl1629629383596.png", record_pos=(-0.24, 0.264), resolution=(1340, 785)))


if pos1:touch(pos1)
touch(Template(r"tpl1629629457969.png", record_pos=(-0.285, -0.047), resolution=(1065, 785)))
sleep(30)
touch(wait(Template(r"tpl1629630613913.png", record_pos=(0.358, 0.09), resolution=(746, 437)),timeout=5000))
touch(Template(r"tpl1629630625666.png", record_pos=(0.357, 0.092), resolution=(746, 437)))
wait(Template(r"tpl1629630847422.png", record_pos=(0.212, 0.23), resolution=(746, 437)),timeout=50000)
touch(Template(r"tpl1629630847422.png", record_pos=(0.212, 0.23), resolution=(746, 437)))
touch(wait(Template(r"tpl1629631327945.png", record_pos=(0.338, 0.05), resolution=(746, 437)),timeout=2000))
touch(wait(Template(r"tpl1629689580945.png", record_pos=(-0.346, 0.22), resolution=(1322, 785)),timeout=2000))
sleep(1.0)
#前往江南
touch(Template(r"tpl1629784944266.png", record_pos=(0.225, -0.263), resolution=(890, 522)))
if exists(Template(r"tpl1629802174949.png", record_pos=(0.085, 0.264), resolution=(1272, 746))):
    touch(Template(r"tpl1629802174949.png", record_pos=(0.085, 0.264), resolution=(1272, 746)))
    touch(Template(r"tpl1629802209271.png", record_pos=(-0.363, 0.131), resolution=(1272, 746)))
    touch(Template(r"tpl1629802239330.png", record_pos=(0.252, -0.035), resolution=(1272, 746)))
    sleep(40)
    touch(wait(Template(r"tpl1629808453961.png", record_pos=(0.47, -0.269), resolution=(737, 432)),timeout =5000))



else:
    touch(Template(r"tpl1629802209271.png", record_pos=(-0.363, 0.131), resolution=(1272, 746)))

#     touch(Template(r"tpl1629792051747.png", record_pos=(0.468, -0.268), resolution=(979, 574)))
    touch(Template(r"tpl1629802239330.png", record_pos=(0.252, -0.035), resolution=(1272, 746)))
    sleep(40)
    touch(wait(Template(r"tpl1629808453961.png", record_pos=(0.47, -0.269), resolution=(737, 432)),timeout =5000))
#前往剑冢，烽火等
#生死剑冢三次
if exists(Template(r"tpl1629808650593.png", record_pos=(0.226, -0.263), resolution=(737, 432))):
    touch(Template(r"tpl1629808650593.png", record_pos=(0.226, -0.263), resolution=(737, 432)))
pos = exists(Template(r"tpl1629566720355.png", record_pos=(-0.128, 0.266), resolution=(627, 369)))
if pos:
    touch(pos)
    touch(Template(r"tpl1629637856824.png", record_pos=(0.223, -0.057), resolution=(746, 437)))
    touch(Template(r"tpl1629637907803.png", record_pos=(0.338, 0.171), resolution=(746, 437)))
    touch(wait(Template(r"tpl1629638449338.png", record_pos=(-0.131, 0.113), resolution=(746, 437)),timeout=3000000))
touch(Template(r"tpl1629808650593.png", record_pos=(0.226, -0.263), resolution=(737, 432)))
if pos:
    touch(pos)
    touch(Template(r"tpl1629637856824.png", record_pos=(0.223, -0.057), resolution=(746, 437)))
    touch(Template(r"tpl1629637907803.png", record_pos=(0.338, 0.171), resolution=(746, 437)))
    touch(wait(Template(r"tpl1629638449338.png", record_pos=(-0.131, 0.113), resolution=(746, 437)),timeout=3000000))
touch(Template(r"tpl1629808650593.png", record_pos=(0.226, -0.263), resolution=(737, 432)))
if pos:
    touch(pos)
    touch(Template(r"tpl1629637856824.png", record_pos=(0.223, -0.057), resolution=(746, 437)))
    touch(Template(r"tpl1629637907803.png", record_pos=(0.338, 0.171), resolution=(746, 437)))
    touch(wait(Template(r"tpl1629638449338.png", record_pos=(-0.131, 0.113), resolution=(746, 437)),timeout=3000000))

