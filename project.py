import http.client

conn = http.client.HTTPSConnection("goodreads12.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "01abf95d02msh2e6435276d913b5p178d14jsnc481249351a4",
    'x-rapidapi-host': "goodreads12.p.rapidapi.com"
}

conn.request("GET", "/getAuthorBooks", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))