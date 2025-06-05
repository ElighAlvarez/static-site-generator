import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_1(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        actual = node.props_to_html()
        expected = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(actual, expected)
    def test_props_to_html_2(self):
        node = HTMLNode(props={})
        actual = node.props_to_html()
        expected = ""
        self.assertEqual(actual, expected)
    def test_props_to_html_3(self):
        node = HTMLNode()
        actual = node.props_to_html()
        expected = ""
        self.assertEqual(actual, expected)
    def test_props_to_html_4(self):
        node = HTMLNode(props={"a":"b", "c":3, "dict": {"zero": 0}})
        actual = node.props_to_html()
        expected = " a=\"b\" c=\"3\" dict=\"{'zero': 0}\""
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
