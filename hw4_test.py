import unittest

import unittest.mock as mock

from hw4 import GithubApi

class TestGithubAPI(unittest.TestCase):
    def testGithub(self):
        with mock.patch('hw4.GithubAPI', create=True) as MockGithub:
            MockGithub.return_value = False
            self.assertEqual(MockGithub('?'), False)
    def testGithub2(self):
        with mock.patch('hw4.GithubAPI', create=True) as MockGithub:
            MockGithub.return_value = True
            self.assertEqual(MockGithub('sprabhu5'), True)
       
if __name__ == '__main__':
    unittest.main()
