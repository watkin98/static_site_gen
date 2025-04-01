from enum import Enum

TextType = Enum('TextType', ['TEXT', 'BOLD', 'ITALIC', 'CODE', 'LINK', 'IMAGE'])
'''
Type identifier for a TextNode (ex. 'TEXT', 'BOLD', 'IMAGE')
'''

class TextNode():
    '''
    A class for tokenizing raw inline text from markdown or HTML into a program object that we can write 
    logic for and interact with.
    '''
    def __init__(self, text, text_type, url=None):
        self.text = text 
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"