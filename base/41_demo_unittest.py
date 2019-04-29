import unittest

class Dict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value

class TestDict(unittest.TestCase):

    def setUp(self):
        print('this is setUp')

    def tearDown(self):
        print('this is tearDown')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        print('testing...')
        self.assertTrue(isinstance(d, Dict))

if __name__ == '__main__':
    unittest.main()