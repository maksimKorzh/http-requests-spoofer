########################################################
#
#       HTTP requests 
#
#                          by
#
#                   Code Monkey King
#
########################################################

# packages
import requests
from bs4 import BeautifulSoup
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem, Popularity
import random
import time

# otodom scraper class
class Scraper():    
    # custom headers
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    
    # init
    def __init__(self, use_proxy=True, tries=5, delay=0):
        # init params
        self.use_proxy = use_proxy
        self.tries = tries
        self.delay = delay
        
        # init random user agents
        software_names = [SoftwareName.CHROME.value,
            SoftwareName.SAFARI.value,
            SoftwareName.INTERNET_EXPLORER.value,
            SoftwareName.CHROMIUM.value
        ]
    
        operating_systems = [
            OperatingSystem.WINDOWS.value,
            OperatingSystem.LINUX.value,
            OperatingSystem.MAC_OS_X.value,
            OperatingSystem.MAC.value,
            OperatingSystem.MACOS.value,
            OperatingSystem.ANDROID.value,
        ]   

        self.user_agent_rotator = UserAgent(
            software_names=software_names,
            operating_systems=operating_systems,
            limit=100000
        )

    # user agent rotation
    def get_random_agent(self):
        return self.user_agent_rotator.get_random_user_agent()
    
    # get random proxy
    def get_random_proxy(self, tries):
        # return if axceeded the number of tries
        if tries == 0: return {}
        
        # proxy list
        proxies = []
        
        # get proxies
        response = requests.get('https://free-proxy-list.net/')
        content = BeautifulSoup(response.text, 'lxml')
        
        # extract proxies
        for row in content.find('table').find_all('tr'):
            try:
                proxy = [col.text for col in row.find_all('td')]
                if proxy[4] == 'elite proxy' and proxy[6] == 'yes':
                    proxy = {'https': 'https://' + proxy[0] + ':' + proxy[1]}
                    if requests.get('https://api.ipify.org?format=json', proxies=proxy, timeout=1).status_code == 200:
                        proxies.append(proxy)

            except: pass

        # return random proxy if found, try again otherwise
        if len(proxies): return random.choice(proxies)
        else: self.get_random_proxy(tries - 1)

    # test proxies
    def test_requests(self):
        for i in range(10):
            try: print(self.GET('https://api.ipify.org?format=json').text)
            except: print('Failed')
    
    # crawler's entry
    def GET(self, url):        
        # delay before request
        time.sleep(self.delay)
        
        # rotate user agent
        self.headers['user-agent'] = self.get_random_agent()
        
        try:
            # get random proxy
            random_proxy = self.get_random_proxy(self.tries) if self.use_proxy is True else {}

            # crawl next postcode URL
            return requests.get(
                url=url,
                headers=self.headers,
                proxies=random_proxy
            )

        except Exception as e:
            # crawl next postcode URL
            return requests.get(
                url=url,
                headers=self.headers,
            )

# demo
if __name__ == '__main__':
    # create scraper instance
    scraper = Scraper()
    
    # run tests
    scraper.test_requests()

