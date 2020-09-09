#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:26:30 2019

@author: sunny
"""


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64decode

print ("hello")
key = open("/path/to/keyPair/key.pem").read()
key = key.replace("-----BEGIN RSA PRIVATE KEY-----", "").replace("-----END RSA PRIVATE KEY-----", "").replace("\n", "")
key = b64decode(key)
key = RSA.importKey(key)

inputString = 'RyGR3vB6v8hl3ITN5H9tm3sxNQZnZGxOWMIL0V8s7VIQZgUhGonRAVnDKe5KHH9aB8KynoLaLUn5/baNqfC9EiynOLqS7CxNPTY28UT1kxchGQ/YX3yaw7AUBZeNmEKUBD5JOQD3VNaKbrgosnhaVK6bNzjlGyyhZrDpBlx2tX+h057b0ecZTPHHhJUwkjAmBMsSTwTUJqwzzCNARDpHCS4o2qt23XYJNmw5UidPJ2JURt45YUEUovPmzDSdmS/5V9fxbcCMpdwZJa5d2tLhzpcjdmUM6tiQNu4DUqwF4ICYxZmX9Za74Niu9fTTy4+C0jY1uUd8o8Y9g0tvamCBwQ=='

cipher = PKCS1_v1_5.new(key)
plainText = cipher.decrypt(b64decode(inputString), "Error decrypting the input string!")

print(plainText)