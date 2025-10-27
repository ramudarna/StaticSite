import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_page, generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"
dir_path_docs = "./docs"

def main():
    # Get base path from the command line arguments or defaults to /
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print("Deleting public directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print ('Generating page')
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)

main()
