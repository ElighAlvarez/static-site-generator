import unittest
from block_utilities import *

class TestBlockUtilities(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_paragraph(self):
        block = "####### I look like a heading but I'm just a lonely paragraph..."
        expected = BlockType.PARAGRAPH
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_heading(self):
        block = "###### I'm just a lonely 6 heading"
        expected = BlockType.HEADING
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_code(self):
        block = """
```
I'm a big 'ol block 'o CODE!!!
```
""".strip()
        expected = BlockType.CODE
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_quote(self):
        block = """
>Quote from person 1...
>Yet another quote...
>Part of the same quoooote!
""".strip()
        expected = BlockType.QUOTE
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_ul(self):
        block = """
- Item 1
- milk
- eggos
""".strip()
        expected = BlockType.UNORDERED_LIST
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_ol(self):
        block = """
1. Ordered
2. Lists
3. Are
4. SO
5. COOL!!
""".strip()
        expected = BlockType.ORDERED_LIST
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
