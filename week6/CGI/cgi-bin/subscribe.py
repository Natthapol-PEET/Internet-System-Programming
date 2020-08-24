import cgi

form = cgi.FieldStorage()

name = form.getvalue('name')
email = form.getvalue('email')

print("Status: 200 OK")
print("Content-type: text/html")
print()
print("<html><head><title>Success!</title></head><body><h1>")
print("Hello %s" % (name))
print("<br>")
print("Your email is %s" % email)
print("</h1></body>")
