#!/usr/bin/python3
# Date: 2019-1-9

import requests

class RotatingProxy:
    def __init__(self, *args, **kwargs):
        self.proxy_list_addr = kwargs.get('', 'https://www.proxy-list.download/api/v1/get')
        self.proxies = []
        self.used_proxies = []
        self.buildProxyList()
        
    def buildProxyList(self):
        try:
            print('Attempting to Build list of Proxies')
            session = requests.Session()
            response = session.get(self.proxy_list_addr, params={'type':'https'})

            if response.status_code != 200:
                print(f'Request status: {response.status_code}')
                print('Proxy List Not Build!')
                raise ValueError('The request made to build the proxie list returned as a non 200 status code')

            for proxy in response.text.splitlines():
                self.proxies.append(proxy)
            
            if self.proxies != None:
                print('Proxy List Built')
            
        except:
            raise ValueError(f'An Error occured while building the Proxy List:\n{self.proxy_list_addr}')

    def rotate(self):
        # Provide a new proxy
        proxy = self.proxies.pop()
        print(f'\nSwitched to new Proxy:{proxy}({len(self.proxies)-1})')
        # add used proxy to the used proxy list
        self.used_proxies.append(proxy)
        return proxy