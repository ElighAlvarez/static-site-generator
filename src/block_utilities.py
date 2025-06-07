from enum import Enum
from types import CodeType


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

# separates a string into a list of blocks
# blocks are defined as strings separated by two newlines
def markdown_to_blocks(markdown):
    split_blocks = markdown.split("\n\n")
    stripped_blocks = map(lambda block: block.strip(), split_blocks)
    filtered_blocks = filter(lambda block: block != "", stripped_blocks)
    return list(filtered_blocks)

# returns the BlockType of the block string supplied
def block_to_block_type(block_text):
    lines = block_text.split("\n")
    # HEADING
    i = 0 # assume block_text != ""
    while len(block_text) > i and block_text[i] == "#":
        i += 1
    if len(block_text) > i and i < 7 and block_text[i] == " ": # assume " " cannot be the first char
        return BlockType.HEADING
    # CODE
    if len(block_text) >= 6 and block_text[0:3] == "```" and block_text[-3:] == "```":
        return BlockType.CODE
    # QUOTE
    is_quote = True
    for line in lines:
        if len(line) < 1 or line[0] != ">":
            is_quote = False
    if is_quote:
        return BlockType.QUOTE
    # UNORDERED_LIST
    is_ul = True
    for line in lines:
        if len(line) < 2 or line[0:2] != "- ":
            is_ul = False
    if is_ul:
        return BlockType.UNORDERED_LIST
    # ORDERED_LIST
    is_ol = True
    for i in range(0, len(lines)):
        if len(lines[i]) < 3 or lines[i][0:3] != f"{i + 1}. ":
            is_ol = False
    if is_ol:
        return BlockType.ORDERED_LIST
    # PARAGRAPH
    return BlockType.PARAGRAPH
