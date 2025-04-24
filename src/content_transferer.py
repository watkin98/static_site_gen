import shutil
import os
import traceback

def main():
    try:
        static_to_public_transfer()
    except Exception as e:
        #print(f"Did not work, clearing public directory. \nException: {e}")
        traceback.print_exc()
        shutil.rmtree("../public/")
        os.mkdir("../public")

def static_to_public_transfer():
    # Delete files and directories existing in public and create new public directory
    shutil.rmtree("public/")
    os.mkdir("public/")

    # Transfer the files
    #print()
    file_transferer("static/")

def file_transferer(fpath):
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
    sub_path = fpath[6:]
    sub_path_new = ""

    if '.' in sub_path:
        #print("1")
        sub_path_new = sub_path.replace(file, '')
        #print(f"New Sub Dir: {sub_path_new}")

    #print(f"Path: {fpath}\nSub Path: {sub_path}\nFile: {file}")

    if sub_path_new == "":
        shutil.copy(f"{fpath}", "public/")
    elif os.path.exists(f"public/{sub_path_new}"):
        shutil.copy(fpath, f"public/{sub_path_new}")
    else:
        os.mkdir(f"public/{sub_path_new}")
        shutil.copy(f"{fpath}", f"public/{sub_path_new}")

main()