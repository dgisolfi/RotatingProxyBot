# RotatingProxyBot
A Bot that acts as a Rotating Proxy Crawler, simulating many clients to a single server

### Author

**Daniel Gisolfi** - *All current work* - [dgisolfi](https://github.com/dgisolfi)

## Usage

```python
#!/usr/bin/python3
from RotatingProxyBot import ProxyBot

# Create new custom bot
bot = ProxyBot(
    address='IP OR URL',
    method='POST'
    desired_reqs=10,
    reqs_per_int=2,
    wait_time=600 # 10 mins
)
# Start Submiting and rotating proxies
bot.enable()
```

## Arguemnts

The following are key word arguments that can be passed into the constructor of the ProxyBot Class.

* **id** - Assigns the instance of the ProxyBot with the given numeric ID

  Example: `RotatingProxyBot(id=1)`

* **address** - the IP or URL for the bot to contact, will defualt to a tester API

  Example: `RotatingProxyBot(address='0.0.0.0')`

* **method** - The request method to be used. Only `GET` and `POST` supported. Defulat is `GET`
  Example: `RotatingProxyBot(method='POST')`

* **params** - Parameters to be passed with the request, works with all request methods 
  Example: `RotatingProxyBot(params={'example':'test'})`

* **desired_reqs** - Desired number of requests to be completed

  Example: `RotatingProxyBot(desired_reqs=10)`

* **keep_alive** - A boolean allow the bot to continue to make requests forever

  *if set to `True` dont set `desired_reqs`*
  Example: `RotatingProxyBot(keep_alive=True)`

* **reqs_per_int** - Requests Per Interval, number of requests to be completed before waiting. This will prevent the server from being DOSed
  Example: `RotatingProxyBot(reqs_per_int=2)`

* **wait_time** - Amount of time in Seconds to wait until the next interval of requests
  Example: `RotatingProxyBot(wait_time=600)`

