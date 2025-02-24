import unittest
from leafnode import *

class TestLeafNode(unittest.TestCase):
    def test(self):
        leafnode = LeafNode("p", "This is a paragraph of text.")
        leafnode1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        leafnode2 = LeafNode("p", "This is a paragraph of text.", 
                             {
                                "href": "https://www.google.com",
                                "target": "_blank",
                             }
                            )

        self.assertEqual(leafnode.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(leafnode1.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
        self.assertEqual(leafnode2.to_html(), "<p href=\"https://www.google.com\" target=\"_blank\">This is a paragraph of text.</p>")

        