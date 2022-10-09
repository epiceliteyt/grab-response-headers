import requests
import os
import sys

url = "https://api.github.com/users/a"

sys.stdout = open("response.txt", "w")

try:
    response = requests.head(url)
except Exception as e:
    print(f"NOT OK: {str(e)}")
else:
    if response.status_code == 200:
        print(url + " : ONLINE")
        sys.stdout.close()
        cmd = os.system('curl ' + url + " > output.txt")
    else:
        print(url + f"   NOT OK: HTTP response code {response.status_code}")
        

