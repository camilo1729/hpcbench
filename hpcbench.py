#!/usr/bin/python

import sys,os,argparse

from hpcbench.parser import Config_parser
from hpcbench.benchdir import Benchdir
from hpcbench.executor import Executor



parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_true', help='foo help')
subparsers = parser.add_subparsers(dest='cmd')
parser_init = subparsers.add_parser('init', help='init help')

parser_list = subparsers.add_parser('list', help='init help')
parser_list.add_argument('bench', type=str, help='bench help')

parser_download=subparsers.add_parser('download', help='download help')
parser_download.add_argument('bench', type=str, help='bench help')

parser_run=subparsers.add_parser('run', help='run help')
parser_run.add_argument('bench', type=str, help='bench help')
parser_run.add_argument('-i', type=int)

args = parser.parse_args()

def get_bench_config(bench_name):
    bench_dir = os.path.join(os.getcwd(),"benchdir")
    return Config_parser(os.path.join(bench_dir,"{0}.yaml".format(bench_name)))


# import pdb;pdb.set_trace()
if args.cmd == 'init':
  print "Initializing benchmark directory"
  benchdir= Benchdir(os.getcwd())
elif args.cmd == 'list':

  if 'bench' in args:
    print "listing bench: " + args.bench
    bench = get_bench_config(args.bench)
    bench.list_bench()
  else:
    bench_dir = os.path.join(os.getcwd(),"benchdir")
    bench_files = [os.path.splitext(bfile)[0] for bfile in os.listdir(bench_dir) if bfile.endswith('.yaml')]
    for bench in bench_files:
      print bench
elif args.cmd == 'download':
  bench = get_bench_config(args.bench)
  run = Executor(bench,bench.path)
  run.download()

elif args.cmd == 'run':
  bench = get_bench_config(args.bench)
  run = Executor(bench,bench.path)
  run.prepare()
  run.run(args.i)
