# pip install requests
# https://www.datacamp.com/community/tutorials/making-http-requests-in-python
# https://httpbin.org/

# https://docs.python-requests.org/en/master/
# https://www.nylas.com/blog/use-python-requests-module-rest-apis/
# https://lerneprogrammieren.de/python-http-requests-tutorial/
# https://www.w3schools.com/python/module_requests.asp

import requests


def print_response_info(address):
    response = requests.get(address)
    print(response)
    print(response.status_code)
    print(response.headers)
    print(response.text)

    with open("../ch99_web_http/python.html", "w") as html_file:
        html_file.write(response.text)


print_response_info('https://reqres.in/api/users?page=2')
print_response_info("https://www.python.org/")

