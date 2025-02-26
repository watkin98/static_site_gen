import unittest
import tests
from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a code node ", TextType.CODE)
        node4 = TextNode("This is a node of code,", TextType.CODE)
        node5 = TextNode("This is a text node", TextType.BOLD, url="www.urmom.com")
        node6 = TextNode("This is a text node", TextType.BOLD, url="www.urmom.com")
        node7 = TextNode("Different text node!", TextType.BOLD, url="www.urmom.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node2, node3)
        self.assertEqual(node5, node6)
        self.assertNotEqual(node6, node7)
        self.assertNotEqual(node5, node)




if __name__ == "__main__":
    unittest.main()