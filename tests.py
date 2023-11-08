import unittest
from main import*

class Test(unittest.TestCase):
    def add_positive(self):
        resuls = add(2,3)
        self.assertEquals(resuls,5)

def add_videmni(self):
    result = add(-2,-3)
    self.assertEquals(result,-5)

def add_mix(self):
    result = add(-2,3)
    self.assertEquals(result,1)

if __name__=="__mein__":
    unittest.main()