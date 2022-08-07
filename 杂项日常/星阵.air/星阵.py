# -*- encoding=utf8 -*-
__author__ = "86133"

from airtest.core.api import *

auto_setup(__file__)
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