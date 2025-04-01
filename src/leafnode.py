from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    '''
    A Type of HTMLNode that represents a single HTML tag and accompanying text with no children.
    '''
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
