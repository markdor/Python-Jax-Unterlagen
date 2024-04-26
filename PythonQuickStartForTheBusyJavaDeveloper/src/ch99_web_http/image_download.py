import requests


response = requests.get("https://imgs.xkcd.com/comics/modern_tools.png")
print(response)
print(response.status_code)

with open("../ch99_web_http/modern_tools.png", "wb") as png_file:
    png_file.write(response.content)



