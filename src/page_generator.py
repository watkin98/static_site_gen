from src.block_handlers import *
from src.html_handlers import *

def extract_title(markdown):
    
    md_blocks = markdown_to_blocks(markdown)
    first_line = md_blocks[0]
    h1_chars = first_line[0:2]

    if h1_chars == '# ':
        return first_line[2:]
    else:
        raise ValueError("h1 header not identified from markdown file")
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    md_file = open(from_path)
    template_file = open(template_path)

    md_str = md_file.read()
    template_str = template_file.read()

    html_node = markdown_to_html_node(md_str)
    html = html_node.to_html()
    
    #print(md_str)
    #print(template_str)
    #print(html_node)
    print(html)
