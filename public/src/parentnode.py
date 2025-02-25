from htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Invalid HTML: tag required")
        
        if self.children == None:
            raise ValueError("Invalid ParentNode: parent node must have children")
        
        html_tag = ""

        for child in self.children:
            html_tag += child.to_html()

        return f"<{self.tag}>" + html_tag + f"</{self.tag}>"