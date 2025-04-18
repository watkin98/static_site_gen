import shutil
import os

def main():
    static_to_public_transfer()

def static_to_public_transfer():
    # Delete files and directories existing in public and create new public directory
    print(f"1")
    shutil.rmtree("../public/")
    os.mkdir("../public")
    print(f"2")

main()