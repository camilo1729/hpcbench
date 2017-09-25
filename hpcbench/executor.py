#!/usr/bin/python

import os
import subprocess

class Executor:

    def __init__(self,bench_config,bench_dir):
        self.bench_config = bench_config
        self.bench_dir = os.path.join(bench_dir,self.bench_config.name())
        if not os.path.exists(self.bench_dir):
            os.makedirs(self.bench_dir)

    def compile(self):
        cmd = ";".join(self.bench_config.prepare())
        p=subprocess.Popen(cmd, shell=True, cwd=self.bench_dir,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print line

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
        cmd = bench_to_run['run']
        p=subprocess.Popen(cmd, shell=True, cwd=workdir_exe,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print line
