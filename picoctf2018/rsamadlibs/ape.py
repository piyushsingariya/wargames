import pwn

host, port = '2018shell.picoctf.com', 40440

s = pwn.remote(host, port)

s.sendline('y')
s.sendline(str(93187*94603))

s.sendline('y')
s.sendline(str())

