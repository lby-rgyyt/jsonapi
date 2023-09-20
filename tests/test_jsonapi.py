import json
from jsonapi import jsonapi
import random
import unittest


class Test(unittest.TestCase):
    def test_complex(self):
        for i in range(10):
            c = complex(random.random(), random.random())
            j_c = json.dumps(c, cls=jsonapi.MyEncoder)
            # print(j_c)
            un_j_c = json.loads(j_c, cls=jsonapi.MyDecoder)
            # print(un_j_c)
            self.assertEqual(c, un_j_c)

    def test_range(self):
        for i in range(10):
            r = range(random.randint(-10, 10),
                      random.randint(-10, 10), random.randint(1, 4))
            j_r = json.dumps(r, cls=jsonapi.MyEncoder)
            # print(r_c)
            un_j_r = json.loads(j_r, cls=jsonapi.MyDecoder)
            # print(un_r_c)
            self.assertEqual(r, un_j_r)
