# -*- encoding=utf8 -*-
__author__ = "86133"

from airtest.core.api import *

auto_setup(__file__)
counter=0;
while(counter<9999):
    touch(Template(r"tpl1633009947880.png", record_pos=(0.226, -0.264), resolution=(1340, 785)))
    touch(Template(r"tpl1633012163006.png", record_pos=(-0.181, 0.119), resolution=(1340, 785)))

    sleep(30)

    while (not exists(Template(r"tpl1633011201480.png", record_pos=(0.225, -0.263), resolution=(1340, 785)))):
        attack=touch(Template(r"tpl1633007812459.png", record_pos=(0.381, 0.147), resolution=(1340, 785)),times=2)


        run=touch(Template(r"tpl1633007832503.png", record_pos=(0.454, 0.054), resolution=(1340, 785)),times=1)

    #touch(wait(Template(r"tpl1629710727929.png", record_pos=(0.31, 0.028), resolution=(1322, 785))
    #,timeout=1000))