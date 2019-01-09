#!/usr/bin/python3
# Date: 2019-1-8

from tqdm import tqdm
import requests
import random
import time

class RotatingProxyBot:
    def __init__(self, *args, **kwargs):
        self.address = kwargs['address']
        self.desired_subs = kwargs['submissions']
        self.proxies = []
        self.current_sub = 0
        # Every 2 the Bot will wait for a 
        # given time to avoid overflowing server
        self.sub_count = 0

    def __repr__(self): 
        return f'RotatingProxyBot({self.address}, {self.desired_subs})'
    
    def __del__(self):
        print('Bot Deleted')

    def buildProxyList(self):
        proxy_list_addr = 'https://www.proxy-list.download/api/v1/get'
        try:
            print('Attempting to Build list of Proxies')
            session = requests.Session()
            response = session.get(proxy_list_addr, params={'type':'https'})
            print(f'Request status: {response.status_code}')
            
            if response.status_code != 200:
                print(f'Request status: {response.status_code}')
                print('Proxy List Not Build!')
                raise ValueError('The request made to build the proxie list returned as a non 200 status code')

            for proxy in response.text.splitlines():
                self.proxies.append(proxy)
            
            if self.proxies != None:
                print('Proxy List Built')
        except:
            raise ValueError(f'An Error occured while building the Proxy List:\n{proxy_list_addr}')

    def submit(self, proxy):
        # request the specified website
        try:
            session = requests.Session()
            response = session.post(self.address, proxies=proxy)
            print(f'Request status: {response.status_code} \n {response.json()}')
        except:
            raise ValueError(f'An Error occured while making a GET request to:\n{self.address}')

    def wait(self):
        # Get a random interval of time to wait for
        wait_time = random.randint(600,1200) # between 10-20mins
        print(f'Waiting for the next {wait_time/60} Mins')
        for tick in tqdm(range(wait_time)):
            time.sleep(1)

    def rotate(self):
        try:
            for proxy in self.proxies:
                if self.current_sub >= self.desired_subs:
                    break
                elif self.sub_count == 2:
                    self.wait()
                    self.sub_count = 0
                else:
                    self.submit({'https':proxy})
                    self.current_sub += 1
                    self.sub_count += 1

        except KeyboardInterrupt:
            print('Bot Interupted')