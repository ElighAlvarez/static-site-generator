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

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()

    title = extract_title(markdown)
    body_html = markdown_to_html_node(markdown).to_html()
    output = template.replace("{{ Title }}", title).replace("{{ Content }}", body_html)

    dest_dir = os.sep.join(dest_path.split(os.sep)[:-1])
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    with open(dest_path, "w") as f:
        f.write(output)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_contents = os.listdir(dir_path_content)
    for item in dir_contents:
        item_path = f"{dir_path_content}{os.sep}{item}"
        dest_path = f"{dest_dir_path}{os.sep}{item}"
        if os.path.isdir(item_path):
            os.mkdir(dest_path)
            generate_pages_recursive(item_path, template_path, dest_path)
        else:
            generate_page(item_path, template_path, dest_path.replace(".md", ".html"))
