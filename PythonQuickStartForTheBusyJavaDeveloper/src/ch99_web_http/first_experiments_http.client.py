# https://docs.python.org/3/library/http.client.html
import http.client

h1 = http.client.HTTPConnection('www.python.org')
h2 = http.client.HTTPConnection('www.python.org:80')
h3 = http.client.HTTPConnection('www.python.org', 80)
h4 = http.client.HTTPConnection('www.python.org', 80, timeout=10)

print(h1)

print(h1.request("GET", "/"))
# print(h1.getresponse())
print(h1.getresponse().read())


def print_response_info(response):
    print(response.status, response.reason)
    print(response.read())


# Problem mit Https
httpconn = http.client.HTTPConnection('reqres.in')
# => 301 Moved Permanentyly
print(httpconn.request("GET", "/api/users?page=2"))
print_response_info(httpconn.getresponse())