#from textnode import *
from content_transferer import static_to_public_transfer
from page_generator import generate_page, generate_pages_recursive

import os
import shutil

def main():

    # Delete files and directories existing in public and create new public directory
    shutil.rmtree("public/")
    os.mkdir("public/")

    # Transfer files from static to public
    static_to_public_transfer()

    # Generate html page
    #generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content", "template.html", "public")

main()