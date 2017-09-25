#!/usr/bin/python

import yaml


class Config_parser(object):
    """docstrConfig_parser"""
    def __init__(self, file_name):
        stream = open(file_name,"r")
        self.config = yaml.load(stream)

    def name(self):
        return self.config['name']

    def prepare(self):
        return self.config['prepare'].split('\n')

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
