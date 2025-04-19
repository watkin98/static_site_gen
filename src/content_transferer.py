import shutil
import os

def main():
    try:
        static_to_public_transfer()
    except Exception as e:
        print(f"Did not work, clearing public directory. \nException: {e}")
        shutil.rmtree("../public/")
        os.mkdir("../public")

def static_to_public_transfer():
    # Delete files and directories existing in public and create new public directory
    shutil.rmtree("../public/")
    os.mkdir("../public")

    # Transfer the files
    print()
    file_tranferer("../static")

def file_tranferer(fpath):
    print(f"Current File Path: {fpath}")
    # Get list of existing files and directories 
    a_file = os.path.exists(fpath)
    print(f"3 {a_file}")

    if not a_file:
        print(f"Item: {fpath}")
        shutil.copy(f"{fpath}/{item}", "../public")
    else:
        print(f"{fpath}\nCwd: {os.getcwd()}")
        entries = os.listdir(path=fpath)
        print(f"{entries}")

    for item in entries:
        item_is_a_file_1 = file_determiner(item)
        if item_is_a_file_1:
            shutil.copy(f"{fpath}/{item}", "../public")
        else:
            file_tranferer(item)

def file_determiner(fpath):
    '''
    Takes in a string that represents either a directory or a file. Return True if a file,
    false if a Directory
    '''
    dot_count = 0
    for char in fpath:
        if char == '.':
            dot_count += 1
    
    if dot_count == 1:
        return True
    
    return False

main()