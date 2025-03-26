
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
    #lines_stripped_of_whitespace = [item for item in lines_stripped_of_whitespace if item == '']
    '''
    for i in range(0, len(lines_stripped_of_whitespace)):
        if lines_stripped_of_whitespace[i] is '':
            del lines_stripped_of_whitespace[i]
    '''
    #print(f"\n{lines_stripped_of_whitespace}")
    return lines_stripped_of_whitespace