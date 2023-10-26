import sys
import subprocess

user_process = subprocess.Popen(["python3", "user.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, bufsize=1)
cloud_process = subprocess.Popen(["python3", "cloud.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, bufsize=1)

data = input()
user_process.stdin.write(data + '\n')
user_process.stdin.flush()
n = input()
user_process.stdin.write(n + '\n')
user_process.stdin.flush()

print('Sending to cloud -->')
cloud_process.stdin.write(data + '\n')
cloud_process.stdin.flush()

while True:
    command = input()
    if command == 'q':
        break
    user_process.stdin.write(command)
    user_process.stdin.flush()
    user_challenge = user_process.stdout.readline()
    cloud_process.stdin.write(user_challenge)
    cloud_response = cloud_process.stdout.readline()
    user_process.stdin.write(cloud_response)

cloud_process.stdin.close()
cloud_process.stdout.close()
cloud_process.terminate()
cloud_process.wait()
user_process.stdin.close()
user_process.stdout.close()
user_process.terminate()
user_process.wait()