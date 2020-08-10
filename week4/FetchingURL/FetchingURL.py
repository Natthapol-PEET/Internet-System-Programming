import urllib.request as ur
import urllib.parse as up

with ur.urlopen('http://www.python.org/') as f:
    data = f.read(300)
    print(data)
