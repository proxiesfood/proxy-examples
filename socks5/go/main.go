package main

import (
	"fmt"
	"io"
	"net/http"
	"net/url"
)

func main() {
	proxy, _ := url.Parse("socks5://USERNAME:PASSWORD@proxies.proxiesfood.com:81")
	client := &http.Client{Transport: &http.Transport{Proxy: http.ProxyURL(proxy)}}
	resp, err := client.Get("https://icanhazip.com")
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	body, _ := io.ReadAll(resp.Body)
	fmt.Print(string(body))
}
