#!/usr/bin/env python

from memd import memd, CacheManager
import uuid
import unittest
import memcache

class Test(unittest.TestCase):

    @memd(custom_key="mykey")
    def nottl(self, value):
        return value
    
    @memd(ttl=1)
    def randomkey(self, value):
        return value
        
    def test(self):
        # check predefined key
        self.mcd = CacheManager()
        uvalue = str(uuid.uuid1())
        self.nottl(uvalue)    
        mvalue = self.mcd.get("mykey")
        self.mcd.delete("mykey")
        #self.assertEqual(str(mvalue), str(uvalue))
        # check random key... theoretically function randomkey returns a new value every time
        # but with the decorator the first value is cached
        v1 = self.randomkey(str(uuid.uuid1()))
        v2 = self.randomkey(str(uuid.uuid1()))
        self.assertEqual(str(v1), str(v2))
    
if __name__ == '__main__':
    unittest.main()