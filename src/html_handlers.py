from src.block_handlers import *
from src.parentnode import *
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
            html_tag = get_heading_number(block)
            print(f"\n{inline_html_nodes[0].value}")
            inline_html_nodes[0].value = inline_html_nodes[0].value[2:] # 2 IS HARDCODED ATTN!!!!!!!!!!!!!!!!!
            print(f"\n{inline_html_nodes[0].value}")
            #print(f"Header Tag: {html_tag}")
        elif html_tag == 'ul':
            print(f"UL found!")
        elif html_tag == 'ol':
            print(f"OL found!")

        converted_block = ParentNode(html_tag, inline_html_nodes)
        blocks.append(converted_block)

    #print(f"Converted Blocks: {blocks}")

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
