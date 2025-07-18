#from textnode import *
from content_transferer import static_to_public_transfer
from page_generator import generate_page, generate_pages_recursive

import os
import sys
import shutil

def main():

    # Delete files and directories existing in public and create new public directory
    shutil.rmtree("docs/")
    os.mkdir("docs/")

    # Transfer files from static to public
    static_to_public_transfer()

    basepath = sys.argv
    if len(basepath) <= 1:
        basepath = '/'
    else:
        basepath = basepath[1]

    # Generate html page
    generate_pages_recursive("content", "template.html", "docs", basepath)


main()