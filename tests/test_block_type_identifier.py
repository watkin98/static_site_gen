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
This is NOT a quote
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_markdown_quote_multiline(self):
        md = """
> This is a quote
> with
> multiple lines.
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.quote)

    def test_markdown_quote_multiline_false(self):
        md = """
> This is a quote
> with
> multiple lines
sike!
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_markdown_quote_multiline_false1(self):
        md = """
This is a quote
> with
> multiple lines
> sike!
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_markdown_unordered_list(self):
        md = """
- Apples
- Bananas
- Pears
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.unordered_list)

    def test_markdown_unordered_list1(self):
        md = """
- Apples
- Bananas
- Pears
- Carrots
- Cucumbers
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.unordered_list)

    def test_markdown_unordered_list_false(self):
        md = """
Apples
- Bananas
- Pears
- Carrots
- Cucumbers
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_markdown_unordered_list_false1(self):
        md = """
-Apples
- Bananas
- Pears
- Carrots
- Cucumbers
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_markdown_unordered_list_false2(self):
        md = """
- Apples
- Bananas
- Pears
- Carrots
Cucumbers
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_markdown_unordered_list_false3(self):
        md = """
- Apples
- Bananas
- Pears
- Carrots
-Cucumbers
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_markdown_unordered_list_false4(self):
        md = """
- Apples
- Bananas
- Pears
- Carrots
C - ucumbers
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_markdown_ordered_list(self):
        md = """
1. Apples
2. Bananas
3. Pears
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.ordered_list)

    def test_markdown_ordered_list1(self):
        md = """
1. Apples
2. Bananas
3. Pears
4. Carrots
5. Cucumbers
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.ordered_list)

    def test_markdown_ordered_list2(self):
        md = """
1. Apples
2. Bananas
3. Pears
4. Carrots
5. Cucumbers
6. Cake
7. Milk
8. Chips
9. Salsa
10. Dog Kibble
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.ordered_list)

    def test_markdown_ordered_list_100(self):
        md = """
1. Apples  
2. Bananas  
3. Oranges  
4. Grapes  
5. Strawberries  
6. Blueberries  
7. Raspberries  
8. Lemons  
9. Limes  
10. Avocados  
11. Tomatoes  
12. Cucumbers  
13. Lettuce  
14. Spinach  
15. Kale  
16. Broccoli  
17. Cauliflower  
18. Carrots  
19. Celery  
20. Bell peppers  
21. Onions  
22. Garlic  
23. Potatoes  
24. Sweet potatoes  
25. Zucchini  
26. Squash  
27. Green beans  
28. Snap peas  
29. Mushrooms  
30. Corn  
31. Cabbage  
32. Brussels sprouts  
33. Ginger  
34. Parsley  
35. Cilantro  
36. Basil  
37. Milk  
38. Eggs  
39. Butter  
40. Yogurt  
41. Cheese  
42. Cream cheese  
43. Sour cream  
44. Half & half  
45. Almond milk  
46. Orange juice  
47. Chicken breast  
48. Ground beef  
49. Pork chops  
50. Bacon  
51. Sausage  
52. Deli turkey  
53. Ham  
54. Salmon  
55. Tuna  
56. Shrimp  
57. Rice  
58. Pasta  
59. Spaghetti  
60. Macaroni  
61. Bread  
62. Bagels  
63. Tortillas  
64. Crackers  
65. Cereal  
66. Oatmeal  
67. Granola  
68. Flour  
69. Sugar  
70. Brown sugar  
71. Honey  
72. Maple syrup  
73. Peanut butter  
74. Jam  
75. Ketchup  
76. Mustard  
77. Mayonnaise  
78. Soy sauce  
79. Hot sauce  
80. Olive oil  
81. Vegetable oil  
82. Vinegar  
83. Salt  
84. Pepper  
85. Cinnamon  
86. Chili powder  
87. Cumin  
88. Paprika  
89. Coffee  
90. Tea  
91. Bottled water  
92. Soda  
93. Juice boxes  
94. Chips  
95. Popcorn  
96. Cookies  
97. Ice cream  
98. Frozen veggies  
99. Frozen pizza  
100. Frozen berries  
101. Queso
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.ordered_list)

    def test_markdown_ordered_list_fewer_than_10(self):
        md = """
1. Apples
2. Bananas
3. Pears
4. Carrots
5. Cucumbers
6. Cake
7. Milk
8. Chips
9. Salsa
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.ordered_list)

    def test_markdown_ordered_list_0(self):
        md = """
0. Apples
1. Bananas
2. Pears
3. Carrots
4. Cucumbers
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_markdown_ordered_list_negative(self):
        md = """
-1. Apples
0. Bananas
1. Pears
2. Carrots
3. Cucumbers
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_markdown_ordered_list_incorrect_numbering(self):
        md = """
1. Apples
3. Bananas
5. Pears
7. Carrots
9. Cucumbers
"""

        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.paragraph)

    # Bootdev test
    def test_block_to_block_types_bootdev(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.quote)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)
