from textnode import TextNode, TextType
import re

# returns the TextNode representation of a string input text
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes

# returns a list of nodes with delimiter-delimited sections converted
# into text_type TextNodes. Returned nodes maintains ordering of the text
# within old_nodes. Does not remove nodes that are not converted.
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        # We only care about TEXT nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        temp_node_strs = node.text.split(delimiter)
        # if there are an even number of strings left over, there were an odd number of delimiters,
        # so we combine the last two segments and reinsert the delimiter
        if len(temp_node_strs) > 1 and len(temp_node_strs) % 2 == 0:
            temp_node_strs[-2] = f"{temp_node_strs[-2]}{delimiter}{temp_node_strs[-1]}"
            temp_node_strs.pop()
        # the first type should be normal text, then alternate between text_type and normal
        temp_nodes = []
        for i in range(0, len(temp_node_strs)):
            if i % 2 == 0:
                temp_nodes.append(TextNode(temp_node_strs[i], TextType.TEXT))
            else:
                temp_nodes.append(TextNode(temp_node_strs[i], text_type))
        # remove blank text nodes at beginning and end
        if len(temp_nodes) > 0 and temp_nodes[0].text == "":
            temp_nodes.pop(0)
        if len(temp_nodes) > 0 and temp_nodes[-1].text == "":
            temp_nodes.pop()
        for node in temp_nodes:
            new_nodes.append(node)
    return new_nodes

# returns a list of nodes, where TextNodes with type TEXT have been
# split into TEXT and IMAGE nodes if applicable.
def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        # We only care about TEXT nodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        matches = extract_markdown_images(text)
        for match in matches:
            # split around first occurrence of match
            splits = text.split(f"![{match[0]}]({match[1]})", 1)
            # put last split bach into text to search for remaining matches
            text = splits[1]
            # build normal node with previous text as long as its not an empty string
            # and create image nodes with match
            if splits[0] != "":
                new_nodes.append(TextNode(splits[0], TextType.TEXT))
            new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
        # Add remaining text if it exists
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

# returns a list of nodes, where TextNodes with type TEXT have been
# split into TEXT and LINK nodes if applicable.
def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        # We only care about TEXT nodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        matches = extract_markdown_links(text)
        for match in matches:
            # split around first occurrence of match
            splits = text.split(f"[{match[0]}]({match[1]})", 1)
            # put last split bach into text to search for remaining matches
            text = splits[1]
            # build normal node with previous text as long as its not an empty string
            # and create image nodes with match
            if splits[0] != "":
                new_nodes.append(TextNode(splits[0], TextType.TEXT))
            new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
        # Add remaining text if it exists
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

# returns a list of (text, filepath) tuples, one tuple for each image tag
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

# returns a list of (text, url) tuples, one tuple for each link tag
def extract_markdown_links(text):
    return re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
