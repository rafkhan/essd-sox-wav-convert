import sys
import getopt
import os
from pathlib import Path

# https://www.threetom.com/news/batch-conversion-of-samples-for-erica-sample-drum/
# sox -G input.wav --norm=-1 -b 16 -r 44.1k -c 1 output.wav

def sox_convert_file(root, filename, outputroot, srcdir_prefix):
  final_in_path = os.path.join(root,filename)
  final_out_path = os.path.join(outputroot, root[srcdir_prefix:], filename)
  cmd = "sox -G \"" + final_in_path + "\" --norm=-1 -b 16 -r 44.1k -c 1 \"" + final_out_path + "\""
  print(final_out_path)
  os.system(cmd)

def get_srcdir_prefix_index(srcdir):
    srcdir = os.path.abspath(srcdir)
    return len(srcdir) + len(os.path.sep)

# https://stackoverflow.com/questions/15663695/shutil-copytree-without-files
def create_empty_dirtree(srcdir, srcdir_prefix, dstdir, onerror=None):
  for root, dirs, _ in os.walk(srcdir, onerror=onerror):
    for dirname in dirs:
      dirpath = os.path.join(dstdir, root[srcdir_prefix:], dirname)
      try:
        os.mkdir(dirpath)
      except OSError as e:
        if onerror is not None:
          onerror(e)

def convert_input_directory(inputpath, outputpath):
  srcdir_prefix = get_srcdir_prefix_index(inputpath)
  create_empty_dirtree(inputpath, srcdir_prefix, outputpath)

  for root, _, f_names in os.walk(inputpath):
    for filename in f_names:
      if filename.endswith(('.wav', '.mp3', '.aiff')):
        sox_convert_file(root, filename, outputpath, srcdir_prefix)

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

  print('Reading from', inputpath)
  convert_input_directory(inputpath, outputpath)

if __name__ == "__main__":
   main()
