#!/usr/bin/python3
# Date: 2019-1-8

from .RotatingProxy import *
from tqdm import tqdm
import requests
import random
import time

class ProxyBot:
    def __init__(self, *args, **kwargs):
        self.id = kwargs.pop('id', 0)
        self.address = kwargs.pop('address', 'http://httpbin.org/ip')
        self.method = kwargs.pop('method', 'GET')
        self.params = kwargs.pop('reqs_params', False)
        self.desired_reqs = kwargs.pop('desired_reqs', 0)
        self.reqs_per_int = kwargs.pop('reqs_per_int', self.desired_reqs)
        self.keep_alive = kwargs.pop('keep_alive', False)
        self.wait_time = kwargs.pop('wait_time', 0)
        self.proxy_api = kwargs.pop('proxy_api', None)
        self.proxy_list = kwargs.pop('proxy_file', None)
        
        if self.proxy_api != None:
            self.rotating_proxy = RotatingProxy(proxy_api=self.proxy_api)
        elif self.proxy_list != None:
            self.rotating_proxy = RotatingProxy(proxy_file=self.proxy_list)
        else:
            self.rotating_proxy = RotatingProxy()
        
        self.proxy = ''
        self.current_req = 0
        self.req_count = 0
        self.enabled = False
        print(f'ProxyBot {self.id} Created')

    def __str__(self): 
        return f'ProxyBot({self.id})'
    
    def __repr__(self):
        return self.__str__()
    
    def getRequest(self, proxy):
         # request the specified website
        try:
            session = requests.Session()
            response = session.get(self.address, proxies=proxy, params=self.params)
            print(f'Request status: {response.status_code} \n {response.text}')
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print ('Http Error:', errh)
        except requests.exceptions.ConnectionError as errc:
            print ('Error Connecting:', errc)
        except requests.exceptions.Timeout as errt:
            print ('Timeout Error:', errt) 
        except KeyboardInterrupt:
            self.enabled = False
        except:
            print(f'An Error occured while making a GET request to:\n{self.address}')
            return 'proxy err'
    

    def postRequest(self, proxy):
        # request the specified website
        try:
            session = requests.Session()
            response = session.post(self.address, proxies=proxy, data=self.params)
            print(f'Request status: {response.status_code} \n {response.json()}')
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print ('Http Error:', errh)
        except requests.exceptions.ConnectionError as errc:
            print ('Error Connecting:', errc)
        except requests.exceptions.Timeout as errt:
            print ('Timeout Error:', errt) 
        except KeyboardInterrupt:
            self.enabled = False
        except:
            print(f'An Error occured while making a GET request to:\n{self.address}')
            return 'proxy err'
          
    def wait(self):
        # Get a random interval of time to wait for # between 10-20mins
        print(f'Waiting for the next {self.wait_time/60} Mins')
        for tick in tqdm(range(self.wait_time)):
            time.sleep(1)

    def preformRotate(self):
        self.proxy = self.rotating_proxy.rotate()

        if self.method == 'GET':
            response = self.getRequest({'https':self.proxy})
        elif self.method == 'POST':
            response = self.postRequest({'https':self.proxy})
        else:
            raise ValueError(f'Method: {self.method} is not valid.\nValid Methods GET or POST')
        
         # Check if the proxy was bad
        if response == 'proxy err':
            self.preformRotate()
        else:
            return response

    def enable(self):
        self.enabled = True
        while self.enabled:
            try:
                if not self.keep_alive:
                    if self.req_count >= self.desired_reqs:
                        self.enabled = False
                            
                # Every n requests the Bot will wait for a given time to avoid overflowing server
                if self.current_req == self.reqs_per_int:
                    self.current_req = 0
                    self.wait()
                else:
                    self.preformRotate()
                    self.current_req += 1
                    self.req_count += 1


            except KeyboardInterrupt:
                self.enabled = False
            except ValueError as err:
                raise ValueError(f'Value Error Raised: {err}')

    def disable(self):
        self.enabled = False
        print(f'ProxyBot {self.id} Disabled')
        print(f'\tfinal proxy: {self.proxy}')
        self.__del__()

    def __del__(self):
        print(f'ProxyBot {self.id} Deleted')