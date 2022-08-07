# -*- encoding=utf8 -*-
__author__ = "86133"
import win32api   
from airtest.core.api import *

auto_setup(__file__)
position=win32api.GetCursorPos()
print(position)
# def getCursor():
#     print win32api.GetCursorPos()
# touch([662,312],10)
# pos2=assert_exists(Template(r"tpl1629615068108.png", record_pos=(-0.442, -0.166), resolution=(910, 530)), "存在观梦")
# if pos2:touch(Template(r"tpl1629615068108.png", record_pos=(-0.442, -0.166), resolution=(910, 530)))
# pos1=assert_not_exists(Template(r"tpl1629615068108.png", record_pos=(-0.442, -0.166), resolution=(910, 530)), "不存在观梦")
# if pos1:touch(Template(r"tpl1629615248321.png", record_pos=(0.279, 0.015), resolution=(910, 530)))
# click(1762,512)
# ifexists(Template(r"tpl1629625904079.png", record_pos=(0.0, 0.121), resolution=(910, 530)))
# touch(Template(r"tpl1629625904079.png", record_pos=(0.0, 0.121), resolution=(910, 530)))
# touch(Template(r"tpl1629625953461.png", record_pos=(0.164, 0.118), resolution=(910, 530)))
# wait(Template(r"tpl1629626009005.png", record_pos=(0.342, 0.048), resolution=(910, 530)))touch(Template(r"tpl1629626236310.png", record_pos=(0.169, 0.113), resolution=(910, 530)))
# wait(Template(r"tpl1629630847422.png", record_pos=(0.212, 0.23), resolution=(746, 437)),timeout=500)
# touch(Template(r"tpl1629630847422.png", record_pos=(0.212, 0.23), resolution=(746, 437)))
# wait(Template(r"tpl1629631327945.png", record_pos=(0.338, 0.05), resolution=(746, 437)))
#touch([610,367])
# if not exists(Template(r"tpl1629568294263.png", record_pos=(0.224, -0.246), resolution=(627, 369))):
#     touch(Template(r"tpl1629688336746.png", record_pos=(0.244, 0.182), resolution=(1340, 785)))

# else:
#     touch(Template(r"tpl1629568294263.png", record_pos=(0.224, -0.246), resolution=(627, 369)))

# # pos = exists(Template(r"tpl1629566720355.png", record_pos=(-0.128, 0.266), resolution=(627, 369)))
#     if pos:touch(pos)
#     touch(Template(r"tpl1629566569580.png", record_pos=(-0.325, -0.028), resolution=(627, 369)))
# sleep(20)

# touch(Template(r"tpl1629567592054.png", record_pos=(0.28, -0.143), resolution=(627, 369)))
# touch(Template(r"tpl1629567604081.png", record_pos=(0.162, 0.114), resolution=(627, 369)))
# if exists(Template(r"tpl1629779953642.png", record_pos=(-0.156, 0.155), resolution=(890, 522))):
#     touch(Template(r"tpl1629776644969.png", record_pos=(-0.156, 0.178), resolution=(890, 522)))
    
# sleep(2)
touch(Template(r"tpl1629784944266.png", record_pos=(0.225, -0.263), resolution=(890, 522)))

if exists(Template(r"tpl1629631838894.png", record_pos=(-0.347, 0.263), resolution=(746, 437))):
        touch(Template(r"tpl1629631853708.png", record_pos=(-0.349, 0.259), resolution=(746, 437)))
else:
    if exists(Template(r"tpl1629631920109.png", record_pos=(0.126, 0.137), resolution=(746, 437))):
        touch(Template(r"tpl1629631920109.png", record_pos=(0.126, 0.137), resolution=(746, 437)))
    else:
        touch(Template(r"tpl1629636412515.png", record_pos=(0.131, 0.078), resolution=(746, 437)))
swipe(Template(r"tpl1629782712370.png", record_pos=(-0.09, 0.0), resolution=(890, 522)), vector=[0.3472, -0.0019])
swipe(Template(r"tpl1629782738611.png", record_pos=(-0.054, -0.008), resolution=(890, 522)), vector=[0.3112, 0.0019])
swipe(Template(r"tpl1629784895916.png", record_pos=(-0.089, -0.007), resolution=(890, 522)), vector=[0.2854, 0.0096])



if exists(Template(r"tpl1629785162404.png", record_pos=(-0.227, 0.039), resolution=(890, 522))):
    touch(Template(r"tpl1629632965307.png", record_pos=(-0.097, -0.073), resolution=(746, 437)))
    if exists(Template(r"tpl1629687099656.png", record_pos=(0.055, 0.001), resolution=(1340, 785))):
        touch(Template(r"tpl1629687099656.png", record_pos=(0.055, 0.001), resolution=(1340, 785)),times=2)
        touch(Template(r"tpl1629634861823.png", record_pos=(0.166, 0.119), resolution=(746, 437)))
        touch(Template(r"tpl1629633570588.png", record_pos=(0.299, 0.029), resolution=(746, 437)),times=5)
        touch(Template(r"tpl1629633779575.png", record_pos=(-0.003, 0.109), resolution=(746, 437)))
        touch(Template(r"tpl1629633848407.png", record_pos=(0.007, 0.191), resolution=(746, 437)),times=2)
    else:
        touch(Template(r"tpl1629633461797.png", record_pos=(0.173, 0.116), resolution=(746, 437)))
        touch(Template(r"tpl1629633570588.png", record_pos=(0.299, 0.029), resolution=(746, 437)),times=2)
        touch(Template(r"tpl1629633779575.png", record_pos=(-0.003, 0.109), resolution=(746, 437)))
        touch(Template(r"tpl1629633848407.png", record_pos=(0.007, 0.191), resolution=(746, 437)),times=2)
swipe(Template(r"tpl1629785383125.png", record_pos=(-0.076, -0.008), resolution=(890, 522)), vector=[0.3809, 0.0])
swipe(Template(r"tpl1629785529395.png", record_pos=(-0.055, -0.026), resolution=(890, 522)), vector=[0.3315, -0.0057])



# touch(Template(r"tpl1629634758296.png", record_pos=(-0.129, -0.068), resolution=(746, 437)))
# touch(Template(r"tpl1629634766960.png", record_pos=(0.182, 0.149), resolution=(746, 437)))
# touch(Template(r"tpl1629634773215.png", record_pos=(0.162, 0.116), resolution=(746, 437)))
touch(Template(r"tpl1629634852520.png", record_pos=(-0.37, -0.072), resolution=(746, 437)))
if exists(Template(r"tpl1629687099656.png", record_pos=(0.055, 0.001), resolution=(1340, 785))):
    touch(Template(r"tpl1629687099656.png", record_pos=(0.055, 0.001), resolution=(1340, 785)),times=2)
    touch(Template(r"tpl1629634861823.png", record_pos=(0.166, 0.119), resolution=(746, 437)))
    touch(Template(r"tpl1629633570588.png", record_pos=(0.299, 0.029), resolution=(746, 437)),times=5)
    touch(Template(r"tpl1629633779575.png", record_pos=(-0.003, 0.109), resolution=(746, 437)))
    touch(Template(r"tpl1629633848407.png", record_pos=(0.007, 0.191), resolution=(746, 437)),times=2)
else:
    touch(Template(r"tpl1629634861823.png", record_pos=(0.166, 0.119), resolution=(746, 437)))
    touch(Template(r"tpl1629633570588.png", record_pos=(0.299, 0.029), resolution=(746, 437)),times=5)
    touch(Template(r"tpl1629633779575.png", record_pos=(-0.003, 0.109), resolution=(746, 437)))
    touch(Template(r"tpl1629633848407.png", record_pos=(0.007, 0.191), resolution=(746, 437)),times=2)

swipe(Template(r"tpl1629785653615.png", record_pos=(-0.076, -0.024), resolution=(890, 522)), vector=[0.3742, 0.0])

touch(Template(r"tpl1629635345017.png", record_pos=(0.016, -0.056), resolution=(746, 437)))
if exists(Template(r"tpl1629687099656.png", record_pos=(0.055, 0.001), resolution=(1340, 785))):
    touch(Template(r"tpl1629687099656.png", record_pos=(0.055, 0.001), resolution=(1340, 785)),times=2)
    touch(Template(r"tpl1629634861823.png", record_pos=(0.166, 0.119), resolution=(746, 437)))
    touch(Template(r"tpl1629633570588.png", record_pos=(0.299, 0.029), resolution=(746, 437)),times=5)
    touch(Template(r"tpl1629633779575.png", record_pos=(-0.003, 0.109), resolution=(746, 437)))
    touch(Template(r"tpl1629633848407.png", record_pos=(0.007, 0.191), resolution=(746, 437)),times=2)
else:
    touch(Template(r"tpl1629634861823.png", record_pos=(0.166, 0.119), resolution=(746, 437)))
    touch(Template(r"tpl1629633570588.png", record_pos=(0.299, 0.029), resolution=(746, 437)),times=5)
    touch(Template(r"tpl1629633779575.png", record_pos=(-0.003, 0.109), resolution=(746, 437)))
    touch(Template(r"tpl1629633848407.png", record_pos=(0.007, 0.191), resolution=(746, 437)),times=2)
touch(Template(r"tpl1629635647215.png", record_pos=(-0.295, -0.057), resolution=(746, 437)))
if exists(Template(r"tpl1629687099656.png", record_pos=(0.055, 0.001), resolution=(1340, 785))):
    touch(Template(r"tpl1629687099656.png", record_pos=(0.055, 0.001), resolution=(1340, 785)),times=2)
    touch(Template(r"tpl1629634861823.png", record_pos=(0.166, 0.119), resolution=(746, 437)))
    touch(Template(r"tpl1629633570588.png", record_pos=(0.299, 0.029), resolution=(746, 437)),times=5)
    touch(Template(r"tpl1629633779575.png", record_pos=(-0.003, 0.109), resolution=(746, 437)))
    touch(Template(r"tpl1629633848407.png", record_pos=(0.007, 0.191), resolution=(746, 437)),times=2)
else:
#     touch(Template(r"tpl1629783971450.png", record_pos=(-0.171, 0.116), resolution=(890, 522)))
    touch(Template(r"tpl1629634861823.png", record_pos=(0.166, 0.119), resolution=(746, 437)))
    touch(Template(r"tpl1629633570588.png", record_pos=(0.299, 0.029), resolution=(746, 437)),times=5)
    touch(Template(r"tpl1629633779575.png", record_pos=(-0.003, 0.109), resolution=(746, 437)))
    touch(Template(r"tpl1629633848407.png", record_pos=(0.007, 0.191), resolution=(746, 437)),times=2)
touch(Template(r"tpl1629644914203.png", record_pos=(0.373, -0.223), resolution=(746, 437)))
touch(Template(r"tpl1629644928311.png", record_pos=(0.452, -0.255), resolution=(746, 437)))
sleep(1.0)

