
print("******************************************")
print("********Xor_decrypt_script****************")
print("*******Authored by ianwolf99**************")
print("******************************************")

#import the sys and os modules
import os
import sys
key = "key-here".decode("hex")
data = sys.stdin.read()
r = ""
for i in range(len(data)):
     c = chr(ord(data[i]) ^ ord(key[i % len(key)]))
     r = c
sys.stdout.write(r)
