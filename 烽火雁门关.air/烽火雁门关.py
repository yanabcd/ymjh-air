# -*- encoding=utf8 -*-
__author__ = "86133"

from airtest.core.api import *

auto_setup(__file__)
while not exists(Template(r"tpl1658292519669.png", record_pos=(-0.359, -0.133), resolution=(1352, 797))):

    touch(Template(r"tpl1658560220827.png", record_pos=(0.226, -0.268), resolution=(1352, 797)))
#     if exists(Template(r"tpl1658292441201.png", record_pos=(-0.097, -0.068), resolution=(1118, 797))):

#         touch(Template(r"tpl1658292441201.png", record_pos=(-0.097, -0.068), resolution=(1118, 797)))
    if exists(Template(r"tpl1658930748777.png", record_pos=(-0.162, -0.069), resolution=(1352, 797))):
        touch(Template(r"tpl1658930923801.png", record_pos=(-0.163, -0.059), resolution=(1352, 797)))



    wait(Template(r"tpl1658292519669.png", record_pos=(-0.359, -0.133), resolution=(1352, 797))
    ,timeout=10000)
    while (exists(Template(r"tpl1658292519669.png", record_pos=(-0.359, -0.133), resolution=(1352, 797)))):
        try:
            attack=touch(Template(r"tpl1629639986880.png", record_pos=(0.398, 0.153), resolution=(746, 437)),times=1)
            sleep(5)
        except:

            if (exists(Template(r"tpl1658294666960.png", record_pos=(0.297, -0.079), resolution=(1352, 797)))):
                touch(Template(r"tpl1658293531139.png", record_pos=(0.438, 0.218), resolution=(1352, 797)))
        try:
            run=touch(Template(r"tpl1629642795014.png", record_pos=(0.454, 0.057), resolution=(746, 437)))
            sleep(5)
    #         if exists(Template(r"tpl1658927234452.png", record_pos=(-0.462, -0.261), resolution=(1352, 797))):


        except:
            if (exists(Template(r"tpl1658294666960.png", record_pos=(0.297, -0.079), resolution=(1352, 797)))):
                touch(Template(r"tpl1658293531139.png", record_pos=(0.438, 0.218), resolution=(1352, 797)))
