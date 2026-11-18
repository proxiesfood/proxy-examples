# pip install requests
import requests

proxy = "http://USERNAME:PASSWORD@proxies.proxiesfood.com:81"
r = requests.get("https://icanhazip.com", proxies={"http": proxy, "https": proxy})
print(r.text)
