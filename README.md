# ultimate-web-scraper-template
A bunch of freely available anti-scraping techniques bundled into a single template

```python
# import library & dependencies
from scraper import *

# default scraper uses proxy, 5 tries to fetch proxy list, 0 delay between requests
print('\nFree proxies used:')
scraper = Scraper()
scraper.test_requests()

# no proxy
print('\nNo proxies:')
scraper = Scraper(use_proxy=False, delay=2)
scraper.test_requests()

# if you want to use custom headers
scraper = Scraper()
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
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

```
