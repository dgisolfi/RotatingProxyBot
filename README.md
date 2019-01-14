# RotatingProxyBot
A Bot that uses a Rotating Proxy to simulate many clients making a request to a single server

**Version 0.0.3**

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
    wait_time=60 # 1min
)
# Start Submiting and rotating proxies
bot.enable()
```

## Building a list of Proxies

The bot will need a list of proxies to use for making requests, it can use either an API to retrieve proxies or a file to import them from.

### Proxies from an API

By default, the bot will retrieve a few thousand proxies from an [API](https://www.proxy-list.download/). To use a custom API tell the bot what address to reach the API at by passing in the following argument when creating a new instance `proxy_api='http://api.com'`.

### Proxies from a File

To use a custom file of proxies rather than the default API, pass in the following argument to the bot constructor `proxy_file=filename.txt`
For the bot to be able to import the list of proxies, the file should have the following structure:

```txt
0.0.0.0:80
1.1.1.1:90
2.2.2.2:20
```

## Methods

The following are some useful methods that are a part of the package

### ProxyBot

* **getRequest(proxy)** - if passed a specific proxy, this method will perform a`GET` request using the specified proxy to the address set in the creation of the bot. EX: `getRequest('0.0.0.0:80')`
* **postRequest(proxy)** - if passed a specific proxy, this method will perform a `POST` request using the specified proxy to the address set in the creation of the bot. EX: `postRequest('0.0.0.0:80')`
* **preformRotate()** - if called the bot will request a new proxy from the RotatingProxy class and perform the specified request to the specified address, returning the response element
* **enable()** - if called will initiate the main loop of the bot, making the specified requests to the address using the set number of intervals and wait time
* **disable()** - if called will shut down the main loop of the program and delete the bot

### RotatingProxy

* **buildProxyList()** - when called will contact the set API(or default one) to retrieve a list of  up to date proxies in which it can pull from to make requests
* **importProxyList()** - will attempt to build a list of proxies from the file name provided.
* **rotate()** - will return the 0th proxy in the list and add it to the used proxy list.

## Additional Arguments for the Constructor

The following are keyword arguments that can be passed into the constructor of the ProxyBot Class.

* **id** - Assigns the instance of the ProxyBot with the given numeric ID

  Example: `RotatingProxyBot(id=1)`

* **address** - the IP or URL for the bot to contact, will default to a tester API

  Example: `RotatingProxyBot(address='0.0.0.0')`

* **method** - The request method to be used. Only `GET` and `POST` supported. The default is `GET`
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