import unittest
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p_1(self):
        node = LeafNode("p", "Hello, world!")
        expected = "<p>Hello, world!</p>"
        actual = node.to_html()
        self.assertEqual(actual, expected)
    def test_leaf_to_html_p_2(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"
        actual = node.to_html()
        self.assertEqual(actual, expected)
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = "<a href=\"https://www.google.com\">Click me!</a>"
        actual = node.to_html()
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
