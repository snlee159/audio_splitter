import subprocess, os, argparse, textwrap

def split_file(filename, n_parts, save_dir):
  """
  Actually does the splitting using ffmpeg.

  Inputs:
  filename  - str  - the audio file to split
  n_parts   - int  - the number of equal parts to split it into
  save_dir  - str  - where the split files will be saved

  Outputs:
  out_files - list - the filenames of the split files.
  """
  # Get the length of the audio file
  file_len = float(subprocess.check_output([f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {filename}'], stderr=subprocess.STDOUT, shell=True))
  split_len = file_len / n_parts

  for i in range(n_parts):
    print(f'Saving part {i+1} of {n_parts}')
    out_file = f'{save_dir}/{filename.split("/")[-1][:-4]}_part{i}.m4a'
    subprocess.call([f'ffmpeg -i {filename} -ss {split_len * i} -t {split_len} -acodec copy {out_file}'], shell=True)


def main():
  parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
                                   Use to split audio files into x number of files.

                                   For example, use the following command:
                                   python audio_splitter.py --audio_file <audio_input_filename> --n_parts 3 --save_dir <directory_to_save_split_files>

                                   will split the specified file into 3 equal parts and save the files to the specified directory.
                                   '''))

  parser.add_argument(
    '--audio_file',
    type=str,
    help='The filename of the audiofile you would like to split')
  parser.add_argument('--n_parts',
                      type=int,
                      help='The number of equal parts to split the data into',
                      default=2)
  parser.add_argument('--save_dir',
                      type=str,
                      help='Where the split files will be saved')

  args = parser.parse_args()

  if not args.save_dir:
    args.save_dir = '/'.join(args.audio_file.split('/')[:-1])
    if args.save_dir == '':
        args.save_dir = '.'
  elif args.save_dir[-1] == '/':
    args.save_dir = args.save_dir[:-1]

  split_file(args.audio_file, args.n_parts, args.save_dir)


if __name__ == '__main__':
  main()
