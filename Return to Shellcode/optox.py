with open("hmexecve32.bin", "rb") as f:
    byte_content = f.read()

formatted_opcodes = ''.join(f'\\x{byte:02x}' for byte in byte_content)
print(formatted_opcodes)
