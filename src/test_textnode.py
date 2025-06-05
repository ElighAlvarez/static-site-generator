import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_different_style(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is also a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_different_url(self):
        node = TextNode("This is a text node", TextType.IMAGE, '../static/shiba.png')
        node2 = TextNode("This is a text node", TextType.IMAGE, '../static/doge.png')
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
