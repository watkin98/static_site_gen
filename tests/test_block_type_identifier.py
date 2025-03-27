import unittest
from src.block_handlers import *

class TestBlockTypeIdentifier(unittest.TestCase):
    def test_markdown_header(self):
        md = """
# This is header text
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.heading)

    def test_markdown_header_3_hashtags(self):
        md = """
### This is header text
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.heading)

    def test_markdown_header_6_hashtags(self):
        md = """
###### This is header text
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.heading)

    def test_markdown_header_7_hashtags(self):
        md = """
####### This is NOT header text
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_markdown_header_no_hashtags(self):
        md = """
 This is NOT header text
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_markdown_code(self):
        md = """
```This is a code block```
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.code)

    def test_markdown_code_with_trailing_and_preceeding_whitespace(self):
        md = """
``` This is a code block ```
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.code)
    
    def test_markdown_code_incorrect_preceeding_tics(self):
        md = """
``This is a code block```
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_markdown_code_incorrect_trailing_tics(self):
        md = """
```This is a code block``
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_markdown_quote(self):
        md = """
> This is a quote
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.quote)

    def test_markdown_quote1(self):
        md = """
>This is a quote
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.quote)

    def test_markdown_quote(self):
        md = """
>>This is a quote
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.quote)

    def test_markdown_quote_trailing_chevron(self):
        md = """
This is NOT a quote >
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_markdown_false_quote(self):
        md = """
This is a quote
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.paragraph)

    
