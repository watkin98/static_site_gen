import unittest
from src.textnode import *
from src.node_splitter import *

class LinkAndImageSplitterTest(unittest.TestCase):
    '''
    def test_bootdev_1(self):
        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        test_case = [
                        TextNode("This is text with a link ", TextType.TEXT),
                        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                        TextNode(" and ", TextType.TEXT),
                        TextNode(
                            "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                        ),
                    ]
        self.assertEqual(new_nodes, test_case)
    '''
    def test_split_images_bootdev(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        #print(f"\n{new_nodes}")
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
        for node in new_nodes:
            print(node.__repr__)
    