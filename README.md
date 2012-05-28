memd
=======

memcached decorator for lazy developers (like me) built on top of python-memcached

### usage

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

### licence

memd is released under the MIT license