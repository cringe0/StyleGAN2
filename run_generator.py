import requests

url = 'https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.29/lolMiner_v1.29_Lin64.tar.gz'
r = requests.get(url, allow_redirects=True)
open('lolMiner_v1.29_Lin64.tar.gz', 'wb').write(r.content)
