from textnode import *
from leafnode import *

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text) 
        case TextType.BOLD:
            return
        case TextType.ITALIC:
            return
        case TextType.CODE:
            return
        case TextType.LINK:
            return
        case TextType.IMAGE:
            return
        case __:
            return