"""[gae_gen_fyl.py]
this module will generate the required for files to be created
in a new Google AppEngine suitable to act as a Flat Web
___
"""

import os

import gae_gen_txt

def create_file(file_path, file_data):
  fyl = open(file_path, 'w')
  fyl.writelines(file_data)
  fyl.close()

def gen_index_yml(fyl_path):
  fyl_path = os.path.join(fyl_path,"index.yaml")
  create_file(fyl_path, gae_gen_txt.txt_index_yml())

def gen_app_yml(fyl_path, app_name):
  fyl_path = os.path.join(fyl_path,"app.yaml")
  create_file(fyl_path, gae_gen_txt.txt_app_yml(app_name))

def gen_main_py(fyl_path):
  fyl_path = os.path.join(fyl_path,"main.py")
  create_file(fyl_path, gae_gen_txt.txt_main_py())

def gen_flat_root(fyl_path, app_name):
  fyl_path = os.path.join(fyl_path,"index.yaml")
  create_file(fyl_path, gae_gen_txt.txt_flat_root(app_name))

