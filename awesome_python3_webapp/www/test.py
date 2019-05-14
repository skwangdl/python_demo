import unittest
from models import *

class AppTest(unittest.TestCase):
    def test_saveuser(self):
        user = User(id='kepler', email='kepler', passwd='kepler', admin=123, name='kepler', image='kepler', create_at=123)
        yield from user.save()

if __name__ == '__main__':
    unittest.main()