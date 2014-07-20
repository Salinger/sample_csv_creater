#!/usr/bin/env python
# -*-coding: utf-8 -*-

import random
import sys


def create_dataset():
    n = int(sys.argv[1])
    print "user_id,action,item_type,payment"
    for i in range(n):
        user_id, action, item_type, payment = create_recode()
        print "%s,%s,%s,%s" % (user_id, action, item_type, payment)
    return


def create_recode():
    user_id = random.randint(1, 100000)
    action = random.randint(100, 10000)
    item_type = random.randint(0, 4)
    if item_type == 0:
        payment = random.randint(100, 500)
    elif item_type == 1:
        payment = random.randint(50, 100)
    elif item_type == 2:
        payment = random.randint(1000, 5000)
    elif item_type == 3:
        payment = random.randint(300, 10000)
    elif item_type == 4:
        payment = random.randint(10000, 20000)
    else:
        payment = 0
    return [user_id, action, item_type, payment]


def parse_recode(l):
    return

create_dataset()
