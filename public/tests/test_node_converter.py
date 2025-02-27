import unittest
import tests
from src.textnode import *
from src.node_converter import *

class TestNodeConverter(unittest.TestCase):
    def test(self):
        text_node = TextNode("yolo mcswaggins", TextType.TEXT)
        leafnode = text_node_to_html_node(text_node)
        print(f"LeafNode: {leafnode.to_html()}")
        print(f"leafnode: {type(leafnode)}")
        self.assertIs(leafnode, LeafNode)