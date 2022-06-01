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

