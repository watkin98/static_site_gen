import shutil
import os
import traceback

def main():
    try:
        static_to_public_transfer()
    except Exception as e:
        print(f"Did not work, clearing public directory. \nException: {e}")
        traceback.print_exc()
        shutil.rmtree("../public/")
        os.mkdir("../public")

def static_to_public_transfer():
    # Delete files and directories existing in public and create new public directory
    shutil.rmtree("../public/")
    os.mkdir("../public")

    # Transfer the files
    print()
    file_transferer("../static")

'''
def file_tranferer(fpath):
    print(f"Current File Path: {fpath}")
    # Get list of existing files and directories 
    a_file = os.path.exists(fpath)
    print(f"3 {a_file}")

    if not a_file:
        #print(f"Item: {fpath}\nPath: {fpath}/{item}")
        os.mkdir(f"../public/{fpath}")
        shutil.copy(f"{fpath}", "../public")
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
'''
def file_transferer(fpath):
    directory_entires = os.listdir(path=fpath)
    print(f'{directory_entires}')
    
    for item in directory_entires:
        working_dir = f"../static/{item}"
        print(f"Dir: {working_dir}")
        a_file = os.path.isfile(working_dir)
        print(f"Item {item} is a file: {a_file}\nCwd: {working_dir}")
        if a_file:
            pass
            # Copy the file to public

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