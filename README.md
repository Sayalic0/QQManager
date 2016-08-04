## 使用方法

登录[QQ群管理首页](http://qun.qq.com/member.html)拿到Cookie,然后访问任意一个QQ群数据接口,拿到bkn。

利用bkn和Cookie初始化`QQGroupManager`:

```
manager = QQGroupManager('480394714', bkn, cookie) # 群号, bkn, cookie
```

访问群成员列表:

```
manager.get_member_list()
```

删除群成员:

```
manager.del_qq_user(qq) # 欲删除群成员qq号
```