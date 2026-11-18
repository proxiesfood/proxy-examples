# ProxiesFood proxy examples

Code examples for [ProxiesFood](https://proxiesfood.com) unlimited residential and datacenter proxies: cURL, Python,
Node.js, PHP, Go, Java, C#, Scrapy, Puppeteer, Playwright and Selenium, over HTTP(S) and SOCKS5.

Every plan uses one host and port:

```
proxies.proxiesfood.com:81
```

HTTP(S) and SOCKS5 run on the same port with the same username and password. Replace `USERNAME` and `PASSWORD`
in the examples with the login from your [dashboard](https://proxiesfood.com/dashboard).

## Quick test

```sh
curl -x "http://USERNAME:PASSWORD@proxies.proxiesfood.com:81" https://icanhazip.com
```

Run it twice: each request leaves from a new IP.

## Username options

Add options to the end of the username. They work the same over HTTP(S) and SOCKS5.

| Option | Example | What it does |
|---|---|---|
| Rotating | `USERNAME` | A new IP on every request |
| Country | `USERNAME-country-US` | IPs from one country (two-letter code) |
| Sticky session | `USERNAME-session-a1b2c3-time-10m` | The same IP for the time set, up to 24 hours (`s`, `m` or `h`) |
| Fast pool | `USERNAME-pool-fast` | Only IPs that answer in under 1000 ms (unlimited residential) |
| Together | `USERNAME-pool-fast-country-US-session-a1b2c3-time-10m` | All of the above |

A new session name gives a new IP.

## Examples

| Language or tool | HTTP(S) | SOCKS5 |
|---|---|---|
| cURL | [http/curl](http/curl/curl.sh) | [socks5/curl](socks5/curl/curl.sh) |
| Python (requests) | [http/python](http/python/python_requests.py) | [socks5/python](socks5/python/python_requests.py) |
| Node.js (axios) | [http/node](http/node/node_axios.js) | [socks5/node](socks5/node/node_axios.js) |
| PHP (cURL) | [http/php](http/php/php_curl.php) | [socks5/php](socks5/php/php_curl.php) |
| Go | [http/go](http/go/main.go) | [socks5/go](socks5/go/main.go) |
| Java | [http/java](http/java/Main.java) | |
| C# | [http/csharp](http/csharp/Program.cs) | [socks5/csharp](socks5/csharp/Program.cs) |
| Scrapy | [http/scrapy](http/scrapy/scrapy_spider.py) | |
| Puppeteer | [http/puppeteer](http/puppeteer/puppeteer.js) | |
| Playwright | [http/playwright](http/playwright/playwright.py) | |
| Selenium (SeleniumBase) | [http/selenium](http/selenium/selenium.py) | |

Browsers and Scrapy use the HTTP side.

## Plans

- **Unlimited residential:** priced by speed, 100 Mbps to 1 Gbps, no GB or thread limit, 40M+ IPs in 200+ countries.
- **Unlimited datacenter:** 1,000 to 30,000 threads, no GB limit, 50K+ IPs.
- **Bandwidth residential:** by the GB, from $0.20 per GB.

Prices: [proxiesfood.com](https://proxiesfood.com). Free trial: [@proxiesfoodbot](https://t.me/proxiesfoodbot) on Telegram.
Guides: [proxiesfood.com/help](https://proxiesfood.com/help).

## Support

Telegram [@proxiesfoodsupport](https://t.me/proxiesfoodsupport)

## License

MIT
