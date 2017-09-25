#!/usr/bin/python


## Create workdir structure
import os

class Benchdir:

    def __init__(self, path):
        self.path = os.path.join(path,"benchdir")
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def path(self):
        return self.path
