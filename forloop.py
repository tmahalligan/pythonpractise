import subprocess

for i in range(3):
  subprocess.Popen(['echo', 'multipass', 'launch', '-c 2', '-m 2G', '-d 10G', '-n ' f"server{i}"])  
  