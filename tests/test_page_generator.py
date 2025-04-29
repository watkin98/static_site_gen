import unittest
from src_test.page_generator import *

class TestPageGenerator(unittest.TestCase):
    def test_base(self):
        markdown = """
        # This is a h1 header

        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        test = extract_title(markdown)
        self.assertEqual(test, "This is a h1 header")

    def test_only_header(self):
        markdown = """
        # This is a h1 header
        """
        test = extract_title(markdown)
        self.assertEqual(test, "This is a h1 header")

    def test_misplaced_header(self):
        markdown = """
        This is **bolded** paragraph

        # This is a h1 header

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_h2(self):
        markdown = """
        ## This is a h1 header

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_h6(self):
        markdown = """
        ###### This is a h1 header

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        with self.assertRaises(ValueError):
            extract_title(markdown)
    
    def test_paragraph(self):
        markdown = """
        This is a paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        with self.assertRaises(ValueError):
            extract_title(markdown)
        
    #def test_generate_page(self):
    #    generate_page("content/index.md", "template.html", "public/index.html")