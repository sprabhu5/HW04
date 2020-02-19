import unittest

from hw4 import GithubApi

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestGithubAPI(unittest.TestCase):
    def testGithub(self):
        self.assertEqual(GithubApi('?'), False)
    def testGithub2(self):
        self.assertEqual(GithubApi('sprabhu5'), True)
       
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
