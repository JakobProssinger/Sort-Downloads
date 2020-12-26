from os import walk

import os
import csv

def receive_selectors(path):
    """
    name:           receive_selectors
    description:    reads all selectors from an csv file. Each selector has two properties, the first properties is 
                        the directory and the second properties is the file-ending.
    parameter:      path to the csv-file
    return: directories and file-endings.         
    """
    directories = []
    file_endings = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            directories.append(row[0])
            file_endings.append(row[1])
        
    return directories, file_endings


def receive_file_names(path):
    """
    name:           rechive_file_names
    description:    searches for all files in a given path
    parameter:      path to the folder
    return:         list of all names of the files in this folder
    """
    for (dirpath, dirnames, filenames) in walk(path):
        return filenames


def main():
  files_names = receive_file_names(r'C:\Users\jakob\Downloads')

     
if __name__ == "__main__":
    main()