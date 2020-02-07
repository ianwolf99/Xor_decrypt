import os
import sys
key = "key-here".decode("hex")
data = sys.stdin.read()
r = ""
for i in range(len(data)):
     c = chr(ord(data[i]) ^ ord(key[i % len(key)]))
      r += c
sys.stdout.write(r)