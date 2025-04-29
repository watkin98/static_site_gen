from block_handlers import *
from html_handlers import *

def extract_title(markdown):
    '''
    Takes in a markdown file as a string and returns the title, which should be a line 
    starting with '# '
    '''
    
    md_blocks = markdown_to_blocks(markdown)
    first_line = md_blocks[0]
    h1_chars = first_line[0:2]

    if h1_chars == '# ':
        return first_line[2:]
    else:
        raise ValueError("h1 header not identified from markdown file")
    
def generate_page(from_path, template_path, dest_path):
    '''
    Takes in 'from_path', 'template_path', and 'dest_path' strings that represent file paths to generate
    an html page from a markdown file and a template html file.
    - from_path -> file path to markdown file
    - template_path -> file path to html template
    - dest_path -> file path to html page file
    '''
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    md_file = open(from_path)
    template_file = open(template_path)

    md_str = md_file.read()
    template_str = template_file.read()

    html_node = markdown_to_html_node(md_str)
    html = html_node.to_html()

    title_block = extract_title(md_str)

    template_with_title = template_str.replace('{{ Title }}', title_block)
    completed_template = template_with_title.replace('{{ Content }}', html)
    
    md_file.close()
    template_file.close()

    html_file = open(dest_path, mode='w')
    html_file.write(completed_template)
    html_file.close

    #print(md_str)
    #print(completed_template)
    #print(html_node)
    #print(html)
    #print(title_block)
