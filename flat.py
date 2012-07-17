#!/usr/bin/env python
"""[flat.py]
this will create the structure for a new Google AppEngine suitable
to act as a Flat Web with the GAE Application Name provided as parameter

#python flat.py $GAE_APPLICATION_NAME
___
"""

import os
import sys

import gae_gen_fyl

def create_flat_web(gae_app_name):
  gae_app_path = os.path.join(os.getcwd(),gae_app_name)
  flat_dir_path = os.path.join(gae_app_path,"flat_web")
  if not os.path.exists(gae_app_path):
    #dir-structure generation
    os.makedirs(gae_app_path)
    os.makedirs(flat_dir_path)
    #required file generation
    gae_gen_fyl.gen_index_yml(gae_app_path)
    gae_gen_fyl.gen_app_yml(gae_app_path, gae_app_name)
    gae_gen_fyl.gen_main_py(gae_app_path)
    gae_gen_fyl.gen_flat_root(flat_dir_path, gae_app_name)
  else:
    print "Error: " + str(gae_app_path) + " already exists."
    
if __name__ == '__main__':
  if sys.argv.__len__()==2:
    gae_app_name = sys.argv[1]
    create_flat_web(gae_app_name)
  else:
    print "Wrong Command Execution"
    print "Syntax: #python flat.py GAE_APP_NAME"
