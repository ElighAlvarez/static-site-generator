from block_utilities import *
from parentnode import ParentNode
import shutil, os
        
# returns a div ParentNode containing all of the block nodes 
# representing the provided markdown string
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = list(map(block_to_html_node, blocks))
    return ParentNode("div", html_nodes)

# overwrite the contents of the public directory with the static directory
def copy_static_to_public():
    if os.path.exists("public"):
        shutil.rmtree("public")
    shutil.copytree("static", "public")

# returns the text of the first h1 header
def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block[:2] == "# ":
            return block[2:]
    raise Exception("no h1 header found in markdown")