from enum import Enum
import math

#BlockType = Enum('BlockType', ['paragraph', 'heading', 'code', 'quote', 'unordered_list', 'ordered_list'])

class BlockType(Enum):
    paragraph = 'paragraph'
    heading = 'heading'
    code = 'code'
    quote = 'quote'
    unordered_list = 'unordered_list'
    ordered_list = 'ordered_list'

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
    
    # Identifier for markdown block quote
    potential_quote_substring = markdown.split('\n')
    # Remove empty blocks due to excessive newlines
    lines_stripped_of_whitespace = [item for item in potential_quote_substring if item != '']
    is_quote = True
    for item in lines_stripped_of_whitespace:
        if item[0] != '>':
            is_quote = False
            break

    if is_quote:
        return BlockType.quote
    
    # Identifier for markdown block unordered_lists
    potential_unordered_list_substring = markdown.split('\n')
    # Remove empty blocks due to excessive newlines
    lines_stripped_of_whitespace = [item for item in potential_unordered_list_substring if item != '']
    is_unordered = True
    for item in lines_stripped_of_whitespace:
        if item[0:2] != '- ':
            is_unordered = False
            break

    if is_unordered:
        return BlockType.unordered_list

    # Identifier for markdown block ordered_lists
    potential_ordered_list_substring = markdown.split('\n')
    # Remove empty blocks due to excessive newlines
    lines_stripped_of_whitespace = [item for item in potential_ordered_list_substring if item != '']
    is_ordered = True

    for i in range(0, len(lines_stripped_of_whitespace)):
        # Funky syntax below used to account for lists increasing by orders of magnitude (ex. 1 -> 10 -> 100)
        if lines_stripped_of_whitespace[i][0:(3+(math.floor(math.log10(i+1))))] != f"{i + 1}. ": 
            is_ordered = False
            break

    if is_ordered:
        return BlockType.ordered_list

    # Should all checks fail, identify the block as a paragraph BlockType
    return BlockType.paragraph