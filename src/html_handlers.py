from block_handlers import markdown_to_blocks
from block_handlers import block_to_block_type
from parentnode import ParentNode
from text_to_textnode_converter import text_to_textnodes
from node_converter import text_node_to_html_node
from textnode import TextType
from textnode import TextNode
from leafnode import LeafNode
from htmlnode import HTMLNode

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
        print(f"Block: \n{block}\nType: {blocktype}")

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
            #print("In UL logic")
            #print(f"Current nodes: {inline_html_nodes}")
            #print(f"Outgoing: {inline_html_nodes[0].value}")
            inline_html_nodes = ul_text_list_to_html_nodes(block)
            #inline_html_nodes = ul_text_list_to_html_nodes(inline_html_nodes[0].value)
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
    OLD: Takes in a string that is supposed to be an unordered list block and returns a list (python)
    of HTML nodes
    '''
    print(f"Incoming ul: {lst}")
    textnode_nodes = []
    html_nodes = []
    items_in_UL_list = lst.split('- ')[1:]
    print(f"List of UL: {items_in_UL_list}")
    for item in items_in_UL_list:
        textnode = text_to_textnodes(item)
        textnode_nodes.append(textnode)

    print(f"Textnodes: {textnode_nodes}")

    list_item_holder = []
    for list_item in textnode_nodes:
        for item in list_item:
            htmlnode = text_node_to_html_node(item)
            list_item_holder.append(htmlnode)
        html_nodes.append(list_item_holder)
        list_item_holder = []

    print(f"HTML Nodes: {html_nodes}")

    listnodes = []
    for item in html_nodes:
        if len(item) == 1:
            node = LeafNode('li', item[0].value)
            listnodes.append([node])
        else:
            node_holder = []
            for node in item:
                print(f"Node: {node}")
                if node.tag == None:
                    node = HTMLNode('li', node.value)
                    node_holder.append([node])
                else:
                    node = LeafNode(node.tag, node.value)
                    node_holder[len(node_holder) - 1][0].children = [node]
            listnodes.append(node_holder)

    print(f"Final Nodes: {listnodes}")

    final_list = []
    for item in listnodes:
        if len(item) == 1:
            final_list.append(item[0])
        else:
            print(item)
            for node in item:
                if item[0][0].children != None:
                    node[0].children.append(item)

    print(f"Final List: {final_list}")
    '''
    items_in_UL_list = list(map(lambda x: x.strip(), items_in_UL_list[1:]))
    for item in items_in_UL_list:
        node = LeafNode('li', item)
        html_nodes.append(node)
    '''
    raise ValueError("Not done yet!")
    #return html_nodes
'''
def ul_text_list_to_html_nodes(lst):
    ''
    Takes in a list of nodes that represent an unordered list block and its inline elements and returns
    a list of HTML nodes
    ''
    print(f"Incoming ul: {lst}")
    html_nodes = []
    for item in lst:
        if item.tag == None:
            print(f"Item: {item}")
            print("Tag is None!")
        else:
            print(f"Item: {item}")
            print("Tag is not None!")
        #node = LeafNode('li', item)
        #html_nodes.append(node)
    
    raise ValueError("Not done yet!")
    #return html_nodes
'''
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