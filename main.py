from os import walk
from os import listdir

def main():
    f = []
    for (dirpath, dirnames, filenames) in walk(r'C:\Users\jakob\Downloads'):
        f.extend(filenames)
        print(filenames)
        break

    for files in listdir(r'C:\Users\jakob\Downloads'):
        print(files)
        

if __name__ == "__main__":
    main()