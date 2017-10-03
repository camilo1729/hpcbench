#!/usr/bin/python

import yaml
import os

class Config_parser(object):
    """docstrConfig_parser"""
    def __init__(self, file_name):
        stream = open(file_name,"r")
        try:
          self.config = yaml.load(stream,yaml.SafeLoader)
        except yaml.YAMLError as exc:
          ## This error handling should be improved
          print ("The configuration file is illformatted")
          if hasattr(exc,'problem_mark'):
            print " parser says \n {0}\n {1} {2} \n Please correct data and retry".format(exc.problem_mark,exc.problem,exc.context)

          exit(1)

        self.path = os.path.dirname(file_name)

    def path(self):
      return self.path
    def name(self):
        return self.config['name']

    def download(self):
        return self.config['download'].split('\n')

    def prepare(self):
      if 'prepare' in self.config:
        return self.config['prepare'].split('\n')
      else:
        return []

    def benchs(self):
        return self.config['benchs']

    def workdir(self):
        return self.config['workdir']
    def list_bench(self):
        count = 0
        for bench in self.config['benchs']:
            print "-----------id {0}-------------".format(count)
            print "Name: " + bench['name']
            print "Description: " + bench['desc']
            print "Command used to compile: "
            print bench['compile']
            count+=1;
