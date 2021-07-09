import sys
import getopt
import os
from pathlib import Path

# https://www.threetom.com/news/batch-conversion-of-samples-for-erica-sample-drum/
# sox -G input.wav --norm=-1 -b 16 -r 48k -c 1 output.wav

def sox_convert_file(root, filename):
  # os.
  print(root + '/' + filename)

# https://stackoverflow.com/questions/15663695/shutil-copytree-without-files
def create_empty_dirtree(srcdir, dstdir, onerror=None):
    srcdir = os.path.abspath(srcdir)
    srcdir_prefix = len(srcdir) + len(os.path.sep)
    os.makedirs(dstdir, exist_ok=True)
    for root, dirs, files in os.walk(srcdir, onerror=onerror):
        for dirname in dirs:
            dirpath = os.path.join(dstdir, root[srcdir_prefix:], dirname)
            try:
                os.mkdir(dirpath)
            except OSError as e:
                if onerror is not None:
                    onerror(e)

def convert_input_directory(inputpath, outputpath):
  create_empty_dirtree(inputpath, outputpath)

  for root, _, f_names in os.walk(inputpath):
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
  convert_input_directory(inputpath, outputpath)

if __name__ == "__main__":
   main()
