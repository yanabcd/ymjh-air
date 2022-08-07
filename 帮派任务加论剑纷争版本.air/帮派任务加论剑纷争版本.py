# -*- encoding=utf8 -*-
__author__ = "86133"

from airtest.core.api import *

auto_setup(__file__)
#开始帮派按任务
touch(Template(r"tpl1629564549076.png", record_pos=(0.224, -0.25), resolution=(627, 369)))
pos1 = exists(Template(r"tpl1629629383596.png", record_pos=(-0.24, 0.264), resolution=(1340, 785)))


if pos1:touch(pos1)
touch(Template(r"tpl1629629457969.png", record_pos=(-0.285, -0.047), resolution=(1065, 785)))
sleep(30)
touch(wait(Template(r"tpl1629630613913.png", record_pos=(0.358, 0.09), resolution=(746, 437)),timeout=500))
touch(Template(r"tpl1629630625666.png", record_pos=(0.357, 0.092), resolution=(746, 437)))
wait(Template(r"tpl1629630847422.png", record_pos=(0.212, 0.23), resolution=(746, 437)),timeout=500)
touch(Template(r"tpl1629630847422.png", record_pos=(0.212, 0.23), resolution=(746, 437)))
touch(wait(Template(r"tpl1629631327945.png", record_pos=(0.338, 0.05), resolution=(746, 437)),timeout=200))
touch(wait(Template(r"tpl1629689580945.png", record_pos=(-0.346, 0.22), resolution=(1322, 785)),timeout=200))
sleep(1.0)
#前往江南
touch(Template(r"tpl1629564549076.png", record_pos=(0.224, -0.25), resolution=(627, 369)))
if exists(Template(r"tpl1629802174949.png", record_pos=(0.085, 0.264), resolution=(1272, 746))):
    touch(Template(r"tpl1629802174949.png", record_pos=(0.085, 0.264), resolution=(1272, 746)))
    touch(Template(r"tpl1629802209271.png", record_pos=(-0.363, 0.131), resolution=(1272, 746)))
    touch(Template(r"tpl1629802239330.png", record_pos=(0.252, -0.035), resolution=(1272, 746)))
     wait(Template(r"tpl1629802309637.png", record_pos=(0.469, -0.27), resolution=(1272, 746)))



else:
    touch(Template(r"tpl1629802209271.png", record_pos=(-0.363, 0.131), resolution=(1272, 746)))

touch(Template(r"tpl1629792051747.png", record_pos=(0.468, -0.268), resolution=(979, 574)))
touch(Template(r"tpl1629802239330.png", record_pos=(0.252, -0.035), resolution=(1272, 746)))
     wait(Template(r"tpl1629802309637.png", record_pos=(0.469, -0.27), resolution=(1272, 746)))

#前往剑冢，烽火等
#生死剑冢三次
if exists(Template(r"tpl1629564549076.png", record_pos=(0.224, -0.25), resolution=(627, 369))):
    touch(Template(r"tpl1629564549076.png", record_pos=(0.224, -0.25), resolution=(627, 369)))
pos = exists(Template(r"tpl1629566720355.png", record_pos=(-0.128, 0.266), resolution=(627, 369)))
if pos:
    touch(pos)
    touch(Template(r"tpl1629637856824.png", record_pos=(0.223, -0.057), resolution=(746, 437)))
    touch(Template(r"tpl1629637907803.png", record_pos=(0.338, 0.171), resolution=(746, 437)))
    touch(wait(Template(r"tpl1629638449338.png", record_pos=(-0.131, 0.113), resolution=(746, 437)),timeout=3000000))
    touch(Template(r"tpl1629564549076.png", record_pos=(0.224, -0.25), resolution=(627, 369)))
    if pos:touch(pos)
    touch(Template(r"tpl1629637856824.png", record_pos=(0.223, -0.057), resolution=(746, 437)))
    touch(Template(r"tpl1629637907803.png", record_pos=(0.338, 0.171), resolution=(746, 437)))
    touch(wait(Template(r"tpl1629638449338.png", record_pos=(-0.131, 0.113), resolution=(746, 437)),timeout=300000))
    touch(Template(r"tpl1629564549076.png", record_pos=(0.224, -0.25), resolution=(627, 369)))
    if pos:
        touch(pos)
        touch(Template(r"tpl1629637856824.png", record_pos=(0.223, -0.057), resolution=(746, 437)))
        touch(Template(r"tpl1629637907803.png", record_pos=(0.338, 0.171), resolution=(746, 437)))
        touch(wait(Template(r"tpl1629638449338.png", record_pos=(-0.131, 0.113), resolution=(746, 437)),timeout=300000))
        sleep(3)
#逐鹿雁门关
touch(Template(r"tpl1629564549076.png", record_pos=(0.224, -0.25), resolution=(627, 369)))
if exists(Template(r"tpl1629639890467.png", record_pos=(0.417, 0.131), resolution=(746, 437))):
    touch(Template(r"tpl1629639890467.png", record_pos=(0.417, 0.131), resolution=(746, 437)))
    wait(Template(r"tpl1629642650007.png", record_pos=(-0.131, -0.275), resolution=(746, 437)))
    while (not exists(Template(r"tpl1629640708691.png", record_pos=(-0.008, 0.243), resolution=(746, 437)))):
        attack=touch(Template(r"tpl1629639986880.png", record_pos=(0.398, 0.153), resolution=(746, 437)),times=2)
        run=touch(Template(r"tpl1629642795014.png", record_pos=(0.454, 0.057), resolution=(746, 437)))

    touch(wait((Template(r"tpl1629640708691.png", record_pos=(-0.008, 0.243), resolution=(746, 437))),timeout=1000))
