from RotatingProxyBot import ProxyBot


bot = ProxyBot(
            id=3,
            method='GET',
            desired_reqs=2,
            reqs_per_int=1,
            wait_time=3
        )
bot.enable()
