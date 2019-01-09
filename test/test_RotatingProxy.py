#!/usr/bin/python3
# Date: 2019-1-9

from RotatingProxyBot import RotatingProxy
# from RotatingProxyBot import ProxyBot
import pytest

class TestRotatingProxyBot:
    def test_RotateProxy(self):
        rotating_proxy = RotatingProxy()

        proxy = rotating_proxy.rotate()
        assert proxy != None
        assert proxy != ''