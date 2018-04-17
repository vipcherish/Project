#!/usr/bin/python
#-*- coding:utf-8 -*-
# username = input('alex')
# pw=input('123456')
# if username=='alex' and pw=='123456':
#     print(ok)
# else:
#     print(err)
#
i=0
while i<3:
    user=input('username:')
    pw=input('password:')
    if user=="alex" and pw=="123456":
        print('success')
        break
    else:
        print('retry')
        i=i+1