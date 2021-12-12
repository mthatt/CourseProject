from unittest import TestCase, main as unittest_main, mock
from RedditApp import RedditApp
from SentimentProcessing import SentimentProcessing

class PlaylistsTests(TestCase):
    """Flask tests."""
    def setUp(self):
        self.analyzer = RedditApp()

    def testCoinsAreModified(self):
        self.assertNotEqual(self.analyzer.coinScore1, self.analyzer.coinScore2)

if __name__ == '__main__':
    unittest_main()