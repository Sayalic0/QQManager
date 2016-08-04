#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json
from HTMLParser import HTMLParser

role_dict = {
    0: '群主',
    1: '管理员',
    2: '成员'
}

gender_dict = {
    0: '男',
    1: '女',
    255: '未知'
}


class QQUser:
    def __init__(self, qq, nick, memo, last_speak_time, join_time, gender, q_age, role):
        self.qq = qq
        self.nick = nick
        self.memo = memo
        self.last_speak_time = last_speak_time
        self.join_time = join_time
        self.gender = gender
        self.q_age = q_age
        self.role = role

    def __repr__(self):
        return str(self.qq) + ' ' + self.nick.encode('utf8')

class QQGroupManager:
    def __init__(self, group_number, bkn, cookie):
        self.cookie = cookie
        self.group_number = group_number
        self.parser = HTMLParser()
        self.bkn = bkn

    def get_member_list(self):
        r = requests.post('http://qun.qq.com/cgi-bin/qun_mgr/search_group_members', headers={
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': self.cookie,
            'Referer': 'http://qun.qq.com/member.html'
        }, data='gc=%s&st=0&end=500&sort=0&bkn=%s' % (self.group_number, self.bkn))

        post_ret = json.loads(r.text)
        if post_ret['ec'] != 0:
            return []
        ret = []
        for record in post_ret['mems']:
            qq_user = QQUser(record['uin'],
                             self.parser.unescape(record['nick']),
                             self.parser.unescape(record['card']),
                             record['last_speak_time'],
                             record['join_time'],
                             gender_dict[record['g']],
                             record['qage'],
                             role_dict[record['role']])
            ret.append(qq_user)
        return ret

    def del_qq_user(self, qq):
        r = requests.post('http://qun.qq.com/cgi-bin/qun_mgr/delete_group_member', headers={
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': self.cookie,
            'Referer': 'http://qun.qq.com/member.html'
        }, data='gc=%s&ul=%s&flag=0&bkn=%s' % (qq, self.group_number, self.bkn))
        if json.loads(r.text)[u'ec'] == 0:
            print 'del succ'
        else:
            print 'del failed'
