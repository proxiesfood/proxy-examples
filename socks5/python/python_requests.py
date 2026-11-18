# pip install requests[socks]
import requests

proxy = "socks5://USERNAME:PASSWORD@proxies.proxiesfood.com:81"
r = requests.get("https://icanhazip.com", proxies={"http": proxy, "https": proxy})
print(r.text)
