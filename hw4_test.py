"""
@author:Shivani
HW04
"""
import unittest
from unittest import mock
from hw4 import GithubApi


@mock.patch('urllib.request.urlopen')
class TestRepo(unittest.TestCase):
    """Test for the repositoryList function"""

    def test_commits(self, other):
        repo = [value for value in repositoryList("Shivani-Prabhu")]
        result = ["Repo: GitHubApi567, commits: 12", "Repo: hw4, commits: 1", "Repo: StaticCodeAnalysis567, "
                                                                                   "commits: 2", "Repo: Triangle567, "
                                                                                                 "commits: 12"]
        self.assertEqual(repo, result)



if _name_ == '_main_':
    unittest.main(exit=False, verbosity=2)
