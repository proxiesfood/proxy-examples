using System.Net;

var proxy = new WebProxy("socks5://proxies.proxiesfood.com:81") { Credentials = new NetworkCredential("USERNAME", "PASSWORD") };
var client = new HttpClient(new HttpClientHandler { Proxy = proxy });
Console.WriteLine(await client.GetStringAsync("https://icanhazip.com"));
