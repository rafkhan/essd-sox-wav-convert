import sys
import getopt
import os
from pathlib import Path

def getfiles(path):
  for root, d_names, f_names in os.walk(path):
    print(root, d_names, f_names)

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
        outputpath = arg

  print(inputpath)
  print(outputpath)

  getfiles(inputpath)


if __name__ == "__main__":
   main()
