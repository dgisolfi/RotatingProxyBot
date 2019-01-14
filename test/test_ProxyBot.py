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
        self.test_id += 1
    
    def testNewProxy(self):
        bot = ProxyBot(id=self.test_id, keep_alive=True)
        proxy = bot.rotating_proxy.rotate()
        assert proxy != None
        assert proxy != ''
        self.test_id += 1

    # Final test, run the bot and ensure it doesnt fail
    def testBot(self):
        # create a new instance of the bot with basic arguements
        # cant think of any asserts, so just make sure this runs properly
        bot = ProxyBot(
            id=self.test_id,
            method='GET',
            desired_reqs=2,
            reqs_per_int=1,
            wait_time=3
        )
        bot.enable()
        self.test_id += 1




