#!/usr/bin/python

import sys
import os

from hpcbench.parser import Config_parser
from hpcbench.benchdir import Benchdir
from hpcbench.executor import Executor
project_dir_name =  os.path.dirname(os.path.abspath(__file__))
bench_path = os.path.join(project_dir_name,"benchs")
print os.path.abspath(__file__)

nas = Config_parser(os.path.join(bench_path,"nas.yaml"))
stream = Config_parser(os.path.join(bench_path,"stream.yaml"))

print nas.name()
print nas.prepare()

# Initialize directory

benchdir= Benchdir(os.getcwd())

print benchdir.path

stream.list_bench()

run = Executor(nas,benchdir.path)

run.download()
run.prepare()
run.run(2)
