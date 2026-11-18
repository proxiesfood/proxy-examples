<?php
$ch = curl_init("https://icanhazip.com");
curl_setopt($ch, CURLOPT_PROXY, "http://proxies.proxiesfood.com:81");
curl_setopt($ch, CURLOPT_PROXYUSERPWD, "USERNAME:PASSWORD");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
echo curl_exec($ch);
