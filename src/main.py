from block_utilities import block_to_block_type, markdown_to_blocks


def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    block_types = list(map(block_to_block_type, blocks))
    nodes = []
    for block, type in zip(blocks, block_types):
        pass

def main():
    pass

if __name__ == '__main__':
    main()
