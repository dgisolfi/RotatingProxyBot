#!/usr/bin/python3
# Date: 2019-1-9

from RotatingProxyBot import ProxyBot
import os
import pytest

class TestRotatingProxyBot:
    test_id = 1
    # Test that a new instance of the class can be created
    # The default ID is 0 so use a different number to test
    def testCreateBot(self):
        bot = ProxyBot(id=self.test_id, keep_alive=True)
        assert(bot.id == self.test_id)
        self.test_id += 1
    
    def testNewProxy(self):
        bot = ProxyBot(id=self.test_id, keep_alive=True)
        proxy = bot.rotating_proxy.rotate()
        assert proxy != None
        assert proxy != ''
        self.test_id += 1

    def testImportProxyFile(self):
        fake_proxies = [
            '0.0.0.0:80',
            '0.0.0.0:8080',
            '0.0.0.0:9090',
        ]
        # create a test file of proxies
        proxies = open('proxies.txt','w+')

        for proxy in fake_proxies:
            proxies.write(f'{proxy}\n')

        proxies.close()
        # Create an example bot and tell it to 
        # use the list of proxies in the file
        bot = ProxyBot(
            id=self.test_id,
            desired_reqs=3,
            reqs_per_int=1,
            wait_time=10,
            proxy_file='proxies.txt'
        )
        self.test_id += 1

        # The rotate function gets the first element of the proxies array 
        # so assert that the proxies put to file are the same in the bots proxy list
        for proxy in fake_proxies:
            prox = bot.rotating_proxy.rotate()
            print(prox, proxy)
            assert prox == proxy

        os.remove('proxies.txt')

    # Final test, run the bot and ensure it doesnt fail
    def testBot(self):
        # create a new instance of the bot with basic arguements
        # cant think of any asserts, so just make sure this runs properly
        bot = ProxyBot(
            id=self.test_id,
            method='GET',
            desired_reqs=2,
            reqs_per_int=1,
        )
        bot.enable()
        self.test_id += 1




