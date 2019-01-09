from RotatingProxyBot.bot import ProxyBot
import pytest

class TestRotatingProxyBot:
    # The instance of the bot created, can be used by all tests
    # If the first tests fail all others will as a consequence
    bot = None

    # Test that a new instance of the class can be created
    # The default ID is 0 so use a different number to test
    def testCreateBot(self):
        test_id = 1
        self.bot = ProxyBot(id=test_id, keep_alive=True)
        assert(self.bot.id == test_id)

    