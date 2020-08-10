import urllib.request as ur
import urllib.parse as up

url = 'http://localhost/Register/register_post.php'

value = {
    'name': 'PEET',
    'location': '7-225',
    'language': 'Python'
}

data = up.urlencode(value)
data = data.encode('ascii')

req = ur.Request(url, data)

with ur.urlopen(req) as res:
    data_read = res.read()
    print(data_read.decode('ascii'))