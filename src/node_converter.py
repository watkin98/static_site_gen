from src.textnode import *
from src.leafnode import *

def text_node_to_html_node(text_node):
    '''
    Takes in a TextNode object and returns an HTML LeafNode based on the former's TextType
    '''
    #print(f"In the converter: {text_node}\nType: {text_node.text_type}\nTest: {text_node.text_type.name}")
    match text_node.text_type.name:
        case TextType.TEXT.name:
            return LeafNode(value=text_node.text) 
        case TextType.BOLD.name:
            return LeafNode(tag='b', value=text_node.text)
        case TextType.ITALIC.name:
            return LeafNode(tag='i', value=text_node.text)
        case TextType.CODE.name:
            return LeafNode(tag='code', value=text_node.text)
        case TextType.LINK.name:
            return LeafNode(tag='a', value=text_node.text, props={"href" : f"{text_node.url}"})
        case TextType.IMAGE.name:
            return LeafNode(tag='img', value="", props={"src" : f"{text_node.url}", "alt" : f"{text_node.text}"})
        case _:
            raise ValueError("Must input a valid TextType")