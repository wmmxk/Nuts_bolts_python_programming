import subprocess

bash_cmd = 'ls'
res = subprocess.check_output(bash_cmd, shell=True) 
res = res.rstrip()
print(res)
