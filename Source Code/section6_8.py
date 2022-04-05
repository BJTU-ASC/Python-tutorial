# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2022 BJTU Academic Support Centre. All Rights Reserved
#
################################################################################

events = [1917, 1848, 1789, 1871, 1524, 1861]
if 1848 in events:
    print(events.index(1848))


events = [1917, 1848, 1789, 1871, 1524, 1861]
del events[3:]
print(events)
