import unittest

from hw4 import GithubApi


class TestGithubAPI(unittest.TestCase):
    def testGithub(self):
        self.assertEqual(GithubApi('?'), False)
    def testGithub2(self):
        self.assertEqual(GithubApi('sprabhu5'), True)
       
if __name__ == '__main__':
    unittest.main()
