from textnode import *
from content_transferer import *

def main():
    obj = TextNode("This is a test", TextType.BOLD, "https://www.boot.dev")
    string = obj.__repr__
    #print(string)

    static_to_public_transfer()

main()