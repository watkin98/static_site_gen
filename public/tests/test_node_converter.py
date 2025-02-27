import unittest
import tests
from src.textnode import *
from src.node_converter import *

class TestNodeConverter(unittest.TestCase):
    def test_text_node(self):
        text_node = TextNode("yolo mcswaggins", TextType.TEXT)
        leafnode = text_node_to_html_node(text_node)
        self.assertEqual(type(leafnode), LeafNode)

    def test_text_provided(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("Bold move cotton, let's see if it pays off", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "Bold move cotton, let's see if it pays off")

    def test_italic(self):
        node = TextNode("it's a me, a mario", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "it's a me, a mario")

    def test_code(self):
        node = TextNode("dey terk er codr jerbs", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "dey terk er codr jerbs")

    def test_link(self):
        node = TextNode("sauce?", TextType.LINK, "www.images.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "sauce?")
        self.assertEqual(html_node.props_to_html(), f" href=\"{node.url}\"")

    def test_image(self):
        node = TextNode("pics or it didn't happen", TextType.IMAGE, "www.images.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props_to_html(), f" src=\"{node.url}\" alt=\"{node.text}\"")

    def test_image_provided(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold_provided(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")