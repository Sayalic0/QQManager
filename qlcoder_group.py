#!/usr/bin/env python
# -*- coding: utf-8 -*-

from qq_manager import QQGroupManager

cookie = ''
bkn = ''
manager = QQGroupManager('480394714', bkn, cookie)

print manager.get_member_list()