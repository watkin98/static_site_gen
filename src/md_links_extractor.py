import re

def extract_markdown_images(text):
    '''
    Takes raw markdown text pertaining to an image as input and returns a list of tuples.
    Each tuple contains the alt text as its first index and the url of the image in the second index.
    '''
    # The regex below is the implementation I came up with. Bootdev's is the following: 
    # r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    #return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    
def extract_markdown_links(text):
    '''
    Takes raw markdown text pertaining to a url as input and returns a list of tuples.
    Each tuple contains the anchor text as its first index and the url in the second index.
    '''
    # The regex below is the implementation I came up with. Bootdev's is the following: 
    # r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)
    #print(f"\nWhat is happening: {text}")
    #return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)