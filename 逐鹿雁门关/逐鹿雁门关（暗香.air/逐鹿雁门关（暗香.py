# -*- encoding=utf8 -*-
__author__ = "86133"

from airtest.core.api import *

auto_setup(__file__)
touch(Template(r"tpl1629564549076.png", record_pos=(0.224, -0.25), resolution=(627, 369)))
touch(Template(r"tpl1629639890467.png", record_pos=(0.417, 0.131), resolution=(746, 437)))
wait(Template(r"tpl1629642650007.png", record_pos=(-0.131, -0.275), resolution=(746, 437)),timeout=50)
while (not exists(Template(r"tpl1629640708691.png", record_pos=(-0.008, 0.243), resolution=(746, 437)))):
    attack=touch(Template(r"tpl1629709461697.png", record_pos=(0.412, 0.161), resolution=(1317, 785)),times=2)


    run=touch(Template(r"tpl1629709390363.png", record_pos=(0.46, 0.054), resolution=(1340, 785)),times=1)

touch(wait(Template(r"tpl1629710727929.png", record_pos=(0.31, 0.028), resolution=(1322, 785))
,timeout=1000))