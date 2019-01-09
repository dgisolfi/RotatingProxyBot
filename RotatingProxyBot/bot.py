#!/usr/bin/python3
# Date: 2019-1-8

from tqdm import tqdm
import requests
import random
import time

class ProxyBot:
    def __init__(self, *args, **kwargs):
        self.id = kwargs.pop('id', 0)
        self.address = kwargs.pop('address', 'https://jsonplaceholder.typicode.com/users')
        self.desired_subs = kwargs.pop('submissions', 0)
        self.keep_alive = kwargs.pop('keep_alive', False)
        self.reqs_pause_count = kwargs.pop('reqs_pause_count', False)
        self.proxies = []
        self.current_req = 0
        # Every 2 the Bot will wait for a 
        # given time to avoid overflowing server
        self.req_count = 0
        print(f'Bot {self.id} Created')

    def __str__(self): 
        return f'ProxyBot({self.id})'
    
    def __repr__(self):
        return self.__str__()
    
    def __del__(self):
        print(f'Bot {self.id} Deleted')

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
            return response.json()
        except:
            print(f'An Error occured while making a GET request to:\n{self.address}')
            return 'proxy err'
          

    def wait(self):
        # Get a random interval of time to wait for
        wait_time = random.randint(600,1200) # between 10-20mins
        print(f'Waiting for the next {wait_time/60} Mins')
        for tick in tqdm(range(wait_time)):
            time.sleep(1)

    def rotate(self):
        try:
            for index, proxy in enumerate(self.proxies):
                if index < 61:
                    continue
                print(f'\n Switched to new Proxy:{proxy}({index})')
                if not self.keep_alive:
                    if self.current_req >= self.desired_subs:
                        break
                elif self.reqs_pause_count:
                    if self.current_req % self.reqs_pause_count == 0:
                        self.wait()
                        self.sub_count = 0
                else:
                    json = self.submit({'https':proxy})
                    if json == 'proxy err':
                        continue
                    elif json['status'] == 'failed':
                        continue
                    else:
                        print(json['status'])
                        self.current_req += 1
                        self.req_count += 1

        except KeyboardInterrupt:
            print('Bot Interupted')

# # Create new custom bot
# bot = RotatingProxyBot(
#     address='https://pinpoll.com/v1/polls/67763/answers/274566/vote', 
#     # submissions=3
#     keep_alive=True,
#     reqs_pause_count=2
# )
# # Get latest Proxies and store them
# bot.buildProxyList()
# # Start Submiting and rotating proxies
# bot.rotate()