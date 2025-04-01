class HTMLNode():
    '''
    Used to generate representations of "nodes" in an HTML document tree. The objects can be either 
    block level or inline and are designed to output raw HTML.
    '''
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        '''
        Takes in an HTMLNode and returns an HTML string of the attributes associated with that node.
        '''
        if self.props is None:
            return ""

        attributes_string = ""
        for attribute in self.props:
            attributes_string += f" {attribute}=\"{self.props[attribute]}\""
        return attributes_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"