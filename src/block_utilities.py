from enum import Enum
from leafnode import LeafNode
from parentnode import ParentNode
from inline_utilities import text_to_textnodes

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
    if len(block_text) >= 6 and block_text[0:4] == "```\n" and block_text[-4:] == "\n```":
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

# returns a list of HTMLNodes that represents the provided block string
def block_to_html_node(block):
    type = block_to_block_type(block)
    match type:
        case BlockType.PARAGRAPH:
            single_line = block.replace("\n", " ")
            text_nodes = text_to_textnodes(single_line)
            children = list(map(lambda node: node.to_html_node(), text_nodes))
            return ParentNode("p", children)
        case BlockType.HEADING:
            split = block.split(" ", 1)
            heading_size = len(split[0])
            return LeafNode(f"h{heading_size}", split[1])
        case BlockType.CODE:
            text = block.split("\n", 1)[1].strip("```")
            child = LeafNode("code", text)
            return ParentNode("pre", [child])
        case BlockType.QUOTE:
            lines = block.split("\n")
            text = "\n".join(list(map(lambda line: line[1:], lines)))
            return LeafNode("blockquote", text)
        case BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            bullets = list(map(lambda line: line[2:], lines))
            children = list(map(
                lambda bullet: ParentNode(
                    "li", 
                    list(map(lambda node: node.to_html_node(), text_to_textnodes(bullet)))
                ), 
                bullets
            ))
            return ParentNode("ul", children)
        case BlockType.ORDERED_LIST:
            lines = block.split("\n")
            bullets = list(map(lambda line: line[3:], lines))
            children = list(map(
                lambda bullet: ParentNode(
                    "li", 
                    list(map(lambda node: node.to_html_node(), text_to_textnodes(bullet)))
                ), 
                bullets
            ))
            return ParentNode("ol", children)
