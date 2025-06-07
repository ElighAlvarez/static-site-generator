import unittest
from utilities import *

class TestUtilities(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_extract_title_1(self):
        markdown = """
# An easy header
"""
        actual = extract_title(markdown)
        expected = "An easy header"
        self.assertEqual(expected, actual)

    def test_extract_title_2(self):
        markdown = """
## A fake header
"""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "no h1 header found in markdown")

    def test_extract_title_3(self):
        markdown = """
some metadata

# A harder header

other document stuff
"""
        actual = extract_title(markdown)
        expected = "A harder header"
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()