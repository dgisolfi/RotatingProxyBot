#!/usr/bin/python3
# Date: 2019-1-9

import requests

class RotatingProxy:
    def __init__(self, *args, **kwargs):
        self.proxy_list_addr = kwargs.get('proxy_api', 'https://www.proxy-list.download/api/v1/get')
        self.proxy_file = kwargs.get('proxy_file', None)
        self.proxies = []
        self.used_proxies = []

        if self.proxy_file == None:
            self.buildProxyList()
        else:
            self.importProxyList()
        
    def buildProxyList(self):
        try:
            print(f'Attempting to Build list of Proxies from API: {self.proxy_list_addr}')
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
    
    def importProxyList(self):
        try:
            print(f'Attempting to Build list of Proxies from file: {self.proxy_file}')
            file = open(self.proxy_file)
            lines = file.read().splitlines() 
            for proxy in lines:
                self.proxies.append(proxy)

            print('Proxy List Built from file')
        except:
            raise ValueError(
                f'An Error occured while building the Proxy List from file\n'+
                'ensure the filename and directory are correct, and the proxies are in the correct format'
            )

    def rotate(self):
        # Provide a new proxy
        proxy = self.proxies.pop(0)
        # add used proxy to the used proxy list
        self.used_proxies.append(proxy)
        print(f'\nSwitched to new Proxy:{proxy}\n{len(self.used_proxies)} of {len(self.proxies)}')
       
        return proxy