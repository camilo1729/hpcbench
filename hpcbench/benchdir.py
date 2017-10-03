#!/usr/bin/python


## Create workdir structure
import os
import urllib

class Benchdir:

    def __init__(self, path):
        self.benchdir = os.path.join(path,"benchdir")
        if not os.path.exists(self.benchdir):
            os.makedirs(self.benchdir)
            # Download benchs definitions
            upstream_repository = "https://raw.githubusercontent.com/camilo1729/hpcbench/master/"
            bench_list = "{0}/benchs/bench_list.txt".format(upstream_repository)
            bench_list_path = os.path.join(self.benchdir,"bench_list.txt")
            cmd = "wget {0} -O {1}".format(bench_list,bench_list_path)
            os.system(cmd)
            if os.path.exists(os.path.join(self.benchdir,"bench_list.txt")):
              bench_list_file = open(bench_list_path,"r")
              for line in bench_list_file.readlines():
                bench_file = line.strip()
                bench_web_path = "{0}/benchs/{1}".format(upstream_repository,bench_file)
                cmd = "wget {0} -O {1}".format(bench_web_path,os.path.join(self.benchdir,bench_file))
                os.system(cmd)

    def path(self):
        return self.benchdir
