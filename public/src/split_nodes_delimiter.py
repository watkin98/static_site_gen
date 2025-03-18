from src.textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    '''
    Iterates through a list of TextNodes and splits each node into TEXT types nodes and all other types.
    Takes in a list of old TextNodes, a delimiter, and a TextNode type and returns a list of TextNodes that
    are split by the delimiter.
    '''
    new_nodes = []

    for node in old_nodes:
        if node.text_type != 'TEXT':
            new_nodes.append(node)

        split_text = node.text.split(delimiter)
        
        if len(split_text) != 3:
            raise ValueError("Invalid Markdown syntax detected")
        
        
        

    return new_nodes