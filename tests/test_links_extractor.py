import unittest
from src_test.md_links_extractor import *

class TestExtractor(unittest.TestCase):

    # Below are the tests provided by Boot.dev
    def test_bootdev_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
                            [
                                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
                                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
                            ], 
                            extract_markdown_images(text)
                        )
    
    def test_bootdev_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(
                            [
                                ("to boot dev", "https://www.boot.dev"), 
                                ("to youtube", "https://www.youtube.com/@bootdotdev")
                            ],
                            extract_markdown_links(text)
                        )
    
    def test_extract_markdown_images_bootdev(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )