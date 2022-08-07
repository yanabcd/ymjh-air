# -*- encoding=utf8 -*-
__author__ = "86133"

from airtest.core.api import *

auto_setup(__file__)
count=0
while(count<999):
    try: 
        touch(Template(r"tpl1630002486175.png", record_pos=(0.227, 0.094), resolution=(1340, 785)))
        sleep(18)
    
    except:
        print('没有铲子了')
    if exists(Template(r"tpl1630006315106.png", record_pos=(0.228, 0.093), resolution=(1340, 785))):
        touch(Template(r"tpl1630006315106.png", record_pos=(0.228, 0.093), resolution=(1340, 785)))
        touch(Template(r"tpl1630006347490.png", record_pos=(0.125, 0.018), resolution=(1340, 785)))


        



