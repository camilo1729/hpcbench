#!/usr/bin/python

import sys
import os

from hpcbench.parser import Config_parser
from hpcbench.benchdir import Benchdir
from hpcbench.executor import Executor
project_dir_name =  os.path.dirname(os.path.abspath(__file__))
bench_path = os.path.join(project_dir_name,"benchs")
print os.path.abspath(__file__)
p = Config_parser(os.path.join(bench_path,"nas.yaml"))

print p.name()
print p.prepare()

# Initialize directory

benchdir= Benchdir(os.getcwd())

print benchdir.path

p.list_bench()

run = Executor(p,benchdir.path)

run.run(0)
#run.compile()
