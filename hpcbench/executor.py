#!/usr/bin/python

import os
import subprocess
import time
import re
from datetime import datetime
import socket

class Executor:

    def __init__(self,bench_config,bench_dir):
        self.bench_config = bench_config
        self.top_benchdir = bench_dir
        self.bench_dir = os.path.join(bench_dir,self.bench_config.name())
        if not os.path.exists(self.bench_dir):
            os.makedirs(self.bench_dir)

    def download(self):
        ## create file to not download twice
        ready_file = os.path.join(self.bench_dir,".downloaded_ok")
        if os.path.exists(ready_file) :
          print "Already download skipping in workdir directory..."
        else:
          cmd = ";".join(self.bench_config.download())
          p=subprocess.Popen(cmd, shell=True, cwd=self.bench_dir,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
          for line in p.stdout.readlines():
            print line
          p.wait()
          if p.returncode == 0:
            file = open(ready_file,"w")
            file.write("OK")
            file.close()
          else:
            print("Error downloaing benchfile")


    def prepare(self):
      ready_file = os.path.join(self.bench_dir,".prepare_ok")
      if os.path.exists(ready_file) :
        print "Already prepared in workdir directory..."
      else:
        cmd_array = self.bench_config.prepare()
        if cmd_array :
          cmd = ";".join(cmd_array)
          p=subprocess.Popen(cmd, shell=True, cwd=self.bench_dir,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
          for line in p.stdout.readlines():
            print line
          p.wait()
          if p.returncode == 0:
            file = open(ready_file,"w")
            file.write("OK")
            file.close()
          else:
            print("Error preparing bench")
        else:
          return 0

    def read_envvar(self):
      env_file_path = os.path.join(self.top_benchdir,".envars")
      if os.path.exists(env_file_path):
        env_file = open(env_file_path,'r')
        envvar_re = re.compile("^export\s*(?P<var_name>\w+)=(?P<value>\S+)")
        envvar_dic = {}
        for line in env_file.readlines():
          env_match = envvar_re.match(line.strip())
          envvar_dic[env_match.group('var_name')] = env_match.group('value')
        return envvar_dic
      else:
        return {}

    def gen_run_info(self):
        captured_time = datetime.now()
        hostname = socket.gethostname()
        self.header = "captured on: {0}\n".format(captured_time)
        self.header+= "hostname: {0}\n".format(hostname)
        self.header+= "==========hpcbench=================\n"

    def run(self,cmd_id):
        list_cmd = self.bench_config.benchs()
        bench_to_run = list_cmd[cmd_id]
        #compile
        cmd = bench_to_run['compile']
        print "Compiling bench: " + cmd
        workdir_exe = os.path.join(self.bench_dir,self.bench_config.workdir())
        p=subprocess.Popen(cmd, shell=True, cwd=workdir_exe,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print line
        print "Running bench ..."
        ## adding env variables
        output_filename = os.path.join(self.bench_dir,"{2}-{0}-{1}".format(self.bench_config.name(),int(time.time()),bench_to_run['name']))
        output = open(output_filename, 'w')
        self.gen_run_info()
        output.write(self.header)
        cmd = bench_to_run['run']
        p=subprocess.Popen(cmd, shell=True, cwd=workdir_exe,stdout=output, stderr=subprocess.STDOUT, env=self.read_envvar())
