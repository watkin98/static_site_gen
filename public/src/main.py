from textnode import *

def main():
    obj = TextNode("This is a test", TextType.BOLD, "https://www.boot.dev")
    string = obj.__repr__
    print(string)

main()