# pip install seleniumbase
from seleniumbase import Driver

driver = Driver(proxy="USERNAME:PASSWORD@proxies.proxiesfood.com:81")
driver.get("https://icanhazip.com")
print(driver.find_element("tag name", "body").text)
driver.quit()
