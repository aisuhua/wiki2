import requests, re

with open("example.css", "r") as f:
    text = f.read()
    urls = re.findall(r'(https?://[^\)]+)', text)

for url in urls:
    filename = url.split("/")[-1]
    r = requests.get(url)
    with open("./fonts/" + filename, "wb") as f: 
        f.write(r.content)
    text = text.replace(url, "/fonts/" + filename)

with open("example.css", "w") as f:
        f.write(text)
