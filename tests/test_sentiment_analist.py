import unittest
from backend.ai import run_sentiment_analysis


class TestSentimentAnalysis(unittest.TestCase):

    def test_negative_sentence(self):
        text = "dude is extremely dumb, stupid and smells like crap"
        result = run_sentiment_analysis(text)
        self.assertLess(result['pos'], 0.5)
        self.assertLess(result['neu'], 0.75)
        self.assertGreater(result['neg'], 0.5)

    def test_positive_sentence(self):
        text = "dude is smart, handsome, and funny."
        result = run_sentiment_analysis(text)
        self.assertGreater(result['pos'], 0.5)
        self.assertLess(result['neg'], 0.5)

    def test_neutral_sentence(self):
        text = "Mars is far away"
        result = run_sentiment_analysis(text)
        self.assertGreater(result['neu'], 0.75)
        self.assertTrue(result['pos'] < 0.75)
        self.assertTrue(result['neg'] < 0.75)


if __name__ == '__main__':
    unittest.main()
