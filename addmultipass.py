import subprocess, time

for i in range(3):
  subprocess.run(['multipass', 'launch', '-c' '2', '-m' '2G', '-d' '10G', '-n', f"server{i}" ])  