memd
=======

memcached decorator for lazy developers (like me) built on top of python-memcached

### usage

    # simple
    @memd
    def foo(bar):
        return bar
    
    # with custom key and ttl
    @memd(custom_key="yourkey")
    def foo(bar):
        return bar