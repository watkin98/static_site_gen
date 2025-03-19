from src.textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    '''
    Iterates through a list of TextNodes and splits each node into TEXT types nodes and all other types.
    Takes in a list of old TextNodes, a delimiter, and a TextNode type and returns a list of TextNodes that
    are split by the delimiter.
    '''
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        split_text = node.text.split(delimiter)

        if len(split_text) == 1:
            new_nodes.append(node)
            continue

        if len(split_text) < 3:
            raise ValueError("Invalid Markdown syntax detected")
        else:
            # Edge case: first entry in string is a unique TextType
            if split_text[0] == '':
                split_text = split_text[1:]
                for i in range(0, len(split_text)):
                    if i % 2 == 1:
                        new_nodes.append(TextNode(split_text[i], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(split_text[i], text_type))
            # Edge case: last entry in string is a unique TextType
            elif split_text[len(split_text) - 1] == '': 
                split_text = split_text[:len(split_text) - 1]
                for i in range(0, len(split_text)):
                    if i % 2 == 0:
                        new_nodes.append(TextNode(split_text[i], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(split_text[i], text_type))
            else:
                for i in range(0, len(split_text)):
                    if i % 2 == 0:
                        new_nodes.append(TextNode(split_text[i], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(split_text[i], text_type))

    return new_nodes