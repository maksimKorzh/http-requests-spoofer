# HTTP requests spoofer
Freely available & most common web scraping techniques implemented to bypass simple anti-scraping measures bundled into a single class with a dead simple interface

# How to use it
```python
# import library & dependencies
from scraper import *

# default params are: (use_proxy=True, spoof_agent=True, tries=5, delay=0)
scraper = Scraper()

# if you want to use custom headers
scraper.headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'your-custom-header': 'custom-value',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

# make GET request
response_get = scraper.GET('https://enckllaec924.x.pipedream.net/')
print(response_get, response_get.text)

# make POST request
response_post = scraper.POST('https://enckllaec924.x.pipedream.net/', {'param1': 'val1', 'param2': 'val2'})
print(response_post, response_post.text)

# check out at
print('visit: https://requestbin.com/r/enckllaec924 to inspect it\n')

# test proxies
print('Testing proxies:')
for i in range(10):
    try: print(scraper.GET('https://api.ipify.org?format=json').text)
    except: print('Failed')
```

# What is this?
    It's a library that allows making HTTP GET & POST requests
    via proxy meanwhile spoofing the user agent header.

# How it works?
    1. Before making an HTTP request to a desired URL it
       first treis to download a list of free proxies from
       https://free-proxy-list.net/
       choosing only elite proxies with HTTPS support.

    2. It tests newly scraped proxies with a 1 sec timeout
       and if the proxy is alive it gets appended to a list.
    
    3. Finally it randomly picks up a proxy from a list and
       uses it. If proxy fails for some reason your original IP
       is used instead.

# How to bypass CAPTCHA (rhetoric question)?
    Try not to fall into one or better buy 
    a paid API subscription from the target website
    to fetch the data legally ;)


