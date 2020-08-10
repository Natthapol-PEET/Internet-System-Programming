import urllib.request as ur
import urllib.parse as up

data = {}
data['name'] = 'PEET'
data['location'] = '7-225'
data['language'] = 'Python'

url_values = up.urlencode(data)

print(url_values)

url = 'http://localhost/Register/register_get.php'

full_url = url + '?' + url_values

data = ur.urlopen(full_url)
data = data.read()
print(data.decode('ascii'))