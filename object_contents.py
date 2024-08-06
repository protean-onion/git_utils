#!/usr/bin/python3
# coding: utf-8

from subprocess import run
from os import listdir
import sys

def list_sha():
    sha = []
    objects = ".git/objects"
    for directory in listdir(objects):
        if len(str(directory)) <= 2:
            sha.append(directory + listdir(objects + "/" + directory)[0])
    return sha
    
def retreive_contents(sha_list):
    contents = []
    for sha in sha_list:
        object_content = str(run(["git", "cat-file", "-p", sha]))
        contents.append(object_content)
    return contents

def main():
    retreive_contents(list_sha())

if __name__ == "__main__":
    sys.exit(main())
