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
    
def retreive_content(sha):
    object_content = str(run(["git", "cat-file", "-p", sha]))
    return object_content

def main():
    sha_list = list_sha()
    line = "--------------------"
    for sha in sha_list:
        print("SHA " + sha + ":\n")
        print(retreive_content(sha))
        print(line)

if __name__ == "__main__":
    sys.exit(main())
