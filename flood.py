import subprocess
import atexit
import signal
import sys
import os

idval = []
n = 50

for x in range(n):
    process = subprocess.Popen(args=["tilix", "--command=python signup.py"])
    idval.append(process.pid)

print(idval)

while process:
    try:
        print("Still Running")

    except:
        process = False
        print(idval)
        # for item in idval:
            # os.killpg(int(item), signal.SIGKILL)
            # os.system('pkill -TERM -P {item}'.)

        print("Stopped Running")

