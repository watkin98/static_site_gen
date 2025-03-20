from src.textnode import *
from src.md_links_extractor import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    '''
    Iterates through a list of TextNodes and splits each node into TEXT types nodes and the specified text_type.
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

def split_nodes_image(old_nodes):
    '''
    Iterates through a list of TextNodes and splits each node into Text nodes and Image nodes.
    Takes in a list of TextType nodes and returns a list of TextType nodes.
    '''
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        extracted_md_image_values = extract_markdown_images(node.text)
        temp = None
        firstRun = True
        print()
        for text_url_pair in extracted_md_image_values:
            if firstRun:
                extracted_text = (node.text).split(f"![{text_url_pair[0]}]({text_url_pair[1]})", 1)
            else:
                extracted_text = temp.split(f"![{text_url_pair[0]}]({text_url_pair[1]})", 1)
            print(f"Alt Text: {text_url_pair[0]}")
            print(f"Image URL: {text_url_pair[1]}")
            print(f"Extracted Text: {extracted_text}")

            new_text_textnode = TextNode(extracted_text[0], TextType.TEXT)
            new_image_textnode = TextNode(text_url_pair[0], TextType.IMAGE, url=text_url_pair[1])

            new_nodes.append(new_text_textnode)
            new_nodes.append(new_image_textnode)

            temp = "".join(extracted_text[1:])
            firstRun = False
            print(temp)

    return new_nodes

def split_nodes_link(old_nodes):
    '''
    Iterates through a list of TextNodes and splits each node into Text nodes and Link nodes.
    Takes in a list of TextType nodes and returns a list of TextType nodes.
    '''
    pass