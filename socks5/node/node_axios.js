// npm i axios socks-proxy-agent
const axios = require("axios");
const { SocksProxyAgent } = require("socks-proxy-agent");

const agent = new SocksProxyAgent("socks5://USERNAME:PASSWORD@proxies.proxiesfood.com:81");
axios.get("https://icanhazip.com", { httpAgent: agent, httpsAgent: agent })
    .then(r => console.log(r.data));
