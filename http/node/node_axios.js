// npm i axios https-proxy-agent
const axios = require("axios");
const { HttpsProxyAgent } = require("https-proxy-agent");

const agent = new HttpsProxyAgent("http://USERNAME:PASSWORD@proxies.proxiesfood.com:81");
axios.get("https://icanhazip.com", { httpsAgent: agent, proxy: false })
    .then(r => console.log(r.data));
