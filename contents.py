#!/usr/bin/python3
# coding: utf-8

# List the contents of object files in the `objects` directory.

from subprocess import run
from os import listdir
import sys

def list_sha():
    sha_list = []
    objects = ".git/objects"
    for directory in listdir(objects):
        if len(str(directory)) <= 2:
            sha_list.append(directory + listdir(objects + "/" + directory)[0])
    return sha_list
    
def retreive_content(sha):
    object_content = run(f"git cat-file -p {sha}", shell=True, capture_output=True).stdout.decode("unicode_escape")
    return object_content

def dict_content():
    content_dict = {}
    for sha in list_sha():
        content_dict[sha] = retreive_content(sha)
    return content_dict

def main():
    content_dict = dict_content()
    line = "\n--------------------------------\n"
    content = ""
    
    for sha in content_dict.keys():
        return_content = line + "SHA " + sha + ":\n" + content_dict[sha]
        content += return_content

    sys.stdout.write(content)

if __name__ == "__main__":
    sys.exit(main())
