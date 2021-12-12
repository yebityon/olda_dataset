import os
import subprocess

projects = [
  # 'Chart',
  # 'Cli',
  # 'Closure',
  # 'Codec',
  # 'Collections',
  # 'Compress',
  # 'Csv',
  # 'Gson',
  # 'JacksonCore',
  # 'JacksonDatabind',
  # 'JacksonXml',
  'Jsoup',  #WTF
  # 'JxPath',
  # 'Lang',
  'Math',
  # 'Mockito',
  # 'Time',
]

java7 = 'java_7_df'
java8 = 'java_8_df'
base_cmd = 'docker'
bash = '/bin/bash'

exec_df = "mkdir /tmp/tmp && defects4j checkout -p Lang -v 1b -w /tmp/tmp/lang_5_buggy && pwd && cd /tmp/tmp/lang_5_buggy/ && defects4j compile && defects4j test && rm -rf /tmp/tmp"

for prj in projects : 
  path = './' + prj + '_bid.txt'
  with open(path) as f:
    ls = f.readlines()
    for l in ls : 
      l = l.strip()
      dirname = prj + '_' + l
      cmd7 = 'mkdir /tmp/tmp/ && defects4j checkout -p ' + prj + " -v " + l + "b " + "-w " + "/tmp/tmp/ && cd " + "/tmp/tmp/"  + ' && defects4j compile && defects4j test && rm -rf /tmp/tmp/'
      write7 = prj + "_" + l  + "_7.txt"

      cmd8 = 'mkdir /tmp/tmp/ && defects4j checkout -p ' + prj + " -v " + l + "b " + "-w " + "/tmp/tmp/ && cd " + "/tmp/tmp/" + '&& defects4j compile && defects4j test && rm -rf /tmp/tmp/' 
      write8 = prj + "_" + l  + "_8.txt"
      
      with open(write7,'w') as fp:
        
        cp = subprocess.run([base_cmd,"exec","-it",java7,bash,"-c",cmd7],stdout=fp)
        print('====> ',prj,l,"OK")

      with open(write8,'w') as fp:
        cp = subprocess.run([base_cmd,"exec","-it",java8,bash,"-c",cmd8],stdout=fp)
      print('====> ',prj,l,"OK")