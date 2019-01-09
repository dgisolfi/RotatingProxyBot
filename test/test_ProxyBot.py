#!/usr/bin/python3
# Date: 2019-1-9

from RotatingProxyBot import ProxyBot
import pytest

class TestRotatingProxyBot:
    test_id = 1
    # Test that a new instance of the class can be created
    # The default ID is 0 so use a different number to test
    def testCreateBot(self):
        bot = ProxyBot(id=self.test_id, keep_alive=True)
        assert(bot.id == self.test_id)
    
    def testNewProxy(self):
        bot = ProxyBot(id=self.test_id, keep_alive=True)
        proxy = bot.rotating_proxy.rotate()
        assert proxy != None
        assert proxy != ''

    def testBot(self):
        bot = ProxyBot(
            id=self.test_id,
            address='http://httpbin.org/ip',
            method='GET',
            reqs=2
        )
        bot.enable()
        bot.disable()



