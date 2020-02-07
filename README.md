# Xor_decrypt
XOR decryption script for decrypting  the firmware..When reverseengineering IOT device firmwares
 
 USAGE:cat encrypted.bin | python XOR_decryption.py > decrypted.bin
 
To get the decryption key you to simply perform a hexdump and see if there
are any recurring strings.And then modify line 
