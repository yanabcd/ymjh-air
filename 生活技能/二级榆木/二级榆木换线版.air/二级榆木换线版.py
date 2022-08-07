# -*- encoding=utf8 -*-
__author__ = "86133"

from airtest.core.api import *

auto_setup(__file__)
count=0
while(count<999):
    try: 
        touch(Template(r"tpl1630047218988.png", record_pos=(0.226, 0.09), resolution=(1340, 785)))

        sleep(8)
        touch(Template(r"tpl1630046340835.png", record_pos=(0.382, -0.256), resolution=(1340, 785)))
        touch(Template(r"tpl1630046343601.png", record_pos=(0.33, -0.183), resolution=(1340, 785)))
        touch(Template(r"tpl1630047218988.png", record_pos=(0.226, 0.09), resolution=(1340, 785)))
        sleep(8)
        touch(Template(r"tpl1630046356806.png", record_pos=(0.386, -0.256), resolution=(1340, 785)))
        touch(Template(r"tpl1630046358065.png", record_pos=(0.311, -0.235), resolution=(1340, 785)))
        touch(Template(r"tpl1630047218988.png", record_pos=(0.226, 0.09), resolution=(1340, 785)))
        
    except:
        print('没有斧子了')
    


    if exists(Template(r"tpl1630006315106.png", record_pos=(0.228, 0.093), resolution=(1340, 785))):
        touch(Template(r"tpl1630006315106.png", record_pos=(0.228, 0.093), resolution=(1340, 785)))

