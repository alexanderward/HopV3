import time
from itertools import cycle
from random import shuffle

import requests
import logging

from requests import ReadTimeout, ConnectTimeout

logger = logging.getLogger(__file__)

api_key = "75483def8b2456ddf4e3b0ae2e5910592cb7a216c42fe177a1!50385"  # todo - s3ssm


class Proxy(object):

    def __init__(self, proxy_type='SOCKS5', free=True):
        self.proxy_type = proxy_type  # HTTP, HTTPS, SOCKS4, SOCKS5
        self.free = free
        self.__proxy_pool_base = []
        self.current_proxy = None
        self.proxy_pool = cycle([])

    def __scrape_proxies(self, proxy_latency=None):
        if self.free:
            url = f'https://api.proxyscrape.com/?request=getproxies&proxytype={self.proxy_type}&timeout={proxy_latency}&country=US&anonymity=elite'
            if self.proxy_type == "HTTPS":
                url = f'{url}&ssl=yes&anonymity=all'
            elif self.proxy_type == "HTTP":
                url = f'{url}&ssl=no&anonymity=all'
            resp = requests.get(url)
            if "Please" in resp.text:
                # print(f"Waiting 10 second due to msg: {resp.text}")
                time.sleep(10)
                return self.__scrape_proxies(proxy_latency)
            proxies = resp.text.split()
            pool = []
            for proxy in proxies:
                pool.append(f"{self.proxy_type.lower()}://{proxy}")
        else:
            # https://proxybonanza.com/en/articles/api-v1-reference-1
            resp = requests.get('https://proxybonanza.com/api/v1/userpackages.json',
                                headers={'Authorization': api_key})
            package = resp.json()["data"][0]
            resp = requests.get(f'https://proxybonanza.com/api/v1/userpackages/{package["id"]}.json',
                                headers={'Authorization': api_key})
            pool = [f"socks5://{package['login']}:{package['password']}@{x['ip']}:{x['port_socks']}"
                    for x in resp.json()['data']['ippacks']]
        shuffle(pool)
        return pool

    def __retrieve(self):
        logger.info("Retrieving Proxy List")
        self.__proxy_pool_base = self.__scrape_proxies()
        logger.info("Successfully Retrieved {} Proxies".format(len(self.__proxy_pool_base)))
        self.proxy_pool = cycle(self.__proxy_pool_base)

    def __select_proxy(self):
        if not self.__proxy_pool_base:
            self.__retrieve()
            return self.__select_proxy()
        return next(self.proxy_pool)

    def next(self):
        self.current_proxy = self.__select_proxy()
        # print(self.current_proxy)

    def current(self):
        if not self.current_proxy:
            self.next()
        return {"https": self.current_proxy}

    def mark_bad(self):
        if self.current_proxy:
            # print(f"Removing proxy: {self.current_proxy}")
            try:
                del self.__proxy_pool_base[self.__proxy_pool_base.index(self.current_proxy)]
            except ValueError:
                pass
        self.proxy_pool = cycle(self.__proxy_pool_base)
        # print('bad proxy', self.current_proxy)

    def get(self, *args, **kwargs):
        try:
            return requests.get(*args, **kwargs, proxies=self.current())
        except (ReadTimeout, ConnectTimeout, requests.exceptions.ConnectionError):
            self.mark_bad()
            self.next()
            return self.get(*args, **kwargs)


if __name__ == '__main__':
    import pprint

    my_proxy = Proxy()
    pprint.pprint(requests.get('https://api.ipify.org/?format=json', proxies=None).json())
    pprint.pprint(my_proxy.get('https://api.ipify.org/?format=json', timeout=10).json())
    pprint.pprint(my_proxy.get('https://api.ipify.org/?format=json', timeout=10).json())
