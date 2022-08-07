# -*- encoding=utf8 -*-
__author__ = "86133"

from airtest.core.api import *

auto_setup(__file__)
count=0
while(count<999):
    try: 
        touch(Template(r"tpl1630045904970.png", record_pos=(0.225, 0.096), resolution=(1340, 785)))

        sleep(18)
    
    except:
        print('没有斧子了')
    if exists(Template(r"tpl1630006315106.png", record_pos=(0.228, 0.093), resolution=(1340, 785))):
        touch(Template(r"tpl1630006315106.png", record_pos=(0.228, 0.093), resolution=(1340, 785)))
        touch(Template(r"tpl1630045889474.png", record_pos=(0.196, 0.018), resolution=(1340, 785)))
