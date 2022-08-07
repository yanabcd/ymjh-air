# -*- encoding=utf8 -*-
__author__ = "86133"

from airtest.core.api import *

auto_setup(__file__)
touch(wait(Template(r"tpl1629713584157.png", record_pos=(0.456, -0.142), resolution=(1340, 785)))

,timeout=1000)

if exists(Template(r"tpl1629713659612.png", record_pos=(0.334, -0.012), resolution=(1340, 785))):
    touch(Template(r"tpl1629713659612.png", record_pos=(0.334, -0.012), resolution=(1340, 785)))
    touch(Template(r"tpl1629716891963.png", record_pos=(-0.361, 0.195), resolution=(1022, 598)))
    touch(Template(r"tpl1629716909219.png", record_pos=(-0.092, 0.154), resolution=(1022, 598)))
    touch(Template(r"tpl1629716937979.png", record_pos=(0.297, 0.027), resolution=(1022, 598)))
touch(Template(r"tpl1629716944927.png", record_pos=(0.258, -0.142), resolution=(1022, 598)))
touch(Template(r"tpl1629716952541.png", record_pos=(0.452, -0.262), resolution=(1022, 598)))

