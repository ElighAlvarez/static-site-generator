from block_utilities import markdown_to_blocks, block_to_html_node
from parentnode import ParentNode
        
# returns a div ParentNode containing all of the block nodes 
# representing the provided markdown string
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = list(map(block_to_html_node, blocks))
    return ParentNode("div", html_nodes)
