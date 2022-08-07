# -*- encoding=utf8 -*-
__author__ = "86133"

from airtest.core.api import *

auto_setup(__file__)
count=0
while(count<999):
    try:
        touch(Template(r"tpl1629564549076.png", record_pos=(0.224, -0.25), resolution=(627, 369)))
        touch(Template(r"tpl1629639890467.png", record_pos=(0.417, 0.131), resolution=(746, 437)))
        wait(Template(r"tpl1629642650007.png", record_pos=(-0.131, -0.275), resolution=(746, 437)))
        
        while (not exists(Template(r"tpl1629640708691.png", record_pos=(-0.008, 0.243), resolution=(746, 437)))):
            attack=touch(Template(r"tpl1629639986880.png", record_pos=(0.398, 0.153), resolution=(746, 437)),times=2)
            run=touch(Template(r"tpl1629642795014.png", record_pos=(0.454, 0.057), resolution=(746, 437)))
        wait(Template(r"tpl1629640708691.png", record_pos=(-0.008, 0.243), resolution=(746, 437)))
