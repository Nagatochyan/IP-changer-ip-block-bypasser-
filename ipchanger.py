import subprocess
import requests
import time

proxies = {
        'http':'socks5://127.0.0.1:9050',
        'https':'socks5://127.0.0.1:9050'
        }

while True:
    cmd = r'path to the tor.exe'
    olas = subprocess.Popen(cmd, shell=False)
    responce = requests.get('URL', proxies=proxies).json()
    print(responce)
    olas.kill()
    time.sleep(10)
