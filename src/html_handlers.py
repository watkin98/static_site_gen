from src.block_handlers import *

def markdown_to_html_node(markdown):
    '''
    Takes in a string (i.e. document) for markdown text and converts it into a single parent HTMLNode,
    potentially containing multiple child HTMLNode objects.
    '''
    # Turn the markdown text into a list of blocks
    md_blocks = markdown_to_blocks(markdown)

    # Loop over the list to determine the BlockType for each block
    for block in md_blocks:
        blocktype = block_to_block_type(block)
        print(f"\nBlock: {block}\nType: {blocktype}")