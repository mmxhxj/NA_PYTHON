import subprocess
import sys

HOST="root@192.168.113.176"
# Ports are handled in ~/.ssh/config since we use OpenSSH
COMMAND="uname -a"

ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#result = ssh.stdout.readlines()
result = ssh.communicate()

if result == []:
    error = ssh.stderr.readlines()
    print >>(sys.stderr, "ERROR: %s" % error)
else:
    print (result)