import unittest
from src.html_handlers import *

class TestMdToHTMLNodeConverter(unittest.TestCase):
    def test_html_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\nHTML: {html}")
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\nCon HTML: {html}\nTst HTML: <div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>")
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_html_paragraph_with_heading(self):
        md = """
# This is a heading

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\nCon HTML: {html}\nTst HTML: <div><h1>This is a heading</h1><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>")
        self.assertEqual(
            html,
            "<div><h1>This is a heading</h1><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_html_paragraph_with_multi_heading(self):
        md = """
### This is a heading

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\nHTML: {html}")
        self.assertEqual(
            html,
            "<div><h3>This is a heading</h3><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_quotes(self):
        md = """
> This is a quote

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\nHTML: {html}")
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote</blockquote></div>",
        )

    def test_quotes_extended(self):
        md = """
> This is a quote

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\nHTML: {html}")
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote</blockquote><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_quotes_extended_end(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

> This is a quote

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\nHTML: {html}")
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p><blockquote>This is a quote</blockquote></div>",
        )

    def test_unordered_lists(self):
        md = """
- Item 1
- Item 2
- Item 3    

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\nHTML: {html}")
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>",
        )

    def test_unordered_lists_extended(self):
        md = """
- Item 1
- Item 2
- Item 3

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\nHTML: {html}")
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
'''
    def test_ordered_lists(self):
        md = """
1. Item 1
2. Item 2
3. Item 3

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\nHTML: {html}")
        self.assertEqual(
            html,
            "<div><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol></div>",
        )

    def test_ordered_lists_extended(self):
        md = """
1. Item 1
2. Item 2
3. Item 3

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\nHTML: {html}")
        self.assertEqual(
            html,
            "<div><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_links(self):
        md = """
This is a paragraph with a [link](https://www.google.com).

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\nHTML: {html}")
        self.assertEqual(
            html,
            "<div><p>This is a paragraph with a <a href=\"https://www.google.com\">link</a></p></div>",
        )

    def test_links_extended(self):
        md = """
This is a paragraph with a [link](https://www.google.com).

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\nHTML: {html}")
        self.assertEqual(
            html,
            "<div><p>This is a paragraph with a <a href=\"https://www.google.com\">link</a></p><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_images(self):
        md = """
![alt text for image](url/of/image.jpg)

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\nHTML: {html}")
        self.assertEqual(
            html,
            "<div><img src=\"url/of/image.jpg\" alt=\"Description of image\"></div>",
        )

    def test_images_extended(self):
        md = """
![alt text for image](url/of/image.jpg)

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"\nHTML: {html}")
        self.assertEqual(
            html,
            "<div><img src=\"url/of/image.jpg\" alt=\"Description of image\"><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
'''