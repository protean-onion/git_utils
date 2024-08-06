#!/usr/bin/python3
# coding: utf-8

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
    object_content = str(run(["git", "cat-file", "-p", sha]))[:-1] # omit process completion information
    return object_content

def list_content():
    content_list = []
    for sha in list_sha():
        content_list.append(retreive_content(sha))
    return content_list

def main():
    sha_list = list_sha()
    line = "\n--------------------\n\n"
    
    for sha in sha_list:
        return_content = "SHA " + sha + ":\n" + retreive_content(sha) + line

if __name__ == "__main__":
    sys.exit(main())
