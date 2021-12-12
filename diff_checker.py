import os
import subprocess

projects = [
  # 'Chart',
  # 'Cli',
  # 'Closure',
  'Codec',
  # 'Collections',
  # 'Compress',
  # 'Csv',
  'Gson',
  'JacksonCore',
  'JacksonDatabind',
  'JacksonXml',
  'Jsoup',  #WTF
  # 'JxPath',
  # 'Lang',
  'Math',
  # 'Mockito',
  # 'Time',
]

dir_path = "./defects4j"
out_dir_path ="./dataset_diff"

files = [t for t in os.listdir(dir_path) if t.find('_7.txt')  != -1]

diff = []
print(files)
for prj_files in files:
  with_d_prj_files = dir_path + '/' + prj_files
  with open(with_d_prj_files) as f:
    in_7 = f.readlines()
    with_d_8_prj_files = with_d_prj_files.replace('_7.txt','_8.txt')
    prj_8_name = prj_files.replace('_7.txt','_8.txt')
    with open(with_d_8_prj_files) as ff:
      in_8 = ff.readlines()
      if in_7  != in_8 :
        diff.append(prj_files + ' ' + prj_8_name + '\n')

diff.sort()
with open("diff.txt",'w') as df:
  df.writelines(diff)


