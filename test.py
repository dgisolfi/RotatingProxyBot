from RotatingProxyBot import ProxyBot


bot = ProxyBot(
            id=1, 
            keep_alive=True,
            reqs = 2
        )
        
bot.enable()