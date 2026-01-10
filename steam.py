#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hmac, time, base64, hashlib

code = ''
char = '23456789BCDFGHJKMNPQRTVWXY'

hex_time = ('%016x' % (int(time.time()) // 30))
byte_time = bytes.fromhex(hex_time)

digest = hmac.new(base64.b32decode('E743CHKDEA44APEGLSDIUT2N4OY5NXTQ'), byte_time, hashlib.sha1).digest()
begin = ord(digest[19:20]) & 0xF
c_int = int.from_bytes((digest[begin:begin + 4]), "big") & 0x7fffffff

for r in range(5):
    code += char[int(c_int) % len(char)]
    c_int /= len(char)
print(code)
