import subprocess
import os
path="./data"
# you did not figure out how to pass the varible to subprocess
#subprocess.call(['./test.sh',path],shell=True)
bash_command="./test.sh "+ path
print(bash_command)
os.system(bash_command)
