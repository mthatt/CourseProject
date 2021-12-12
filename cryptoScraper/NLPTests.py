from unittest import TestCase, main as unittest_main, mock
import RedditApp
from SentimentProcessing import SentimentProcessing

class PlaylistsTests(TestCase):
    """Flask tests."""
    def setUp(self):
        self.analyzer = SentimentProcessing()

    def testSlightlyPositivePost(self):
        phrase = "Bitcoin is ok, I think there is potential for growth. I feel alright about it"
        self.assertEqual(self.analyzer.getSentimentScore(phrase), "Positive")

    def testVeryPositivePost(self):
        phrase = "Ethereum is absolutely amazing, I think it's going to skyrocket soon I'm so excited!"
        self.assertEqual(self.analyzer.getSentimentScore(phrase), "Positive")

    def testSlightlyNegativePost(self):
        phrase = "Dogecoin is trending down, I'm upset about the direction it's heading in"
        self.assertEqual(self.analyzer.getSentimentScore(phrase), "Negative")

    def testVeryNegativePost(self):
        phrase = "I absolutely hate altcoins, I think they're stupid"
        self.assertEqual(self.analyzer.getSentimentScore(phrase), "Negative")

    def testBadData(self):
        self.assertRaises(TypeError, self.analyzer.getSentimentScore(0), "Negative")


if __name__ == '__main__':
    unittest_main()