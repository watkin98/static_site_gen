from src.block_handlers import *
from src.htmlnode import *

def markdown_to_html_node(markdown):
    '''
    Takes in a string (i.e. document) for markdown text and converts it into a single parent HTML node 
    (raw HTML text), potentially containing multiple child HTMLNode objects.
    '''
    # Turn the markdown text into a list of blocks
    md_blocks = markdown_to_blocks(markdown)
    print(f"\nMarkdown: {md_blocks}")
    # Loop over the list to determine the BlockType for each block
    for block in md_blocks:
        blocktype = block_to_block_type(block)
        print(f"Block: {block}\nType: {blocktype}")
        html_parent_node = HTMLNode()

        # If block is code, do not parse inline children nodes
        if blocktype == BlockType.code:
            pass

        # If block is anything else, parse inline children nodes
        text = ""
        inline_html_nodes = text_to_children(text)

def text_to_children(text):
    pass