from textnode import *
from content_transferer import *
from page_generator import *

def main():
    obj = TextNode("This is a test", TextType.BOLD, "https://www.boot.dev")
    string = obj.__repr__
    #print(string)
    
    # Delete files and directories existing in public and create new public directory
    shutil.rmtree("public/")
    os.mkdir("public/")

    # Transfer files from static to public
    static_to_public_transfer()

    # Generate html page
    generate_page("content/index.md", "template.html", "public/index.html")

main()