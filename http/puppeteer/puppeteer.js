// npm i puppeteer
const puppeteer = require("puppeteer");

(async () => {
    const browser = await puppeteer.launch({ args: ["--proxy-server=http://proxies.proxiesfood.com:81"] });
    const page = await browser.newPage();
    await page.authenticate({ username: "USERNAME", password: "PASSWORD" });
    await page.goto("https://icanhazip.com");
    console.log(await page.evaluate(() => document.body.innerText));
    await browser.close();
})();
