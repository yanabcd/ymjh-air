# -*- encoding=utf8 -*-
__author__ = "86133"

from airtest.core.api import *

auto_setup(__file__)
touch(Template(r"tpl1629613507408.png", record_pos=(0.256, -0.27), resolution=(873, 530)))
pos = exists(Template(r"tpl1629613597800.png", record_pos=(-0.341, 0.275), resolution=(873, 530)))

if pos:touch(pos)
touch(Template(r"tpl1629613667578.png", record_pos=(-0.345, -0.09), resolution=(873, 530))) or touch

touch(Template(r"tpl1629564605219.png", record_pos=(-0.28, 0.127), resolution=(627, 369)))
wait((Template(r"tpl1629613786156.png", record_pos=(0.355, 0.09), resolution=(910, 530))),timeout=120,interval=3)
touch(Template(r"tpl1629564640618.png", record_pos=(0.369, 0.089), resolution=(627, 369)))
touch(Template(r"tpl1629614336480.png", record_pos=(0.356, 0.088), resolution=(910, 530)))

touch([313,172])
sleep(18.0)
pos1=assert_not_exists(Template(r"tpl1629615068108.png", record_pos=(-0.442, -0.166), resolution=(910, 530)), "不存在观梦")
if pos1:touch(Template(r"tpl1629615248321.png", record_pos=(0.279, 0.015), resolution=(910, 530)))
click(1762,512)