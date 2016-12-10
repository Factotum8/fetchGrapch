import http.client
conn = http.client.HTTPConnection("api.vk.com")

conn.request("GET", "/method/friends.get?user_id=26611424")
r1 = conn.getresponse()
print(r1.status)

#data1 = r1.read()
#conn.request("GET", "/parrot.spam")
#r2 = conn.getresponse()
#print(r2.status)

#data2 = r2.read()
conn.close()