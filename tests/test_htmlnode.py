import tests
from src.htmlnode import HTMLNode


import unittest
#from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test(self):
        test_props = {
            "href": "https://www.google.com",
            "target": "_blank",
            }
        test_props1 = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        test_props2 = {
            "href": "https://www.youtube.com",
            "target": "_blank",
        }
        node = HTMLNode(tag='p', value="Hello, remember me?", props=test_props)
        node1 = HTMLNode(tag="a", value="L + Bozo", props=test_props1)
        node2 = HTMLNode(tag="a", value="L + Bozo", props=test_props2)
        node3 = HTMLNode(tag='p', value="yo wassap")

        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
        self.assertEqual(node.props_to_html(), node1.props_to_html())
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())
        self.assertEqual(node3.props_to_html(), "")
