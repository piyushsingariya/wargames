import requests
import re

username = 'natas6'
password = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"

# headers = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}
#cookies = {'loggedin': "1"}
url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url + "includes/secret.in", auth = (username, password))
content = response.text

#print(session.cookies)

print (content)

#print (re.findall('The password for %s is (.*)', content)[0])