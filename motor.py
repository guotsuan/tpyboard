#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 gq <gq@imac.lan>
#
# Distributed under terms of the MIT license.

"""
manupilate motor
"""
from crc16modbus import crc16, crc16add
from binascii import unhexlify

cmd_head = '3e'


def motor_getinfo(cmd_sn='00', devid='01'):
    cmd = '0a' # ask for the information
    length = '00'

    order = cmd_head + cmd_sn + devid + cmd + length

    order_full = crc16add(order)

    print(order_full)

    return unhexlify(order_full)






