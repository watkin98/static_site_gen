import unittest
from src_test.htmlnode import *
from src_test.leafnode import *

class TestLeafNode(unittest.TestCase):
    def test(self):
        leafnode = LeafNode("p", "This is a paragraph of text.")
        leafnode1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        test_props = { 
                        "href": "https://www.google.com",
                        "target": "_blank",
                        }

        leafnode2 = LeafNode("p", "This is a paragraph of text.", test_props)
        leafnode3 = LeafNode(tag="p", props=test_props)
        leafnode4 = LeafNode(value="yolo mcswaggins")

        self.assertEqual(leafnode.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(leafnode1.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
        self.assertEqual(leafnode2.to_html(), "<p href=\"https://www.google.com\" target=\"_blank\">This is a paragraph of text.</p>")
        with self.assertRaises(ValueError):
            leafnode3.to_html()
        self.assertEqual(leafnode4.to_html(), "yolo mcswaggins")
        
                            

        