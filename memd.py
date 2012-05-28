"""
memd - memcached decorator for lazy developers (like me)

usage: 

    # simple
    @memd()
    def foo(bar):
        return bar
    
    # with custom key
    @memd(custom_key="yourkey")
    def foo(bar):
        return bar
        
    # or with ttl
    @memd(ttl=100)
    def foo(bar):
        return bar

"""
import memcache
from hashlib import md5
from functools import wraps
import inspect
import json

class CacheManager:

    def __init__(self):
        self.enabled = True
        self.__cacheClient = memcache.Client(['localhost:11211'])

    def set(self, key, value, time = 0):
        if self.__cacheClient:
            self.__cacheClient.set(key, value, time)
            
    def delete(self, key):
        if self.__cacheClient:
            self.__cacheClient.delete(key)
            
    def get(self, key):
        if self.__cacheClient:
            return self.__cacheClient.get(key)
        return None

class memd(object):
    """    
    Parameters
        ttl : integer
            Time to live. default is 0 (cache forever)
        custom_key : string
            uses a specified custom key instead the auto generated
    """
    def __init__(self, ttl=0, custom_key=None):
        self.ttl = ttl
        self.custom_key = custom_key
        self.mcd = CacheManager()

    def __call__(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            
            # if not enabled executed the function
            if self.mcd.enabled:
                # key generation
                key = self.custom_key
                if not key:
                    # get function specs with a little help
                    jsonSpec = json.dumps(inspect.getargspec(fn))
                    # convert it in a MD5
                    key = md5(jsonSpec.encode('utf-8')).hexdigest()
                # get value
                output = self.mcd.get(key)
                if not output:
                    # get output
                    output = fn(*args, **kwargs)
                    if not output:
                        output = None
                    # set value & return
                    self.mcd.set(key, output, time=self.ttl)
                return None if output.__class__ is None else output
            else:
                # execute function
                return fn(*args, **kwargs)
        return wrapper