import shutil
import os
import traceback

# Testing stuff
'''
def main():
    try:
        static_to_public_transfer()
    except Exception as e:
        #print(f"Did not work, clearing public directory. \nException: {e}")
        traceback.print_exc()
        shutil.rmtree("../public/")
        os.mkdir("../public")
        '''

def static_to_public_transfer():
    '''
    Initiates the transfer of items in static directory to public. Requires that the 
    function is called while program is executed from project root (static_site_gen), ideally
    accomplished with a script.
    '''
    # Delete files and directories existing in public and create new public directory
    shutil.rmtree("public/")
    os.mkdir("public/")

    # Transfer the files
    #print()
    file_transferer("static/")

def file_transferer(fpath):
    '''
    Takes in the relative directory path "static/" and undergoes the tasks to transfer the files to 
    "public/".
    '''
    a_file = os.path.isfile(fpath)
    #print(f"Current fpath: {fpath}")

    if not a_file:
        directory_entires = os.listdir(path=fpath)
        #print(f'{directory_entires}')

    temp_dir = fpath
    
    for item in directory_entires:
        working_dir = f"{temp_dir}/{item}"
        #print(f"Dir: {working_dir}")
        a_file = os.path.isfile(working_dir)
        #print(f"Item {item} is a file: {a_file}\nCwd: {working_dir}")
        if a_file:
            file_copier(working_dir, item)
        else:
            # Create new path for item in public if necessary
            #os.mkdir(f"../public/{item}")
            #print(f"Recursive Dir: {working_dir}\nfpath: {fpath}")
            file_transferer(working_dir)

def file_copier(fpath, file):
    '''
    Takes in a relative file path and file (or directory) name and makes a copy to the public directory.
    '''

    # Remove the 'static/' from the string path
    sub_path = fpath[6:]
    sub_path_new = ""

    # If the fpath leads to a file, extract the string of the path preceeding it.
    if '.' in sub_path:
        #print("1")
        sub_path_new = sub_path.replace(file, '')
        #print(f"New Sub Dir: {sub_path_new}")

    #print(f"Path: {fpath}\nSub Path: {sub_path}\nFile: {file}")

    # If a directory, make a copy to the public directory. If the directory already exists, copy the
    # file to it. If neither are true, subdirectory does not exist. Make it and copy the file to it.
    if sub_path_new == "":
        shutil.copy(f"{fpath}", "public/")
    elif os.path.exists(f"public/{sub_path_new}"):
        shutil.copy(fpath, f"public/{sub_path_new}")
    else:
        os.mkdir(f"public/{sub_path_new}")
        shutil.copy(f"{fpath}", f"public/{sub_path_new}")

#main()