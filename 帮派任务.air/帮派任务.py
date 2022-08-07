# -*- encoding=utf8 -*-
__author__ = "86133"

from airtest.core.api import *

auto_setup(__file__)
touch(Template(r"tpl1629564549076.png", record_pos=(0.224, -0.25), resolution=(627, 369)))
pos = exists(Template(r"tpl1629629383596.png", record_pos=(-0.24, 0.264), resolution=(1340, 785)))


if pos:touch(pos)
touch(Template(r"tpl1629629457969.png", record_pos=(-0.285, -0.047), resolution=(1065, 785)))
sleep(30)
touch(Template(r"tpl1629630613913.png", record_pos=(0.358, 0.09), resolution=(746, 437)))
touch(Template(r"tpl1629630625666.png", record_pos=(0.357, 0.092), resolution=(746, 437)))
wait(Template(r"tpl1629630847422.png", record_pos=(0.212, 0.23), resolution=(746, 437)),timeout=500)
touch(Template(r"tpl1629630847422.png", record_pos=(0.212, 0.23), resolution=(746, 437)))
wait(Template(r"tpl1629631327945.png", record_pos=(0.338, 0.05), resolution=(746, 437)))
touch([610,367])

