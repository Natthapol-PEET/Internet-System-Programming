import urllib.parse
import urllib.request
from faker import Faker

url = 'http://localhost/isp-wk4/register.php'

faker = Faker()

for i in range(10):
    values = {
        'email': faker.email(),
        'fullname': faker.name(),
        'address': faker.address()
    }
    # {'email': 'sarah65@brown.com', 'fullname': 'Carlos Howell', 'address': '313 Mcdonald Route\nBennettside, UT 50968'}
    # print(values)

    # email=sarah65%40brown.com&fullname=Carlos+Howell&address=313+Mcdonald+Route%0ABennettside%2C+UT+50968
    data = urllib.parse.urlencode(values)
    # print(data)

    # b'email=sarah65%40brown.com&fullname=Carlos+Howell&address=313+Mcdonald+Route%0ABennettside%2C+UT+50968'
    data = data.encode('ascii')
    # print(data)

    # <urllib.request.Request object at 0x000002B71D368908>
    req = urllib.request.Request(url, data)
    # print(req)

    with urllib.request.urlopen(req) as response:
        # b"<script type='text/javascript'>alert ('REGISTER SUCCESSFULLY WELCOME Carlos Howell');window.location='greeting.php';</script>"
        print(response.read())


