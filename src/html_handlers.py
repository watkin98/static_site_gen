from src.block_handlers import *
from src.parentnode import *
from src.text_to_textnode_converter import *
from src.node_converter import *

import re

def markdown_to_html_node(markdown):
    '''
    Takes in a string (i.e. document) for markdown text and converts it into a single parent HTML node 
    (raw HTML text), potentially containing multiple child HTMLNode objects.
    '''
    # Turn the markdown text into a list of blocks
    md_blocks = markdown_to_blocks(markdown)
    #print(f"\nMarkdown: {md_blocks}")
    # Loop over the list to determine the BlockType for each block
    blocks = []

    for block in md_blocks:
        blocktype = block_to_block_type(block)
        #print(f"Block: {block}\nType: {blocktype}")

        # If block is anything except code, remove newline characters
        # If code, call helper function
        if blocktype.name != 'code':
            block = block.replace('\n', ' ')
        else:
            code_node = code_block_handler(block)
            blocks.append(code_node)
            continue

        # If block is anything else, parse inline children nodes
        inline_html_nodes = text_to_children(block)
        #print(inline_html_nodes)

        # Get html tag associated with blocktype
        html_tag = block_type_to_html_tag(blocktype)
        #print(f"Tag: {html_tag}")

        # Handle heading, unordered lists, and ordered lists
        if html_tag == 'h':
            # Determine how many #'s to remove from value
            html_tag = get_heading_number(block)
            heading_num = int(html_tag[1])
            inline_html_nodes[0].value = inline_html_nodes[0].value[heading_num+1:] 
        elif html_tag == 'blockquote':
            # Remove '> '
            inline_html_nodes[0].value = inline_html_nodes[0].value[2:]
        elif html_tag == 'ul':
            inline_html_nodes = ul_text_list_to_html_nodes(inline_html_nodes[0].value)
        elif html_tag == 'ol':
            inline_html_nodes = ol_text_list_to_html_nodes(inline_html_nodes[0].value)

        #print(f"\nInline Nodes: {inline_html_nodes}\nHTML Tag: {html_tag}")

        # Edge Case: The whole block consists only of a link
        if len(inline_html_nodes) == 1 and inline_html_nodes[0].tag == 'a':
            converted_block = inline_html_nodes[0]
        # Edge Case: The who block consists only of an image
        elif len(inline_html_nodes) == 1 and inline_html_nodes[0].tag == 'img':
            converted_block = inline_html_nodes[0]
        else:
            converted_block = ParentNode(html_tag, inline_html_nodes)
        #print(f"\nConverted HTML Node: {converted_block}")
        blocks.append(converted_block)

    #print(f"\nConverted Blocks: {blocks}")

    # Edge Case: entire markdown is just a link block
    #if blocks[0].children[0].tag == 'a':
    #    html_parent_node = ParentNode('div', children=[blocks[0].children[0]]+blocks[1:])
    #else:
    html_parent_node = ParentNode('div', children=blocks)

    #print(f"\nHTML: {html_parent_node}")

    return html_parent_node

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

def block_type_to_html_tag(blocktype):
    '''
    Takes in a BlockType enum tag and returns the associated HTML tag
    '''
    match blocktype.name:
        case 'paragraph':
            return 'p'
        case 'heading':
            return 'h'
        case 'code':
            raise ValueError("Code blocktype somehow got past the handler")
        case 'quote':
            return 'blockquote'
        case 'unordered_list':
            return 'ul'
        case 'ordered_list':
            return 'ol'
        case _:
            raise ValueError("Must be a valid BlockType")
        
def code_block_handler(md):
    '''
    Takes in a markdown code string and returns an HTML parent node with the code tag and string as the value
    '''
    code_string = md[3:-3]
    #code_string = code_string.replace('\n', '\\n')
    if code_string.startswith('\n'):
        code_string = code_string[1:]
    #print(f"\nCode String: {code_string}")
    code_node = TextNode(code_string, TextType.CODE)
    code_html = text_node_to_html_node(code_node)
    #print(f"\nCode Block: {code_html}")
    code_html_node = ParentNode('pre', [code_html])
    #print(f"\nHTML Code Node: {code_html_node}")
    return code_html_node

def get_heading_number(header):
    '''
    Takes in a markdown header string and returns the numbered HTML header tag
    '''
    header_syntax = {'#': 1, '##': 2, '###': 3, '####': 4, '#####': 5, '######': 6}
    header_substring = header.split(' ')[0]
    #print(f"\n{header_substring}")

    num_of_header_hashes = header_syntax[header_substring]

    return f'h{num_of_header_hashes}'

def ul_text_list_to_html_nodes(lst):
    '''
    Takes in a string that is supposed to be an unordered list block and returns a list (python)
    of HTML nodes
    '''
    html_nodes = []
    items_in_UL_list = lst.split('- ')
    items_in_UL_list = list(map(lambda x: x.strip(), items_in_UL_list[1:]))
    for item in items_in_UL_list:
        node = LeafNode('li', item)
        html_nodes.append(node)

    return html_nodes

def ol_text_list_to_html_nodes(lst):
    '''
    Takes in a string that is supposed to be an ordered list block and returns a list (python)
    of HTML nodes
    '''
    html_nodes = []
    items_in_OL_list = re.split(r'[0-9]\.', lst)
    new_list = list(filter(lambda x: x != '', items_in_OL_list))

    newer_list = list(map(lambda x: x.strip(), new_list))

    for item in newer_list:
        node = LeafNode('li', item)
        html_nodes.append(node)

    return html_nodes