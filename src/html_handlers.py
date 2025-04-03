from src.block_handlers import *
from src.htmlnode import *
from src.text_to_textnode_converter import *
from src.node_converter import *

def markdown_to_html_node(markdown):
    '''
    Takes in a string (i.e. document) for markdown text and converts it into a single parent HTML node 
    (raw HTML text), potentially containing multiple child HTMLNode objects.
    '''
    # Turn the markdown text into a list of blocks
    md_blocks = markdown_to_blocks(markdown)
    #print(f"\nMarkdown: {md_blocks}")
    # Loop over the list to determine the BlockType for each block
    html_nodes = []
    for block in md_blocks:
        blocktype = block_to_block_type(block)
        #print(f"Block: {block}\nType: {blocktype}")
        html_parent_node = HTMLNode()

        # If block is code, do not parse inline children nodes
        if blocktype == BlockType.code:
            pass

        # If block is anything else, parse inline children nodes
        inline_html_nodes = text_to_children(block)
        html_nodes.extend(inline_html_nodes)

    print(f"HTML: {html_nodes}")

def text_to_children(text):
    '''
    Takes in a string of raw markdown text and returns a list of HTML nodes tokenized by inline type
    '''
    #print(f"Helper Fcn: {text}")
    tokenized_textnodes = text_to_textnodes(text)
    #print(f"Textnodes: {tokenized_textnodes}")

    html_nodes = []
    for textnode in tokenized_textnodes:
        #print(f"Textnode: {textnode}")
        html_node = text_node_to_html_node(textnode)
        html_nodes.append(html_node)

    return html_nodes
    #print(f"HTML Nodes: {html_nodes}")