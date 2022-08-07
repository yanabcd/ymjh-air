# -*- encoding=utf8 -*-
__author__ = "86133"

from airtest.core.api import *

auto_setup(__file__)
touch(Template(r"tpl1632816963111.png", record_pos=(0.236, -0.256), resolution=(1340, 785)))
touch(Template(r"tpl1632816966772.png", record_pos=(-0.172, 0.123), resolution=(1340, 785)))
while (not exists(Template(r"tpl1629640708691.png", record_pos=(-0.008, 0.243), resolution=(746, 437)))):
    attack=touch(Template(r"tpl1629709461697.png", record_pos=(0.412, 0.161), resolution=(1317, 785)),times=2)


    run=touch(Template(r"tpl1629709390363.png", record_pos=(0.46, 0.054), resolution=(1340, 785)),times=1)

touch(wait(Template(r"tpl1629710727929.png", record_pos=(0.31, 0.028), resolution=(1322, 785))
,timeout=1000))