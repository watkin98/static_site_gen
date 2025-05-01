from src.textnode import TextNode
from src.textnode import TextType
from src.node_splitter import split_nodes_delimiter
from src.node_splitter import split_nodes_image
from src.node_splitter import split_nodes_link


def text_to_textnodes(text):
    '''
    Takes in a raw string of markdown text and returns a list of textnodes tokenized by markdown syntax
    '''
    textnodes = []

    starter_node = TextNode(text, TextType.TEXT)
    bold_nodes = split_nodes_delimiter([starter_node], '**', TextType.BOLD)
    textnodes = bold_nodes
    #print(f"\nBold Nodes Processed: {textnodes}")

    italic_nodes = split_nodes_delimiter(textnodes, '_', TextType.ITALIC)
    textnodes = italic_nodes
    #print(f"\nItalic Nodes Processed: {textnodes}")

    code_nodes = split_nodes_delimiter(textnodes, '`', TextType.CODE)
    textnodes = code_nodes
    #print(f"\nCode Nodes Processed: {textnodes}")

    image_nodes = split_nodes_image(textnodes)
    textnodes = image_nodes
    #print(f"\nImage Nodes Processed: {textnodes}")

    link_nodes = split_nodes_link(textnodes)
    textnodes = link_nodes
    #print(f"\nLink Nodes Processed: {textnodes}")

    return textnodes