from unittest import TestCase

import farside_results


class TestMe(TestCase):
    def test_unknown(self):
        self.assertEqual("https://example.com", farside_results.new_link("https://example.com"))

    def test_unknown_http(self):
        self.assertEqual("http://example.org", farside_results.new_link("http://example.org"))

    def test_wikipedia(self):
        self.assertEqual("https://farside.link/wikiless/wiki/Alice", farside_results.new_link("https://en.wikipedia.org/wiki/Alice"))
