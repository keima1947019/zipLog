import os
import zipfile
import time
import shutil

def delete_log_files(directory):
  """
  Delete all files under the directory named “log” under the current directory.

  Args:
    None

  Returns:
    None
  """
  for root, dirs, files in os.walk(directory):
    if os.path.basename(root) == 'log':
      for file in files:
        os.remove(os.path.join(root, file))
        print('Deleted: ', os.path.join(root, file))

def compress_logs(current_dir):
  """
  Compress all files under the directory named “log” under the current directory.

  Args:
    None

  Returns:
    None
  """
  current_time = time.time()
  time_struct = time.localtime(current_time)
  yyyymmdd = time.strftime("%Y_%m%d_%H%M_%S", time_struct)
  archive_dir = 'log_' + yyyymmdd
  os.mkdir(archive_dir)

  i = 1
  for root, _, files in os.walk(current_dir):
    if root.endswith('log'):
      target_files = []
      for file in files:
        if file.endswith('.log'):
          target_files.append(os.path.join(root, file))
      archive_name = os.path.relpath(root, current_dir).replace('\\','_')
      archive_path = str(i) + '_' + archive_name + '.zip'
      print(archive_path, ' has files as follows')
      with zipfile.ZipFile(archive_path, 'w') as zf:
        for file in target_files:
          zf.write(file, arcname=os.path.relpath(file, root))
          print(os.path.relpath(file, root))
        i = i + 1
      shutil.move(archive_path, archive_dir)

if __name__ == '__main__':
  current_dir = os.getcwd()
  compress_logs(current_dir)
  delete_log_files(current_dir)
