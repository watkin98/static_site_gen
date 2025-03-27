from enum import Enum

BlockType = Enum('BlockType', ['paragraph', 'heading', 'code', 'quote', 'unordered_list', 'ordered_list'])

def markdown_to_blocks(markdown):
    '''
    Takes in a string (i.e. document) of markdown text and returns a list of block markdowns delimmited 
    by double newline characters (`\`n`\`n)
    '''
    markdown_lines = markdown.split("\n\n")
    #print(f"\n{markdown}")
    lines_stripped_of_whitespace = []
    for inline_markdown in markdown_lines:
        line = inline_markdown.strip()

        # Detect tab characters within inlines and remove them
        if '\n' in line:
            temp = inline_markdown.split('    ')
            temp1 = ''.join(temp)
            temp2 = temp1.strip()
            lines_stripped_of_whitespace.append(temp2)
        else:
            lines_stripped_of_whitespace.append(line)

    # Remove empty blocks due to excessive newlines
    lines_stripped_of_whitespace = [item for item in lines_stripped_of_whitespace if item != '']
    #print(f"\n{lines_stripped_of_whitespace}")
    return lines_stripped_of_whitespace

def block_to_block_type(markdown):
    '''
    Takes in a string (i.e. document) of markdown block text and returns the BlockType of the block
    (paragraph, heading, code, quote, unordered_list, oredered_list)
    '''
    # Identifier for markdown block headers
    header_syntax = ['# ', '## ', '### ', '#### ', '##### ', '###### ']
    potential_header_substring = markdown[0:8].strip('\n')
    lst = list(filter(lambda x: x in potential_header_substring, header_syntax))
    if lst != []:
        return BlockType.heading
    
    # Identifier for markdown block code
    potential_code_substring = markdown.strip('\n')
    if potential_code_substring[:3] == "```" and potential_code_substring[-3:] == "```":
        return BlockType.code
    
    # Identifier for markdown block code
    potential_quote_substring = markdown.split('\n')
    #print(f"\nlist: {potential_quote_substring}")
    # Remove empty blocks due to excessive newlines
    lines_stripped_of_whitespace = [item for item in potential_quote_substring if item != '']
    #print(f"\n{lines_stripped_of_whitespace}")
    isQuote = True
    for item in lines_stripped_of_whitespace:
        if item[0] != '>':
            isQuote = False
            break

    if isQuote:
        return BlockType.quote
    '''
    if potential_quote_substring[0] == '>':
        return BlockType.quote
    '''
    # Identifier for markdown block unordered_lists


    # Identifier for markdown block ordered_lists
    
    return BlockType.paragraph