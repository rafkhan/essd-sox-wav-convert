import sys
import getopt
import os
from pathlib import Path

def sox_convert_file(root, filename):
  print(root + '/' + filename)

def convert_input_directory(path):
  for root, _, f_names in os.walk(path):
    for filename in f_names:
      if filename.endswith(('.wav', '.mp3', '.aiff')):
        sox_convert_file(root, filename)

def main():
  inputpath = ''
  outputpath = ''

  try:
    opts, _ = getopt.getopt(sys.argv[1:], "h:i:o:")
  except getopt.GetoptError:
    print('test.py -i <inputfile> -o <outputfile>')
    sys.exit(2)

  for opt, arg in opts:
    if opt == '-h':
        print('essd-sox-wav-convert.py -i <inputfile> -o <outputfile>')
        sys.exit(0)

    elif opt in ("-i", "--in"):
        inputpath = Path(arg).resolve()

    elif opt in ("-o", "--out"):
        outputpath = Path(arg).resolve(arg)

  print('Reading from', inputpath)
  print('Writing to', outputpath)
  convert_input_directory(inputpath)

if __name__ == "__main__":
   main()
