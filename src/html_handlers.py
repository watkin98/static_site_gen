from src.block_handlers import *

def markdown_to_html_node(markdown):
    '''
    Takes in a string (i.e. document) for markdown text and converts it into a single parent HTMLNode,
    potentially containing multiple child HTMLNode objects.
    '''
    md_blocks = markdown_to_blocks(markdown)
    print(md_blocks)

    