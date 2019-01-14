#!/usr/bin/python3
# Date: 2019-1-9

from RotatingProxyBot import RotatingProxy
import pytest
import os

class TestRotatingProxyBot:
    def testRotateProxy(self):
        rotating_proxy = RotatingProxy()

        # Call for a new proxy and ensure one is returned
        proxy = rotating_proxy.rotate()
        assert proxy != None
        assert proxy != ''

        # Ensure the proxies are being added to the used list
        assert rotating_proxy.used_proxies[0] == proxy

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

        rotating_proxy = RotatingProxy(proxy_file='proxies.txt')

        # The rotate function gets the first element of the proxies array 
        # so assert that the proxies put to file are the same in the bots proxy list
        for proxy in fake_proxies:
            prox = rotating_proxy.rotate()
            print(prox, proxy)
            assert prox == proxy

        os.remove('proxies.txt')

    