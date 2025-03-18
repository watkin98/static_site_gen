import unittest
#import src.split_nodes_delimiter
from src.split_nodes_delimiter import *
#import src.textnode
from src.textnode import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        #self.assertEqual()