# -*- encoding=utf8 -*-
__author__ = "86133"

from airtest.core.api import *

auto_setup(__file__)
touch(Template(r"tpl1629564549076.png", record_pos=(0.224, -0.25), resolution=(627, 369)))
touch(Template(r"tpl1658292441201.png", record_pos=(-0.097, -0.068), resolution=(1118, 797)))

wait(Template(r"tpl1658292519669.png", record_pos=(-0.359, -0.133), resolution=(1352, 797))
,timeout=100)
while (exists(Template(r"tpl1658292519669.png", record_pos=(-0.359, -0.133), resolution=(1352, 797)))):
    attack=touch(Template(r"tpl1629709461697.png", record_pos=(0.412, 0.161), resolution=(1317, 785)),times=2)


    run=touch(Template(r"tpl1629709390363.png", record_pos=(0.46, 0.054), resolution=(1340, 785)),times=1)
    if (exists(Template(r"tpl1658294666960.png", record_pos=(0.297, -0.079), resolution=(1352, 797)))

):
        sleep(8)
        touch(Template(r"tpl1658293531139.png", record_pos=(0.438, 0.218), resolution=(1352, 797)))
        

# touch(wait(Template(r"tpl1629710727929.png", record_pos=(0.31, 0.028), resolution=(1322, 785))
# ,timeout=1000))