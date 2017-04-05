__author__ = 'kaniu'

# the code here should be executed line by line 

import http.client

conn = http.client.HTTPConnection("www.google.com", 80)
conn.connect()
conn.request("GET", "/index.html")

response = conn.getresponse()
print(response.status, response.reason)

read_data = response.read()
print(read_data)

conn.close()
