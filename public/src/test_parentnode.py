import unittest
from parentnode import *
from leafnode import *

class TestParentNode(unittest.TestCase):

    def test_provided(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_nested_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode("p", 
                           [LeafNode("b", "yolo mcswaggins")]
                           ),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<p><b>yolo mcswaggins</b></p><i>italic text</i>Normal text</p>")

    def test_empty_children(self):
        node = ParentNode(
            "p",
            []
        )

        self.assertEqual(node.to_html(), "<p></p>")

    def test_no_children(self):
        node = ParentNode(tag="p")

        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_tag(self):
        node = ParentNode(
            tag=None,
            children=
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode("p", 
                           [LeafNode("b", "yolo mcswaggins")]
                           ),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )

        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()