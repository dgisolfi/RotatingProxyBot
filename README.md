# RotatingProxyBot
A Bot that acts as a Rotating Proxy Crawler, simulating many clients to a single server

### Author

**Daniel Gisolfi** - *All current work* - [dgisolfi](https://github.com/dgisolfi)

## Deployment

The Rotating Proxy Bot can be run with purely python, to do so import the bot into a python file and use the following to run it.
```python
#!/usr/bin/python3
from RotatingProxyBot.bot import ProxyBot

# Create new custom bot
bot = RotatingProxyBot(
    address='IP OR URL', 
    submissions=10
)
# Get latest Proxies and store them
bot.buildProxyList()
# Start Submiting and rotating proxies
bot.rotate()
```

