import os
import csv

def create_directories(file_path):
  """
      name:           create_directories
      description:    reads all directories from a given csv file.
      parameter:      path to the csv-file
      return:         True if process was successful. False if csv file could not be opened.
  """
  with open(file_path) as csv_file:
    try:
      csv_reader = csv.reader(csv_file, delimiter=',')
    except:
      return False
    else: 

      for row in csv_reader:
        path = row[0]
        if not (os.path.exists(path)):
          try:
            os.mkdir(path)
          except:
            print ("Creation of the directory %s failed" % path)

    return True
        

def main():
  create_directories(r'preset_01.csv')


if __name__ == "__main__":
    main()